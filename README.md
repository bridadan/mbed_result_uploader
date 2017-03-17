# mbed Result Uploader

These are collection of scripts that can be used to assit in uploading mbed build statistics to a mongo DB server.

## memap_to_mongo.py

This script takes the `<project_name>_map.json` file that is produced in an mbed OS project's build folder and turns it into a JavaScript file that can be read by mongo DB's command line tool.

```
$ python mbed_result_uploader/memap_to_mongo.py --help
usage: memap_to_mongo.py [-h] -b BUILD -n NAME -m MCU -t TOOLCHAIN
                         [-c COLLECTION] -o OUTFILE
                         infile

Translate output of memap into a mongoDB-friendly script

positional arguments:
  infile                Input file

optional arguments:
  -h, --help            show this help message and exit
  -b BUILD, --build BUILD
                        Build number
  -n NAME, --name NAME  Name
  -m MCU, --mcu MCU     MCU
  -t TOOLCHAIN, --toolchain TOOLCHAIN
                        Toolchain
  -c COLLECTION, --collection COLLECTION
                        mongoDB collection
  -o OUTFILE, --outfile OUTFILE
                        Output file
```

To use the script:

```python
$ python mbed_result_uploader/memap_to_mongo.py <project_name>/BUILD/<target>/<toolchain>/<project_name>_map.json -b <build number> -n <project_name -m <target> -t <toolchain> -o <project_name>/BUILD/<target>/<toolchain>/dbscript.js
```

The JavaScript file can then be used by the mongo command line tool like so:

```
$ mongo --host <mongo_db_host_address> <database name> <project_name>/BUILD/<target>/<toolchain>/dbscript.js
```