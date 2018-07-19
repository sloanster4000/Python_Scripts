#!/usr/bin/env python
#Copyright (c) 2018 Ephraim Sloan
#Licensed under the terms of LICENSE included in this project

import sys
from lxml import etree

###INPUT###
SOURCE = sys.argv[1]
DEST = sys.argv[2]

# def limit_memory(maxsize):
    # soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    # resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
	
def parse(SOURCE, DEST): 
       try:
           parser = etree.XMLParser(remove_blank_text=True, huge_tree=True)
           tree = etree.parse(SOURCE, parser)
           tree.write(DEST, pretty_print=True)
       except Exception:
           print(parser.error_log)
       except Exception:
           traceback.print_exc(file=sys.stdout)
       sys.exit(0)

if __name__ == "__main__":
   parse(SOURCE, DEST)
   
   # from __main__ import *
   # SOURCE
# DEST