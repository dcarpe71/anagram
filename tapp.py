#!/usr/bin/python
from flask import Flask, request
from flask_restful import Resource, Api
from collections import defaultdict
from itertools import permutations
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
api = Api(app)

def get_anagrams(word, result_list):
    
    # open the file
    searchfile = open("/home/dcv/words", "r")

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
                #print "found a match: " + l

    searchfile.close()

class List_dict(Resource):
    def get(self):
        with open("/home/dcv/words","r+") as f:
            data = f.read()
	f.seek(0)

	return data

class Anagram_search(Resource):
      def get(self, source_word):
        res_list = []
        get_anagrams(source_word, res_list)
	r = json.dumps(res_list)	
	print r
        return r
 
api.add_resource(Anagram_search, '/anagram/<string:source_word>')
api.add_resource(List_dict, '/dictionary')

if __name__ == '__main__':
    ###app.run(debug=True)
    app.run(host='0.0.0.0')
