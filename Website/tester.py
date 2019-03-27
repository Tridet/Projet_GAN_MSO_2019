import numpy as np
import torch
from torch.autograd import Variable
from models.gan_factory import gan_factory
from PIL import Image
from scipy.interpolate import interp1d

import random
import os
import yaml

class Tester(object):
    def __init__(self, type, dataset, cls_option):
        with open('config.yaml', 'r') as f:
	        self.config = yaml.load(f)
        self.generator = self.__get_generator(type, dataset, cls_option)
        self.model = self.__get_embeddings_model(dataset)
        self.dataset = dataset

    def __get_generator(self, type, dataset, cls_option):
        
        pre_trained_model = self.config[f'{dataset}_{type}{"_cls" if cls_option else ""}_path']
        generator = torch.nn.DataParallel(gan_factory.generator_factory(type))
        generator.load_state_dict(torch.load(pre_trained_model, map_location='cpu'))
        return generator

    def __get_embeddings_model(self, dataset):
        model_path = self.config[f'{dataset}_embeddings_model_path']
        model = torch.load(model_path, map_location='cpu')
        return model

    def predict(self, txt=None):
        txt = self.__get_random_descriptions(31) + txt

        right_embed = torch.from_numpy(self.model.encode(txt, tokenize=True))
        
        return self.generate_from_embeddings(right_embed)
        

    def __get_random_descriptions(self, n):
        random_descriptions_path = self.config[f'{self.dataset}_random_descriptions_path']       
        with open(random_descriptions_path) as f:
            lines = f.read().splitlines()
 
        return random.sample(lines, n)

    def __get_embeddings(self, descriptions):
        return self.model.encode(descriptions, tokenize=True)
    
    def get_interpolated_embeddings(self, description1, description2):
        n = 12 # total number of embeddings
        embeddings = self.__get_embeddings([description1, description2])
        first_embedding = np.array(embeddings[0])
        second_embedding = np.array(embeddings[1])
        linfit = interp1d([1,n], np.vstack([first_embedding, second_embedding]), axis=0)
        embeddings = np.array([np.float32(linfit([i]).ravel()) for i in range(1,n+1)])
        return embeddings

    def generate_from_embeddings(self, right_embed):
        right_embed = Variable(right_embed)
        noise = Variable(torch.randn(right_embed.size(0), 100))
        noise = noise.view(noise.size(0), 100, 1, 1)
        fake_images = self.generator(right_embed, noise)

        image = fake_images[-1]
        im = Image.fromarray(image.data.mul_(127.5).add_(127.5).byte().permute(1, 2, 0).cpu().numpy())
        
        return im
    
    def generate_from_embedding(self, embedding):
        embeddings = self.__get_random_embeddings(32)
        embeddings[31] = torch.from_numpy(np.array(embedding))
        return self.generate_from_embeddings(embeddings)

    def __get_random_embeddings(self, n):
        random_descriptions = self.__get_random_descriptions(n)
        embeddings = torch.from_numpy(self.model.encode(random_descriptions, tokenize=True))
        return embeddings


if __name__ == "__main__":
    tester = Tester(type='gan',
                    dataset='flowers',
                    cls_option=False)
    tester.predict(txt=["the medium sized bird has a dark grey color", "the bird has green feathers and a dark tail"])
