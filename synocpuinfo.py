#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(
  description='Modify CPU info in the DSM 7.X control panel.',
)

option = parser.add_argument_group().add_mutually_exclusive_group(required=False)

option.add_argument(
  '-m',
  '--modify',
  action='store_true',
  help='modify CPU info'
)

option.add_argument(
  '-s',
  '--silent',
  action="store_true",
  help="enable silent mode"
)

option.add_argument(
  '-r',
  '--restore',
  action="store_true",
  help="restore from backup"
)

args = parser.parse_args()

if args.__dict__.get('modify', ''):
  print("modify")
elif args.__dict__.get('silent', ''):
  print("silent")
elif args.__dict__.get('restore', ''):
  print("restore")