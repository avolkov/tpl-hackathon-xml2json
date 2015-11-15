#!/usr/bin/env python

### Count all keys whose values are string

import json
from collections import Counter

if __name__ == '__main__':
    key_count = Counter()
    key_count.update('total_count')
    with open('tpl.json', 'r') as tpl_fd:
        for line in tpl_fd:
            tpl_dict = json.loads(line)
            str_keys = [k for k, v in tpl_dict.items() if isinstance(v, str)]
            key_count.update(str_keys)
            key_count['total_count'] += 1
    open('key_stats.json', 'w').write(bytes(json.dumps(key_count), 'utf-8'))
