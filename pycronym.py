#!/usr/bin/python
import string
import random

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
    
nouns = {}
propernouns = readfilewords('propernouns.txt')
verbs = {}
adjectives = {}

def pycronym(acronym):
    """ Acronym expander.
    
    Arguments:
    cronym: A string acronym.

    Example:
    pycronym("LOL") => "Lisa Outrageously Laughs"
    """
    line = []
    for c in acronym:
        line.append(reltime.choice(propernouns[c]))
    return line


def main():
    print 'LOL => ' + ' '.join(pycronym("LOL"))

main()


