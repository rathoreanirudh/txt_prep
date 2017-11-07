#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:55:36 2017

@author: rathorea
"""
import word2vec
import re
import collections

def load_glove(filename):
    text = open(filename, 'r')
    model = {}
    for line in text:
        splitLine = line.split()
        word = splitLine[0]
        embedding = [float(val) for val in splitLine[1:]]
        model[word] = embedding
    return model


def create_vocab(filename):
    raw_text = open(filename).read()
    wordList = re.sub("[^\w]", " ", raw_text.lower()).split()
    vocab = sorted(list(set(wordList)))
    return vocab
    
    
def load_w2v(filename):
    vocab = create_vocab(filename)
    thefile = open('model/vocab.txt', 'w')
    for item in vocab:
        # print item
        thefile.write("%s\n" % item)
    thefile = open('model/vocab.txt', 'r')
    #print(vocab)
    word2vec.word2vec("model/vocab.txt", "model/model.bin",  size = 100, verbose = True, min_count = 1)
    model = word2vec.load('model/model.bin')
    return model


def load_bow(filename):
    text = open(filename, 'r')
    bagofwords = [ collections.Counter(re.findall(r'\w+', txt)) for txt in text]
    model = sum(bagofwords, collections.Counter())
    return model

def fill_null(dim):
    null_vec = []
    for i in range(0, dim):
        null_vec.append(0.0)
    return null_vec


def to_vec(word, dim, model):
    null_vec = fill_null(dim)
    vec = []
    try:
        vec = model[word]
    except KeyError:
        print('Word '+word+' not in dictionary')
        vec = null_vec
    return vec

if __name__ == '__main__':

    # print('loading glove')
    # filename = '/Users/rathorea/data/glove/glove.6B.100d.txt'
    # model = load_glove(filename)
    # print(model['king'])

    # print('loading bow')

    # filename = '../sentiment/neg.txt'
    # model = load_bow(filename)
    # print(model['the'])

    # model = load_w2v(filename)
    # print(model['she'])

    print('hello')
