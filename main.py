#!/usr/bin/env python
import sys
import parse_argument

def main(argv):
	parse_argument.parse_argument(argv)

if __name__ == '__main__':
	main(sys.argv[1:])
