import argparse
import os
import sys
def write_file(file_path):
    with open("filename"+input_ext,"a") as f:
        f.write(file_path)
parser = argparse.ArgumentParser(description='the folder path and the exptension')

parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path of the folder')

parser.add_argument('Extc',
                       metavar='extc',
                       type=str,
                       help='extension to be found')
args = parser.parse_args()
input_path = args.Path
input_ext= args.Extc

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()
os.chdir(input_path)
for line in os.listdir(input_path):
    if line.endswith(input_ext):
         file_path = f"{input_path}\{line}"
         write_file(file_path)