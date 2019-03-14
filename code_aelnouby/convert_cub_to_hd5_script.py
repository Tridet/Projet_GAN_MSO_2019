import os
from os.path import join, isfile
import numpy as np
import h5py
import torch
from glob import glob
from PIL import Image 
import yaml
import io
import pdb

with open('config.yaml', 'r') as f:
    config = yaml.load(f)

images_path = config['birds_images_path']
embedding_path = config['birds_embedding_path']
text_path = config['birds_text_path']
datasetDir = config['birds_dataset_path']

val_classes = open(config['val_split_path']).read().splitlines()
train_classes = open(config['train_split_path']).read().splitlines()
test_classes = open(config['test_split_path']).read().splitlines()
f = h5py.File(datasetDir, 'w', swmr= True)
train = f.create_group('train')
valid = f.create_group('valid')
test = f.create_group('test')

# Test pour vérifier que toutes les classes existent bien
for _class in sorted(os.listdir(embedding_path)):
    split = ''
    if _class in train_classes:
        pass
    elif _class in val_classes:
        pass
    elif _class in test_classes:
        pass
    else:
        raise ValueError(_class + "is not defined ! Try changing classes files !")


for _class in sorted(os.listdir(embedding_path)):
    split = ''
    if _class in train_classes:
        split = train
    elif _class in val_classes:
        split = valid
    elif _class in test_classes:
        split = test

    data_path = os.path.join(embedding_path, _class)
    txt_path = os.path.join(text_path, _class)

    for example, txt_file in zip(sorted(glob(data_path + "/*.t7")), sorted(glob(txt_path + "/*.txt"))):
        example_data = torch.load(example)  #à remplacer par torch.load() certainement
        img_path = example
        embeddings = example_data
        classe = img_path.split('\\')[1]
        example_name = img_path.split('\\')[2][:-3]

        f2 = open(txt_file, "r")
        txt = f2.readlines()
        f2.close()

        img_path = images_path + "\\" + classe + "\\" + example_name + ".jpg"
        img = open(img_path, 'rb').read()
        
        txt_choice = np.random.choice(range(10), 5)

        embeddings = embeddings[txt_choice]
        txt = np.array(txt)
        txt = txt[txt_choice]
        dt = h5py.special_dtype(vlen=str)

        for c, e in enumerate(embeddings):
            ex = split.create_group(example_name + '_' + str(c))
            ex.create_dataset('name', data=example_name)
            ex.create_dataset('img', data=np.void(img))
            ex.create_dataset('embeddings', data=e)
            ex.create_dataset('class', data=_class)
            ex.create_dataset('txt', data=txt[c].astype(object), dtype=dt)

    print(_class)
f.close()



