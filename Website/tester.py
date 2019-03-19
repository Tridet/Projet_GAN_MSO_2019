import numpy as np
import torch
from torch.autograd import Variable
from models.gan_factory import gan_factory
from PIL import Image

import random
import os

class Tester(object):
    def __init__(self, type, dataset, pre_trained_gen):
        self.generator = torch.nn.DataParallel(gan_factory.generator_factory(type))
        self.generator.load_state_dict(torch.load(pre_trained_gen, map_location='cpu'))


        if dataset == 'birds':
            self.model = torch.load('data/model_birds.t7', map_location='cpu')
        elif dataset == 'flowers':
            self.model = torch.load('data/model_flowers.t7', map_location='cpu')
        else:
            print('Dataset not supported, please select either birds or flowers.')
            exit()
        

    def predict(self, txt=None):
        if txt==None:
            txt = ["the blue flower has a yellow center","the yellow flower has a blue pistil", "the red flower has pink pistil and long petals"]
        size = len(txt)
        lines = open('rando.txt').read().splitlines()
        txt[0]=random.choice(lines)

        right_embed = torch.from_numpy(self.model.encode(txt, tokenize=True))
        right_embed = Variable(right_embed)
        noise = Variable(torch.randn(size, 100))
        noise = noise.view(noise.size(0), 100, 1, 1)
        fake_images = self.generator(right_embed, noise)

        for image, t in zip(fake_images, txt):
            im = Image.fromarray(image.data.mul_(127.5).add_(127.5).byte().permute(1, 2, 0).cpu().numpy())
            print(t)
        
        return im


if __name__ == "__main__":
    tester = Tester(type='gan',
                    dataset='flowers',
                    pre_trained_gen='data/gen_170.pth')
    tester.predict(txt=["the medium sized bird has a dark grey color", "the bird has green feathers and a dark tail"])
