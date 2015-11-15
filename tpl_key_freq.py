#!/usr/bin/env python

import json
from pprint import pprint
from collections import OrderedDict

key_freq = json.loads(open('key_stats.json', 'r').read())

sorted_keys = sorted([x for x in key_freq.items()], key=lambda x: x[1])

most_freq = OrderedDict([x for x in reversed(sorted_keys[-11:])])
least_freq = OrderedDict(sorted_keys[:10])

print("10 most frequent keys:")
pprint(most_freq)
print()
print("10 least frequent:")
pprint(least_freq)
