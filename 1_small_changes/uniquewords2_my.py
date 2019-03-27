#!/usr/bin/env python3

"""
cd /home/atollye/current/Sammerfield_exercises/uniquewords/

python3 uniquewords2_my.py data.txt
"""

import collections
import string
import sys


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 3:
                    words[word] += 1

for word in sorted(words, key=lambda x: words.get(x), reverse=True):
    print("'{0}' occurs {1} times".format(word, words[word]))
