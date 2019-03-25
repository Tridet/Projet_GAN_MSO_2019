import numpy as np
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

class Tester(object):
    def __init__(self, type, dataset, save_path, pre_trained_gen, pre_trained_disc):
        with open('config.yaml', 'r') as f:
            config = yaml.load(f)

        self.dataset = dataset
        self.generator = torch.nn.DataParallel(gan_factory.generator_factory(type).cuda())
        self.discriminator = torch.nn.DataParallel(gan_factory.discriminator_factory(type).cuda())
        if pre_trained_disc:
            self.discriminator.load_state_dict(torch.load(pre_trained_disc))
        else:
            self.discriminator.apply(Utils.weights_init)

        if pre_trained_gen:
            self.generator.load_state_dict(torch.load(pre_trained_gen))
        else:
            self.generator.apply(Utils.weights_init)

        if self.dataset == 'birds':
            self.model = torch.load(config["birds_model_path"])
        elif self.dataset == 'flowers':
            self.model = torch.load(config["flowers_model_path"])
        else:
            print('Dataset not supported, please select either birds or flowers.')
            exit()

        self.checkpoints_path = 'checkpoints'
        self.save_path = save_path


    def predict(self, txt=None):

        if txt==None:
            txt = ["the white flower has a yellow center"]
        
        if self.dataset=="flowers":
            lines = open('rando.txt').read().splitlines()
        else :
            lines = open('rando_birds.txt').read().splitlines()

        txt = random.sample(lines, 31) + txt
        size = len(txt)

        if not os.path.exists('results/{0}'.format(self.save_path)):
            os.makedirs('results/{0}'.format(self.save_path))

        right_embed = torch.from_numpy(self.model.encode(txt, tokenize=True))
        right_embed = Variable(right_embed)#.cuda()
        noise = Variable(torch.randn(size, 100))#.cuda()
        noise = noise.view(noise.size(0), 100, 1, 1)
        fake_images = self.generator(right_embed, noise)
        #self.logger.draw(right_images, fake_images)

        image = fake_images[-1]
        t = txt[-1]

        im = Image.fromarray(image.data.mul_(127.5).add_(127.5).byte().permute(1, 2, 0).cpu().numpy())
        im.save('results/{0}/{1}.jpg'.format(self.save_path, t.replace("/", "").replace("\n","")[:100]))