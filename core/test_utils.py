from typing import List
import urllib

from rest_framework.reverse import reverse

def build_url_with_query_params(reverse_string, query_params, reverse_kwargs={}):
    query = urllib.parse.urlencode(query_params)
    url = "{}?{}".format(reverse(reverse_string, kwargs=reverse_kwargs), query)

    return url