#!/usr/bin/env python

import json

key_freq = json.loads(open('key_stats.json', 'r').read())

sorted_keys = sorted([ x for x in key_freq.items()], key=lambda x: x[1])

most_freq = sorted_keys[-10:]
least_frew = sorted_keys[:10]

import ipdb; ipdb.set_trace()
