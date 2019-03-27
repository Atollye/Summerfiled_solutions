#!/usr/bin/env python3

import collections
import sys

"""
Тестирование
cd /home/atollye/current/programming_exercises/external_sites/

external_sites_my.py google_translator.html

Пример работы:
>>cd /home/atollye/current/programming_exercises/external_sites/
>>external_sites_my.py google_translator.html
external_sites_my.py: команда не найдена
>>python3 external_sites_my.py google_translator.html
translate.google.ru is referred to in:
    google_translator.html
www.broofa.com is referred to in:
    google_translator.html
www.google.com is referred to in:
    google_translator.html
www.google.ru is referred to in:
    google_translator.html

Отсутствие насройка соответствия расширения py и python3 в системе
>>external_sites_my.py google_translator.html
external_sites_my.py: команда не найдена


"""


sites = collections.defaultdict(set)

for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            i = 0
            while True:
                site = None
                i = line.find("http://", i)
                if i > -1:
                    i += len("http://")
                    for j in range(i, len(line)):
                        if not (line[j].isalnum() or line[j] in ".-"):
                            site = line[i:j].lower()
                            break
                    if site and "." in site:
                        sites[site].add(filename)
                    i = j
                else:
                    break

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        print("    {0}".format(filename))

