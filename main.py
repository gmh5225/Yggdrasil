#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer C. B. Herold
# Vers 0.1 28.10.2022

# Author
__author__ = "Rainer C. B. Herold"
__copyright__ = "Copyright 2022, Rainer C. B. Herold"
__credits__ = "Rainer C. B. Herold"
__license__ = "MIT license"
__version__ = "0.7c"
__maintainer__ = "Rainer C. B. Herold"
__status__ = "Production"

# Libraries
try:
    from argparse import ArgumentParser, FileType, RawTextHelpFormatter, SUPPRESS
    from os import getcwd, system
    from os.path import dirname, join, realpath
except ModuleNotFoundError as e: input(f"The module was not found\n\n{e}\n\nPlease confirm with the button 'Return'"), exit()

# main
if __name__ == '__main__':
    File_Path = dirname(realpath(__file__))
    Start_Script = join(File_Path, "install.sh")
    parser = ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter)
    optional = parser.add_argument_group('optional arguments')

    optional.add_argument('-p','--path', help='This parameter specifies the target path of your custom tools.\n')
    optional.add_argument('-s','--skip', type=bool, nargs='?', help='This parameter skips the hardening part.\n')
    optional.add_argument('-h','--help', action='help', default=SUPPRESS, help='Show this help message and exit.\n----------------------------------------->
    args = parser.parse_args()

    if (args.path != None and args.skip != None): system(f'sudo bash {Start_Script} -s args.path')
    elif (args.path != None and args.skip == None): system(f'sudo bash {Start_Script} args.path ')
    elif (args.path == None and args.skip != None): system(f'sudo bash {Start_Script} -s')
    else: system(f'sudo bash {Start_Script}')
