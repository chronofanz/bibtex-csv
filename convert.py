#!/usr/bin/env python3

"""
This is a simple Python script that converts BibTeX entries to CSV.
"""

from re import match
from re import search

import pandas as pd

''' Parses input file handle or text object holding bibtex formatted string data into a pandas dataframe. '''        
def parse_bib(handle):
    entries = []
    entry = {}
    
    for line in handle:
        if (match('^@', line.strip())):
            if entry != {}:
                entries.append(entry)
                entry = {}
        elif (match('url', line.strip())):
            value, = findall('\{(\S+)\}', line)
            entry["url"] = value
        elif (search('=', line.strip())):
            key, value = [v.strip(" {},\n") for v in line.split("=", 1)]
            entry[key] = value

    keys = set()
    for entry in entries:
        for key in entry.keys():
            keys.add(key)
            
    df = pd.DataFrame(columns=sorted(keys))
    for entry in entries:
        df = df.append(entry, ignore_index=True)
                
    return df

def convert(input_file, output_file):
    with open(input_file, 'r', encoding="utf8") as handle:
        df = parse_bib(handle)
        df.to_csv(output_file, encoding='utf-8-sig')
    
if __name__ == "__main__":
   convert(sys.argv[1], sys.argv[2])
   