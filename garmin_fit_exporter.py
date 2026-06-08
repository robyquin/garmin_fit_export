#!python

import os
import argparse
from pathlib import Path

from garmin_fit_export.garmin_fit_export import GarminFitExport

import logging
logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')


def export_manager(filename: str, output_dir: str, debug: bool, overwrite: bool):
    """Export manager function

    :param filename: input filename
    :param output_dir: destination directory
    :param debug: create only debug file (raw)
    :param overwrite: permission to overwrite output file
    """
    act = GarminFitExport(filename)
    file_type = act.file_id.get('type')
    logging.info("process: {}".format(filename))
    if (debug):
        act.debug_tree(output_dir)
    else:
        if (file_type in ('activity', 'location', 'course')):
            if (file_type in ('activity', 'course')):
                Y = act.file_id.get('time_created').strftime('%Y')
                m = act.file_id.get('time_created').strftime('%m')
                output = os.path.join(output_dir, file_type + "_gpx", Y, m)
            else:
                output = os.path.join(output_dir, file_type + "_gpx")
            if (not os.path.exists(output)):
                os.makedirs(output)
            act.get_gpx(output, overwrite, copy_fit=True)
        elif (file_type in ('workout', 'record')):
            output = os.path.join(output_dir, file_type + "_md")
            if (not os.path.exists(output)):
                os.makedirs(output)
            act.get_md(output, overwrite)
        else:
            logging.warning("File type: {} not recognized for export"
                            .format(file_type))


parser = argparse.ArgumentParser()
parser.add_argument('-s',
                    '--source',
                    required=True,
                    help='file or directory source')
parser.add_argument('-d',
                    '--destination',
                    required=True,
                    help='directory destination')
parser.add_argument('--overwrite',
                    action='store_true',
                    help='Permission to overwrite output file')
parser.add_argument('--debug',
                    action='store_true',
                    help='Export debug raw file')
args = parser.parse_args()

input = os.path.realpath(args.source)
output_dir = os.path.realpath(args.destination)
if (not os.path.isdir(output_dir)):
    logging.error("{} : Destination doesn't exist or isn't a directory"
                  .format(output_dir))
    exit()

logging.info("Source: {}".format(input))
logging.info("Destination: {}".format(output_dir))

if (os.path.isfile(input)):
    filename = str(input)
    if (not output_dir.startswith(os.path.dirname(input)) and not os.path.dirname(input).startswith(output_dir)):
        export_manager(filename, output_dir, args.debug, args.overwrite)
    else:
        logging.error("For security reasons, the source directory and the destination directory cannot be nested.")
elif (os.path.isdir(input)):
    if (not output_dir.startswith(input) and not input.startswith(output_dir)):
        for filename in Path(input).rglob('*.fit'):
            export_manager(filename, output_dir, args.debug, args.overwrite)
    else:
        logging.error("For security reasons, the source directory and the destination directory cannot be nested.")
