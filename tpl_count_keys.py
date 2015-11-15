#!/usr/bin/env python

### Count all keys

import json
from collections import Counter

if __name__ == '__main__':
    key_count = Counter()
    key_count.update('total_count')
    with open('tpl.json', 'r') as tpl_fd:
        for line in tpl_fd:
            key_count.update(json.loads(line).keys())
            key_count['total_count'] += 1
    open('key_stats.json', 'wb').write(bytes(json.dumps(key_count), 'utf-8'))
