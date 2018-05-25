#!/usr/bin/env python
import argparse
import sys

def parse_argument(argv):
	parser = argparse.ArgumentParser(add_help=True)
	parser.add_argument('--optional','-o', action='store_const', const='OPTIONAL')
	parser.add_argument('positional')
	parser.add_argument('--number-args','-n', nargs='*')
	parser.add_argument('--dest','-d', nargs='+', dest='DESTINATION')
	parser.add_argument('--require','-r', nargs='?', required=True )
	parser.add_argument('--default', default='DEFAULT', help='Default = DEFAULT')

	print parser.parse_args(argv)

if len(sys.argv) == 1:
	args = "positional -o -n abcd efg 123 -d target is here -r require ".split()
else:
	args = sys.argv[1:]

parse_argument(args)
