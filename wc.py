#Author: Nitzan Saar
import os
import argparse
import pickle
from string import punctuation
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Calculate word frequency distribution')
    parser.add_argument('file_or_directory')
    parser.add_argument('--strip')
    parser.add_argument('--convert')
    parser.add_argument('--load')
    parser.add_argument('--save')
    parser.add_argument('-s', '--sort')

    args = parser.parse_args()

    file_or_directory = args.file_or_directory
    strip = args.strip
    convert = args.convert
    load = args.load
    save = args.save
    sort = args.sort
    wd = {}

    if load:
        with open(load, 'rb') as f:
            wb = pickle.load(f)
    else:
        if os.path.isfile(file_or_directory):
            wd = wordfreq(file_or_directory, strip, convert)
        elif os.path.isdir(file_or_directory):
            for root, dirs, files in os.walk(file_or_directory):
                for filename in files:
                    fname = os.path.join(root, filename)
                    wd = wordfreq(fname, strip, convert)
        else:
            print("Invalid file or directory")

    if save:
        with open(save, 'wb') as f:
            pickle.dump(wd, f)
    if sort:
        print(sorted(wd.items(), key=lambda x: x[1]))
    else:
        print(wd)

