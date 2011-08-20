# -*- coding: utf-8 -*-

import time

def calculate_score(text):
    """ project euler #22: calculates the total of all name scores in ´text´. """
    alphabet = '.abcdefghijklmnopqrstuvwxyz'
    corpus = sorted([word.lower().replace('"', '') for word in text.split(',')])
    vbag = []
    for word in corpus:
        wvalue = sum([alphabet.index(c) for c in word]) * (corpus.index(word) + 1)
        vbag.append(wvalue)
    return sum(vbag)

if __name__ == '__main__':
    text = open('names.txt').read()
    t1 = time.time()
    score = calculate_score(text)
    t2 = time.time()
    print "The calculation took", t2 - t1, "seconds to run."
