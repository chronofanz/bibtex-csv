bibtex-csv
==========

Converts bibtex files to CSV.

Overview
--------

This program converts bibliography databases stored in the BibTeX / BibLaTeX format to the comma-separated value format.

Dependencies
------------

This script requires Python 3.x and Pandas.

Usage
-----

Input and output are text files.  Optionally, there's also a 'convert' method that users can leverage as part of their own data wrangling code.

Examples
--------

* Converting a single .bib file:

```sh
./convert.py bibliography.bib spreadsheet.csv
```
