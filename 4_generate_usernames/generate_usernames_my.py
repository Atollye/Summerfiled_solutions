#!/usr/bin/env python3

"""
/home/atollye/Summerfiled_solutions/4_generate_usernames/generate_usernames_my.py /home/atollye/Summerfiled_solutions/4_generate_usernames/data/users2.txt
"""

import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("User",
            "username forename middlename surname id")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(),
                            user.id)] = user
    lst = convert_to_list(users)
    while lst:
        print_page(lst)

def print_page(lst):
    left_column = make_column(lst)
    right_column = make_column(lst)
    
    print_the_header()
    for k in range(64):
        line = left_column[k] + ' '*4 + right_column[k]
        if line:
        print(line)
    print("\f")

    

        
def make_column(lst):
    column = []
    for i in range(64):
        try:
            item = lst.pop(0)
            fullname = (str(item.surname)+", "+str(item.forename))[:16]
            line = "{0:.<16} ({1.id:<4}) {1.username:<9}".format(fullname, item)
            column.append(line)
        except IndexError:
            column.append(' '*33)
    return column
        


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username

def convert_to_list(users):
    lst = []
    for key in sorted(users):
        lst.append(users[key])
    return lst   


def print_the_header():
    namewidth = 17
    usernamewidth = 9    
    str1 = "{0:<{nw}} {1:^6} {2:{unw}}".format(
          "Name", "ID", "Username", nw=namewidth, unw=usernamewidth)
    str2 = "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth)
    print(str1, " ", str1)
    print(str2, " ", str2)
 
main()
