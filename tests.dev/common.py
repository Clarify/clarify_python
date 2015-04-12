#
#  Functions used by multiple tests.
#

import sys
sys.path.append('..')
from clarify_python import clarify


def bundle_list_map(client, func):
    """Execute func on every bundle."""
    has_next = True
    next_href = None  # if None, retrieves first page

    while has_next:
        # Get a page and perform the requested function.
        bundle_list = client.get_bundle_list(next_href)
        for i in bundle_list['_links']['items']:
            href = i['href']
            func(client, href)
        # Check for following page.
        next_href = None
        if 'next' in bundle_list['_links']:
            next_href = bundle_list['_links']['next']['href']
        if next_href is None:
            has_next = False
