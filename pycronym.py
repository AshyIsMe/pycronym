#!/usr/bin/env python3
import random
import sys
import itertools

w=[{k:list(v) for k,v in itertools.groupby(open(f),lambda l:l[0])} for f in['nouns.txt','propernouns.txt','verbs.txt']]
print('\n'.join(a.upper()+' => '+' '.join((random.choice(w[i%3][c]).strip() for i,c in enumerate(a.upper()))) for a in sys.argv[1:]))

