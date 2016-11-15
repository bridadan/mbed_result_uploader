"""Translate output of memap into a mongoDB-friendly script
"""

import os
import sys
import argparse
import json


def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-b', '--build', help="Build number", type=int, required=True)
    parser.add_argument('-n', '--name', help="Name", required=True)
    parser.add_argument('-m', '--mcu', help="MCU", required=True)
    parser.add_argument('-t', '--toolchain', help="Toolchain", required=True)
    parser.add_argument('-c', '--collection', help="mongoDB collection", default="builds")
    parser.add_argument('-o', '--outfile', help="Output file", type=argparse.FileType('w'), required=True)

    args = parser.parse_args(arguments)

    infile_contents = args.infile.read()
    infile_object = json.loads(infile_contents)
    args.infile.close()
    
    built_binary = {
        'name': args.name,
        'target': args.mcu,
        'toolchain': args.toolchain,
        'sizes': infile_object
    }    
    
    update_string = 'db.%s.update({"number": %d}, {$push: {"built_binaries": %s}})' % (args.collection, args.build, json.dumps(built_binary))
    args.outfile.write(update_string)
    args.outfile.close()    
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))