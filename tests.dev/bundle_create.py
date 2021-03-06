#!/usr/bin/env python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
sys.path.insert(0, '..')
from clarify_python import clarify


def create_15_bundles(client):
    """Create 15 bundles without any media."""

    for i in range(0, 15):
        bundle_ref = client.create_bundle(str(i))
        href = bundle_ref['_links']['self']['href']
        bundle = client.get_bundle(href)
        print('*** Created bundle ' + href + ' with name: ' + bundle['name'])


def all_tests(apikey):
    """Set API key and call all test functions."""

    client = clarify.Client(apikey)

    print('===== create_15_bundles() =====')
    create_15_bundles(client)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: ' + sys.argv[0] + ' <apikey>')
        exit(1)

    all_tests(sys.argv[1])
