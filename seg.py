#!/bin/python

import jieba
import sys
from collections import Counter

def get_file(f):
	return open(f).read()

def count_words(words, stoplist):
	c = Counter()
	for word in words:
		if word not in stoplist:
			c[word] += 1
	return c

def get_words(s):
	seg_list = '~~'.join(jieba.cut(s, cut_all=True))
	return seg_list.split('~~')


def main():
	myfile = get_file(sys.argv[1])
	words = get_words(myfile)
	stopwords = open('stopwords.txt').read()
	c = count_words(words, stopwords)
	for a, b in c.most_common(10):
		print('{}\t{}'.format(a, b))

if __name__ == "__main__":
	main()
