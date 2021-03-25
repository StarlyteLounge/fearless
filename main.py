#! /bin/env python3

from flask import Flask
ppc = Flask(__name__)


@ppc.route('/')
def lander():
    return "nothing to see here. Try /item"


@ppc.route('/item')
def item():
    return "this is the item page"


if __name__ == '__main__':
    ppc.run()
