#!python

import os
import argparse
from pathlib import Path

from garmin_fit_export.garmin_fit_export import GarminFitExport

import logging
logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser()
parser.add_argument('-s',
                    '--source',
                    required=True,
                    help='file or directory source')
parser.add_argument('-d',
                    '--destination',
                    required=True,
                    help='directory destination')
parser.add_argument('--debug',
                    action='store_true',
                    help='Export debug raw file')
args = parser.parse_args()

input = os.path.realpath(args.source)
output_dir = os.path.realpath(args.destination)
output = output_dir
if (not os.path.isdir(output)):
    logging.error("{} : Destination doesn't exist or isn't a directory"
                  .format(output))
    exit()

logging.info("Source: {}".format(input))
logging.info("Destination: {}".format(output))

if (os.path.isfile(input)):
    filename = str(input)
    act = GarminFitExport(filename)
    file_type = act.file_id.get('type')
    if (args.debug):
        act.debug_tree(output)
    else:
        if (file_type in ('activity', 'location', 'course')):
            if (file_type in ('activity', 'course')):
                Y = act.file_id.get('time_created').strftime('%Y')
                m = act.file_id.get('time_created').strftime('%m')
                output = os.path.join(output_dir, file_type + "_gpx", Y, m)
                if (not os.path.exists(output)):
                    os.makedirs(output)
            act.get_gpx(output)
        elif (file_type in ('workout', 'record')):
            output = os.path.join(output_dir, file_type + "_md")
            if (not os.path.exists(output)):
                os.makedirs(output)
            act.get_md(output)
        else:
            logging.warning("File type: {} not recognized for export"
                            .format(file_type))
elif (os.path.isdir(input)):
    for filename in Path(input).rglob('*.fit'):
        filename = str(filename)
        act = GarminFitExport(filename)
        file_type = act.file_id.get('type')
        if (args.debug):
            act.debug_tree(output)
        else:
            if (file_type in ('activity', 'location', 'course')):
                logging.info("process: {}".format(filename))
                if (file_type in ('activity', 'course')):
                    Y = act.file_id.get('time_created').strftime('%Y')
                    m = act.file_id.get('time_created').strftime('%m')
                    output = os.path.join(output_dir, file_type + "_gpx", Y, m)
                    if (not os.path.exists(output)):
                        os.makedirs(output)
                act.get_gpx(output)
            elif (file_type in ('workout', 'record')):
                output = os.path.join(output_dir, file_type + "_md")
                if (not os.path.exists(output)):
                    os.makedirs(output)
                act.get_md(output)
            else:
                logging.warning("File type: {} not recognized for export"
                                .format(file_type))
