#This script can be used for running from Jenkinsfile
import sys,os,argparse
from robot import run_cli, rebot_cli

print ("before")
parser = argparse.ArgumentParser()
parser.add_argument("--config_file", default="")
parser.add_argument("--include", nargs='?', default="")
parser.add_argument("--exclude", nargs='?', default="")
parser.add_argument("--testcases", nargs='?' ,default="")
parser.add_argument("--testcase_location", default="")

args = parser.parse_args()

option_list = []
if args.config_file:
    option_list.extend(['--variable','config_file:'+args.config_file])
if args.include:
    option_list.extend(['-i',args.include])
if args.exclude:
    option_list.extend(['-e',args.exclude])
if args.testcases:
    for test_case in args.testcases.split(","):
        option_list.append(args.testcase_location)

print ("inside new robot cli")
print (option_list)

run_cli(option_list,exit=False)

