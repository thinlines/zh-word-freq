#!/bin/python

import sys
import argparse
from collections import Counter
import jieba

def count_words(words, stoplist):
	c = Counter()
	for word in words:
		if word not in stoplist:
			c[word] += 1
	return c

def get_words(s):
	seg_list = '~~'.join(jieba.cut(s, cut_all=True))
	return seg_list.split('~~')

parser = argparse.ArgumentParser()
parser.add_argument("file", help="the text file to process")
args = parser.parse_args()

def main():
	zh_file = open(args.file).read()
	words = get_words(zh_file)
	stopwords = open('stopwords.txt').read()
	c = count_words(words, stopwords)
	for a, b in c.most_common():
		print('{:<10}\t{:>d}'.format(a, b))

if __name__ == "__main__":
	main()
