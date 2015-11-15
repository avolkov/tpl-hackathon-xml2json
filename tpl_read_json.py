#!/usr/bin/env python

import json

if __name__ == '__main__':

    with open('tpl.json', 'r') as tpl_fd:
        for line in tpl_fd:
            tpl_dict = json.loads(line)
            import pdb; pdb.set_trace()
