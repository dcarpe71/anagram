#!/usr/bin/python
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from collections import defaultdict
from itertools import permutations
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
api = Api(app)

class List_dict(Resource):
    def get(self):
        with open("/home/dcv/words","r+") as f:
            data = f.read()
	f.seek(0)

	return data

class Anagram_search(Resource):
	def get(self, source_word):
		from itertools import permutations
		import enchant
		d = enchant.Dict('en_US')
		return [''.join(p) for p in permutations(source_word, len(source_word)) if d.check(''.join(p))== True]
       
api.add_resource(Anagram_search, '/anagram/<string:source_word>')
api.add_resource(List_dict, '/dictionary')

if __name__ == '__main__':
    ###app.run(debug=True)
    app.run(host='0.0.0.0')
