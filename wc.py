import sys
import argparse
import pickle
from string import punctuation

#only implement load and save , load and save take over --pfile
def wordfreq(fname, stripPunc, toLower) :
    wordDict = {}
    with open(fname) as f:
        words = f.read().split()
        for word in words :
            if stripPunc :
                word = word.strip(punctuation)
            if toLower :
                word = word.lower()
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1
    return wordDict

if __name__== '__main__':
    parser = argparse.ArgumentParser('Calculate word frequency distribution')
    parser.add_argument('file')
    parser.add_argument('-p', '--strip')
    parser.add_argument('-c', '--convert')
    parser.add_argument('-s', '--sort')

    args = parser.parse_args()


