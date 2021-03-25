#! /bin/env python3

from flask import Flask
from flask import request


ppc = Flask(__name__)  # one server serves them all

items = {'1': 'one', '4': 'four'}  # populated via API


@ppc.route('/')
def landing():
    return "nothing to see here. Try /item"


@ppc.route('/item', methods=['GET'])
def item():
    if request.args:
        return str(request.args.getlist('id'))
    else:
        return items


if __name__ == '__main__':
    ppc.run()
