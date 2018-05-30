import argparse

command_list = ['extract', 'ls']
def parse_argument(argv):
	parser = argparse.ArgumentParser(add_help=False)
	x = argv[0]
	if x in command_list:
		func_parser = eval("parse_{}_argument({})".format(x, argv[1:]))
		print func_parser
	
def parse_extract_argument(argv):
	print argv
	return "Extract"

def parse_ls_argument(argv):
	print argv
	return "ls"
