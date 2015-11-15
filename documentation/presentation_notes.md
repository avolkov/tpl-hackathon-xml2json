TPL Hackahton project Value-add
=============

The biggest problem with the dataset we were given -- everyone these days avoids working with XML, and whoever attempted to work the data, the dataset was too big requiring loading everything into memory, which is not feasible on current hardware or it requires the understanding about how XML is structured.

With the new, converted, JSON dataset you can read one record at a time, further processing things you want and skipping things you don't thus not running into RAM size limitation on your machines.

I wanted to work on a problem that was interesting for me and at the same time be able to accomplish something in limited time.

# Please use the data.

Read it one line at a time -- every line albeit a very long line is one record. You skip any lines you don't want, skip any data inside `dictionaries` that you don't want.

Use it with any program or editor that handles plain text.
No knowledge of structure of the documents is needed, you can just look for things you might want.

Performance makes it experimenting with data possible -- I went through the whole 11GB file in 5 1/2 Minutes on my laptop.


Converter source code: https://github.com/avolkov/tpl-hackathon-xml2json
Data file: http://data.flamy.ca/tpl.json.xz (786MB, compressed with LZMA)
My twitter: @a_volkov