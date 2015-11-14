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


def try_get_attr(item, attr_name):
    attr = None
    if hasattr(item, attr_name):
        attr = getattr(item, attr_name)
    return attr


def parse_record(etree, r_str):
    out_record = {}
    for child in etree.getchildren():
        for grandchild in child.getchildren():
            text = try_get_attr(grandchild, 'text')
        attr = try_get_attr(child, 'attrib')
        print(attr)
        print(text)
        import ipdb; ipdb.set_trace()
    return out_record


if __name__ == '__main__':
    out_list = []
    with return_records('tpl.xml') as records:
        for record in records:
            print(len(record))
            parse_record(
                cElementTree.fromstring(record),
                record.replace('\n', '')
            )
