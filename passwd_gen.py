#!/usr/bin/python3

import sys, crypt

if len(sys.argv) == 1 : sys.exit("You must input password! \n --> Usage: passwd_gen.py <passwd> <--")

print(crypt.crypt(sys.argv[1], crypt.mksalt(crypt.METHOD_SHA512)))
