# -*- coding: utf-8 -*-

"""
EDIT #1: Get rid of that motherfucking ´vbag´.
"""

import time

def calculate_score(text):
    """ project euler #22: calculates the total of all name scores in ´text´. """
    alphabet = '.abcdefghijklmnopqrstuvwxyz'
    corpus = sorted([word.lower().replace('"', '') for word in text.split(',')])
    total_score = \
        sum([sum([alphabet.index(c) for c in word]) * (corpus.index(word) + 1) for word in corpus])
    return total_score

if __name__ == '__main__':
    text = open('names.txt').read()
    t1 = time.time()
    score = calculate_score(text)
    t2 = time.time()
    print "The calculation took", t2 - t1, "seconds to run: score is", score
