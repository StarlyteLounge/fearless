#! /bin/env python3

from flask import Flask
from flask import request

ppc = Flask(__name__)

items = {}  # populated via API


@ppc.route('/')
def landing():
    """A not-very-helpful landing page"""
    return "nothing to see here. Try /item"


@ppc.route('/item', methods=['GET', 'POST', 'DELETE'])
def item():
    """Respond to the item REST/HTTP requests"""
    if request.method == 'GET':
        return get_method()
    elif request.method == 'POST':
        items[request.form['id']] = request.form['val']
        return '200'
    elif request.method == 'DELETE':  # NOTE that DELETE is an HTTP construct, and not supported by html
        items.pop(request.form['idx'])
        return '200'


def get_method():
    """Get all of the indicated items, or all of the items if there are no indicated items"""
    if request.args:
        return {i: items.get(i) for i in request.args.getlist('id')}
    else:
        return items


if __name__ == '__main__':
    ppc.run()
