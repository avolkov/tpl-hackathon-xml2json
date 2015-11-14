#!/usr/bin/env python

# GOAL -- convert XML into a set of json records that can be further
# converted into db records of some sort

from contextlib import contextmanager
from xml.etree import cElementTree


@contextmanager
def return_records(fname):
    def out_gen():
        with open(fname, 'r') as tpl_xml:
            lines = []
            in_record = False
            for line in tpl_xml:
                if in_record and '</RECORD>' in line:
                    lines.append(line)
                    in_record = False
                    out_str = "".join(lines)
                    lines = []
                    yield out_str
                elif in_record:
                    lines.append(line)
                else:
                    if '<RECORD>' in line:
                        in_record = True
                        lines.append(line)
    yield out_gen()


class record(dict):
    def __setitem__(self, key, value):
        if key in self:
            super().__setitem__(key, [self[key], value])
        else:
            super().__setitem__(key, value)


def try_get_attr(item, attr_name):
    attr = None
    if hasattr(item, attr_name):
        attr = getattr(item, attr_name)
    return attr


def parse_record(etree, r_str):
    out_record = record()
    for child in etree.getchildren():
        text = None
        grandchild = None
        for grandchild in child.getchildren():
            text = try_get_attr(grandchild, 'text')
        attr = try_get_attr(child, 'attrib')
        if 'NAME' in attr:
            out_record[attr['NAME']] = text
        elif 'DIMENSION_ID' in attr and 'ID' in attr:
            out_record['dimensions'] = attr
        else:
            ## catch-all case, something is weird going on with the data
            import ipdb; ipdb.set_trace()

    return out_record


if __name__ == '__main__':
    out_list = []
    with return_records('tpl.xml') as records:
        for record_str in records:
            print(len(record_str))
            parse_record(
                cElementTree.fromstring(record_str),
                record_str.replace('\n', '')
            )
