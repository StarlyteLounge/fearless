#! /bin/env python3

from flask import Flask
ppc = Flask(__name__)

@ppc.route('/')
def lander():
    return "nothing to see here. Try /item"


if __name__ == '__main__':
    ppc.run()
