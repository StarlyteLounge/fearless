#! /bin/env python3

from flask import Flask
from flask import request

ppc = Flask(__name__)
item = {'id': '', 'name': ''}  # TODO determine proper init values
items = []  # populated via API


@ppc.route('/')
def lander():
    return "nothing to see here. Try /item"


@ppc.route('/item')
def item():
    args = request.args
    if args:
        return f"hey! thanks for the args: {args}"
    else:
        return "hmm. no args."


if __name__ == '__main__':
    ppc.run()
