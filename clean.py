#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:41:49 2017

@author: rathorea
"""
import re
import string
from nltk import sent_tokenize
from nltk.corpus import stopwords
import create_vector


def read_file(filename):
    opened_file = open(filename, 'r')
    text = opened_file.read()
    opened_file.close()
    return text


def vectorize(text):
    #split the words by whitespace
    words = []
    for txt in text:
        words += [normalize(strip_punctuation(txt))]
    print(words[:100])
    return words
    
    
def remove_punctuation(text):
    words = re.split(r'\W+', text)
    return words


def strip_punctuation(text):
    words = text.split()
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    stripped = [w for w in stripped if w!= '']
    return stripped


def normalize(words):
    words = [word.lower() for word in words]
    return words


def split_sentence(text):
    sentences = sent_tokenize(text)
    return sentences


def remove_stopwords(words):
    # tokenize words
    # tokens = word_tokenize(text)
    # tokens = [w.lower() for w in tokens]
    # remove punctuation
    # remove remaining tokens that are not alphabetic
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return words


if __name__ == "__main__":
    # text = read_file('../sentiment/neg.txt')
    text = 'Still not over pizza getting overlooked in the favorite things song. #TheSoundOfMusicLive'
    sents = split_sentence(text)
    #print(sents[:100])
    sents = vectorize(sents)
    vecs = []
    for words in sents:
        vecs += [remove_stopwords(words)]
    print(vecs)
