#!/usr/bin/env python

# Break up xml into RECORDS, parse the records one at a time and write into
# a json file (tpl.json) file, one line per record


from contextlib import contextmanager
from xml.etree import cElementTree
import json


@contextmanager
def return_records(fname):
    """
    A context manager that returs a generator producing strings extracted from
    xml file that begin with <RECORD> and end with </RECORD>

    Parameters
    ----------
    fname:  str
            A filename, the source xml file.
    """
    def out_gen():
        with open(fname, 'r') as tpl_xml:
            lines = []
            in_record = False
            for line in tpl_xml:
                line = line.strip()
                if in_record and '</RECORD>' in line:
                    # detect the end of the record
                    lines.append(line)
                    in_record = False
                    out_str = "".join(lines)
                    lines = []
                    yield out_str
                elif in_record:
                    # reading record lines
                    lines.append(line)
                else:
                    # detect the begging of the record
                    if '<RECORD>' in line:
                        in_record = True
                        lines.append(line)
    yield out_gen()


class record(dict):
    """
    Dictionary that turns values into lists when a value of a particular key is
    inserted more than one time. This code also has basic checks to prevent
    duplicates
    """
    def __setitem__(self, key, value):
        if key in self:
            if isinstance(self[key], list):
                if value not in self[key]:  # naively preventing duplicates
                    self[key].append(value)
            else:
                ### Duplicate dimension IDs, verify that duplicates are omitted
                super().__setitem__(key, [self[key], value])
        else:
            super().__setitem__(key, value)


def try_get_attr(item, attr_name):
    """
    Given an element tree and attributes you're looking for extract the
    attributes without crashing

    Parameters
    ----------
    item:       xml.etree.cElementTree.Element
    attr_name:  str
    """
    attr = None
    if hasattr(item, attr_name):
        attr = getattr(item, attr_name)
    return attr


def cast_vals_to_ints(in_dict):
    """
    Given a dictinary with dimension descriptions,  modify it, converting
    values to integers

    Parameters
    ----------
    in_dict:    dict
                Dictionary with values that can be converted to string
    """
    for k in in_dict.keys():
        in_dict[k] = int(in_dict[k])
    return in_dict


def parse_record(etree):
    """
    Given a record tree, parse it and return a dictionary

    Parameters
    ----------
    etree:  xml.etree.cElementTree.Element
            An element tree with the root <RECORD> and children describing said
            record.
    """
    out_record = record()
    for child in etree.getchildren():
        text = "".join([
            try_get_attr(grandchild, 'text')
            for grandchild in child.getchildren()
        ])
        attr = try_get_attr(child, 'attrib')
        if 'NAME' in attr:
            out_record[attr['NAME']] = text
        elif 'DIMENSION_ID' in attr and 'ID' in attr:
            out_record['dimensions'] = cast_vals_to_ints(attr)
        else:
            ## catch-all case, something is weird going on with the data
            import ipdb; ipdb.set_trace()

    return out_record


if __name__ == '__main__':
    with return_records('tpl.xml') as records:
        with open('tpl.json', 'wb') as json_file:
            for record_str in records:
                out_dict = parse_record(cElementTree.fromstring(record_str))
                out_str = "%s\n" % json.dumps(out_dict)
                json_file.write(bytes(out_str, "utf-8"))
