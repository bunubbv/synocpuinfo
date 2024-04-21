#!/usr/bin/python3
from pathlib import Path
import argparse

WORK_DIR = ''
BKUP_DIR = ''

def modify() -> None:
  if is_silent:
    print("silent")
  else:
    print("normal")

def restore() -> None:
  if is_silent:
    print("silent restore")
  else:
    print("normal restore")

parser = argparse.ArgumentParser(
  description='Modify CPU info in the DSM 7.X control panel.',
  epilog='https://github.com/bunubbv/synocpuinfo'
)

option = parser.add_argument_group().add_mutually_exclusive_group(required=False)

option.add_argument(
  '-m',
  '--modify',
  action='store_true',
  help='modify info'
)

option.add_argument(
  '-r',
  '--restore',
  action="store_true",
  help="restore from backup"
)

parser.add_argument(
  '-s',
  '--silent',
  action="store_true",
  help="silent mode"
)

args = parser.parse_args()
is_silent: bool = args.__dict__.get('silent', False)

if args.__dict__.get('modify', ''):
  modify()
elif args.__dict__.get('restore', ''):
  restore()
else:
  parser.print_help()