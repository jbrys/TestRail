__author__ = 'jeffbrys'

import api
import argparse

#top level parser
parser = argparse.ArgumentParser(description='Interact with TestRail via the command line.')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

#parser for the "get" command
parser_get = subparsers.add_parser('get', help='perform GET requests on TestRail objects.')
get_case = parser_get.add_parser('case', help='retrieve a specific test case.')
get_case.add_argument('id#', type=int, help='retrieve a specific test case by id')