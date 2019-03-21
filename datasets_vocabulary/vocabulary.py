#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:03:53 2019

@author: pascalgodbillot
"""

import os
import string
import json
import matplotlib.pyplot as plt
                
def get_vocabulary(dataset_name):
    """
    to use this function you need to put text descriptions of birds or flowers
    dataset inside a text folder. Dataset available at https://github.com/reedscot/cvpr2016
    """
    vocabulary = {}
    cwd = os.getcwd()
    global_path = cwd+'/text/'+ dataset_name + '/text_c10/'
    all_folders = os.listdir(global_path)
    folders = [folder for folder in all_folders if folder[0]!='.']
    for folder in folders:
        path = global_path + folder +'/'
        all_files = os.listdir(path)
        files = [file for file in all_files if file.split('.')[1]=='txt']
        for file in files :
            sub_path = path + file
            with open(sub_path) as f :
                sentences_init = [line.strip() for line in f if line.strip()]
                str1='' #specifies the list of characters that need to be replaced.
                str2='' #specifies the list of characters with which the characters need to be replaced.
                str3=string.punctuation #Specifies the list of characters that needs to be deleted.
                translator=str.maketrans(str1,str2,str3)
                sentences = [sentence.lower().translate(translator) for sentence in sentences_init]
                word_list = [word for sentence in sentences for word in sentence.split()]
                for word in word_list :
                    if word in vocabulary.keys() :
                        current_value = vocabulary[word]
                        vocabulary[word] = current_value + 1 
                    else : 
                            vocabulary[word] = 1
    return vocabulary

def voc2json(voc, name):
    with open(name + "_vocabulary.json", "wb") as f:
        f.write(json.dumps(voc).encode("utf-8"))
        f.close
        
def json2voc(name):
    with open(name + "_vocabulary.json", "r") as f:
        vocabulary = json.load(f)
    return vocabulary
    
def get_length_vocabulary(vocabulary):
    length = len([key for key in vocabulary.keys()])
    total_words = 0
    for key in vocabulary:
        total_words += vocabulary[key]
    return length, total_words

def get_frequent_voc(vocabulary, threshold):
    frequent_vocabulary = {}
    for key in vocabulary.keys():
        if vocabulary[key] >= threshold :
            frequent_vocabulary[key] = vocabulary[key]
    return frequent_vocabulary


def get_color_vocabulary(vocabulary):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'black', 'grey', 'white', 'dark']
    color_vocabulary = {}
    for key in vocabulary.keys():
        if key in colors :
            color_vocabulary[key] = vocabulary[key]
    return color_vocabulary

def get_barplot_color(vocabulary, name):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'black', 'grey', 'white', 'dark']
    color_vocabulary = {}
    for key in vocabulary.keys():
        if key in colors :
            color_vocabulary[key] = vocabulary[key]
    length, total_words = get_length_vocabulary(vocabulary)
    plt.figure(figsize=(8,4))
    sorted_values = sorted([value/total_words for value in color_vocabulary.values()],reverse = True)
    plt.bar(range(len(color_vocabulary)), sorted_values, align='center', color='lightseagreen')
    sorted_ticks = sorted(color_vocabulary, key=color_vocabulary.__getitem__, reverse = True)
    plt.xticks(range(len(color_vocabulary)), sorted_ticks)
    plt.title('Occurences of colors for ' + name + ' (%)')
    plt.show()


def get_bodypart_vocabulary(vocabulary, name):
    if name == 'flowers':
        bodyparts = ['pistil','petals','center','stamen','edges','pedicel', 'stigma']
    if name == 'birds':
        bodyparts = ['beak','wings','breast','feathers','body','bill','head','crown','belly','throat']
    bodypart_vocabulary = {}
    for key in vocabulary.keys():
        if key in bodyparts :
            bodypart_vocabulary[key] = vocabulary[key]
    return bodypart_vocabulary


def get_barplot_bodypart(vocabulary, name):
    if name == 'flowers':
        bodyparts = ['pistil','petals','center','stamen','edges','pedicel', 'stigma']
    if name == 'birds':
        bodyparts = ['beak','wings','breast','feathers','body','bill','head','crown','belly','throat']
    bodypart_vocabulary = {}
    for key in vocabulary.keys():
        if key in bodyparts :
            bodypart_vocabulary[key] = vocabulary[key]
    length, total_words = get_length_vocabulary(vocabulary)
    plt.figure(figsize=(8,4))
    sorted_values = sorted([(value/total_words)*100 for value in bodypart_vocabulary.values()],reverse = True)
    plt.bar(range(len(bodypart_vocabulary)), sorted_values, align='center', color='lightseagreen')
    sorted_ticks = sorted(bodypart_vocabulary, key=bodypart_vocabulary.__getitem__, reverse = True)
    plt.xticks(range(len(bodypart_vocabulary)), sorted_ticks)
    plt.title('Occurences of body parts for ' + name + ' (%)')
    plt.show()
    

def get_adjective_vocabulary(vocabulary, name):
    if name == 'flowers':
        bodyparts = ['shaped' ,'large', 'center', 'thin','rounded','bright', 'oval']
    if name == 'birds':
        bodyparts = ['small', 'short', 'long', 'bright', 'pointed', 'pointy', 'light', 'large']
    bodypart_vocabulary = {}
    for key in vocabulary.keys():
        if key in bodyparts :
            bodypart_vocabulary[key] = vocabulary[key]
    return bodypart_vocabulary


def get_barplot_adjective(vocabulary, name):
    if name == 'flowers':
        bodyparts = ['shaped' ,'large', 'center', 'thin','rounded','bright', 'oval']
    if name == 'birds':
        bodyparts = ['small', 'short', 'long', 'bright', 'pointed', 'pointy', 'light', 'large']
    bodypart_vocabulary = {}
    for key in vocabulary.keys():
        if key in bodyparts :
            bodypart_vocabulary[key] = vocabulary[key]
    length, total_words = get_length_vocabulary(vocabulary)
    plt.figure(figsize=(8,4))
    sorted_values = sorted([(value/total_words)*100 for value in bodypart_vocabulary.values()],reverse = True)
    plt.bar(range(len(bodypart_vocabulary)), sorted_values, align='center', color='lightseagreen')
    sorted_ticks = sorted(bodypart_vocabulary, key=bodypart_vocabulary.__getitem__, reverse = True)
    plt.xticks(range(len(bodypart_vocabulary)), sorted_ticks)
    plt.title('Occurences of adjectives describing ' + name + ' (%)')
    plt.show()


#vocabulary_birds = get_vocabulary('birds')
#vocabulary_flowers = get_vocabulary('flowers')

#voc2json(vocabulary_birds, 'birds')
#voc2json(vocabulary_flowers, 'flowers')
    
vocabulary_birds = json2voc('birds')
vocabulary_birds = json2voc('flowers')
    
vocabulary_birds = get_vocabulary('birds')
vocabulary_flowers = get_vocabulary('flowers')

length_birds, total_words_birds = get_length_vocabulary(vocabulary_birds)
length_flowers, total_words_flowers = get_length_vocabulary(vocabulary_flowers)

threshold = 5000
frequent_vocabulary_birds = get_frequent_voc(vocabulary_birds, threshold)
frequent_vocabulary_flowers = get_frequent_voc(vocabulary_flowers, threshold)

get_barplot_color(vocabulary_birds, 'birds')
get_barplot_color(vocabulary_flowers, 'flowers')
    
get_barplot_bodypart(vocabulary_birds, 'birds')
get_barplot_bodypart(vocabulary_flowers, 'flowers')

get_barplot_adjective(vocabulary_birds, 'birds')
get_barplot_adjective(vocabulary_flowers, 'flowers')