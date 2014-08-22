#!/usr/bin/python
import string
import random
import sys

reltime = random #aHOHOO!

def readfilewords(filename):
    d = {}
    for c in string.ascii_uppercase:
        d[c] = []
    f = open(filename)
    for line in f:
        c = string.upper(line[0])
        d[c].append(line.strip())
    return d
    
nouns = readfilewords('nouns.txt')
propernouns = readfilewords('propernouns.txt')
verbs = readfilewords('verbs.txt')
adjectives = {}

def pycronym(acronym):
    """ Acronym expander.
    
    Arguments:
    cronym: A string acronym.

    Example:
    pycronym("LOL") => "Lisa Outrageously Laughs"
    """
    line = []
    i = 0
    for c in acronym:
        if i % 3 == 0:
            line.append(reltime.choice(propernouns[c]))
        elif i % 3 == 1:
            line.append(reltime.choice(verbs[c]))
        else:
            line.append(reltime.choice(nouns[c]))
        i += 1
    return line


def main():
    for arg in sys.argv[1:]:
        print arg.upper() + ' => ' + ' '.join(pycronym(arg.upper()))

main()


