#!/usr/bin/env python


from contextlib import contextmanager


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

if __name__ == '__main__':
    with return_records('tpl.xml') as records:
        for record in records:
            print(len(record))
