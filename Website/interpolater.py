import numpy as np
from scipy.interpolate import interp1d
import torch
import yaml
import random
from torch import nn
from torch.autograd import Variable

import nltk
from models_ import InferSent
from models.gan_factory import gan_factory
from PIL import Image

import os

class Interpolater(object):
    def __init__(self, type, dataset, save_path, pre_trained_gen):
        with open('config.yaml', 'r') as f:
            config = yaml.load(f)

        self.dataset = dataset

        self.generator = torch.nn.DataParallel(gan_factory.generator_factory(type))        
        if pre_trained_gen:
            self.generator.load_state_dict(torch.load(pre_trained_gen, map_location='cpu'))
        else:
            self.generator.apply(Utils.weights_init)

        if self.dataset == 'birds':
            self.model = torch.load(config["birds_model_path"],map_location='cpu')
        elif self.dataset == 'flowers':
            self.model = torch.load(config["flowers_model_path"],map_location='cpu')
        else:
            print('Dataset not supported, please select either birds or flowers.')
            exit()

        self.checkpoints_path = 'checkpoints'
        self.save_path = save_path


    def interpolate(self, txt=None):

        if txt==None:
            txt = ["this a white flower with a big yellow pistil", "a purple flower with smooth round petals"]

        embed_init = self.model.encode(txt, tokenize=True)

        n = 16

        fst = np.array(embed_init[0])
        snd = np.array(embed_init[1])
        linfit = interp1d([1,n], np.vstack([fst, snd]), axis=0)

        embed = np.array([np.float32(linfit([i]).ravel()) for i in range(1,n+1)])

        size = embed.shape[0]

        if self.dataset=="flowers":
            lines = open('rando.txt').read().splitlines()
        else :
            lines = open('rando_birds.txt').read().splitlines()

        random_txt = random.sample(lines, n-1)
        batch_txt = self.model.encode(random_txt, tokenize=True)
        noise = Variable(torch.randn(size, 100))#.cuda()
        noise = noise.view(noise.size(0), 100, 1, 1)


        if not os.path.exists('results/{0}'.format(self.save_path)):
            os.makedirs('results/{0}'.format(self.save_path))

        for i in range(n):
            current_embed = np.vstack(([batch_txt, embed[i]]))
            right_embed = torch.from_numpy(current_embed)
            right_embed = Variable(right_embed)#.cuda()
            fake_images = self.generator(right_embed, noise)
            #self.logger.draw(right_images, fake_images)
            image = fake_images[-1]
            im = Image.fromarray(image.data.mul_(127.5).add_(127.5).byte().permute(1, 2, 0).cpu().numpy())
            if i==0:
                t = txt[0]
                im.save('results/{0}/{1}.jpg'.format(self.save_path, str(i) + '_' + t.replace("/", "").replace("\n","")[:100]))
            elif i==n-1:
                t = txt[1]
                im.save('results/{0}/{1}.jpg'.format(self.save_path, str(i) + '_' + t.replace("/", "").replace("\n","")[:100]))
            else:
                im.save('results/{0}/{1}.jpg'.format(self.save_path, i))
        