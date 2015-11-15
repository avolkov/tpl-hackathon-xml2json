tpl_hackathon
===========

The goal of this project is to convert all presented XML data into JSON making it more available to the developers.

The project is written in Python 3.4.3, no external libraries were user, however I just ipdb for debugging.

`tpl_xml2json.py` -- reads input `tpl.xml` and outputs `tpl.json`

Run time as measured on a 20GB segment, the program running on AMD FX-8329 CPU (3.2GHz)

`tpl_read_json.py` -- reads in `tpl.json` produced with `tpl_xml2json.py`  and stops at debug point waiting for the user input.

`tpl_count_str.keys` -- count how many times a key with a string value occurs. The application outpus key_stats.json