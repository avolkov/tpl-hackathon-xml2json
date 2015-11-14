Old code
====
This director contains all failed attempts and dead-end guesses on about the structure, and size of `tpl.xml` as well as machine resources.

`dump_json.py` -- This code assumes that cElementTree.iterparse properly parse chil nodes as well as parent root node. It doesnt.

`examine_tags.py` -- this code looks for all possible tags. In the context of the problem that information didn't actually give me anything.
On a Intel i5-2410M \w SSD, this process took about 30 minutes

`load_root_etree.py` -- a very naive implementation that attempted to just load whole 20GB xml file into the memory using cElementTree which is significantly more efficient than ElementTree

`read_xml.py` -- an original attempt of loading whole xml file into the memory.

`collect_events.py` -- an attempt to collect events, data which turned out to be irrelevant, events in the context of xml.etree are used when editing or creating xml files, not reading.