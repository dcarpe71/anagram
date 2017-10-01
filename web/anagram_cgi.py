#!/usr/bin/env python
import cgi
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from collections import defaultdict
from itertools import permutations
import urllib
import sys
import unicodedata


def get_anagram(word, result_list):
    
    # open the file
    searchfile = open("words", "r")

    # sort the word to test
    word_sorted = sorted(word)
    word_len = len(word_sorted)

    # iterate through the file and test
    for line in searchfile:
    
        # strip newline
        l = line[0:len(line)-1]

        # check sizes of words, ignore if they differ
        if word_len == len(l):
            s = sorted(l)
            # compare strings
            if word_sorted == s:
                result_list.append(l)

    searchfile.close()


form = cgi.FieldStorage() # instantiate only once!
str1 = form.getfirst('one', 'empty')

# Avoid script injection escaping the user input
s1 = cgi.escape(str1)

res_list = []
get_anagram(s1, res_list)

response = "{anagrams:["
for r in res_list:
    response = response + r + ","

response = response[0:len(response)-1]
response = response + "]}"

print "Content-Type: text/html\n"
print '<html><body>'
print '<p>The first submitted string was ', s1, '</p>'
print '<p>anagrams: ', response, '</p>'
print '</body></html>'
