#!python
"""
GarminFitExport: Garmin FIT file export and debug manager

:Author: Roberto Quintiliani
:Copyright: Copyright (c) Roberto Quintiliani
:License: GPLv3 - see LICENSE

"""

from .garmin_fit_sdk_upgrade import gfs
from . import lib_fit_messages as lfm

import os
import shutil
from datetime import timedelta

import logging
logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')

__name__ = "GarminFitExport"
__version__ = "0.0.1"


class GarminFitExport():
    """
    Garmin FIT file export and debug manager.

    :param absolute_path: absolute path to file FIT.
    """
    def __init__(self, absolute_path: str):
        self.log = logging
        self.fit_type = "unknown"
        self.__pathfile = absolute_path

        self.__decoder(self.__pathfile)

        self.file_id = lfm.FileId(self._messages)
        # self.file_creator = lfm.FileCreator(self._messages)

        file_type = self.file_id.get('type')
        if (file_type == 'activity'):
            pass
            # file Activity
            # self.event = lfm.Event(self._messages)
            # self.device_info = lfm.DeviceInfo(self._messages)
            # self.device_settings = lfm.DeviceInfo(self._messages)
            # self.user_profile = lfm.UserProfile(self._messages)
            self.sport = lfm.Sport(self._messages)
            # self.training_settings = lfm.TrainingSettings(self._messages)
            # self.zones_target = lfm.ZonesTarget(self._messages)
            self.record = lfm.Record(self._messages)
            # self.gps_metadata = lfm.GpsMetadata(self._messages)
            self.lap = lfm.Lap(self._messages)
            # self.time_in_zone = lfm.TimeInZone(self._messages)
            # self.split = lfm.Split(self._messages)
            # self.split_summary = lfm.SplitSummary(self._messages)
            # self.session = lfm.Session(self._messages)
            # self.activity = lfm.Activity(self._messages)
        elif (file_type == 'location'):
            self.location = lfm.Location(self._messages)
        # elif (file_type == 'record'):
        #     pass
        elif (file_type == 'course'):
            self.course = lfm.Course(self._messages)
            self.record = lfm.Record(self._messages)
        elif (file_type == 'workout'):
            self.workout = lfm.Workout(self._messages)
            self.workout_step = lfm.WorkoutStep(self._messages)
        elif (file_type == 'record'):
            self.record = lfm.Record2(self._messages)

        self.__parse()

    def __decoder(self, path_file_fit: str):
        """
        Decoder file FIT

        :param absolute_path: absolute path to file FIT.
        """
        stream = gfs.Stream.from_file(path_file_fit)
        decoder = gfs.Decoder(stream)
        self._messages, self._errors = decoder.read()

    def __parse(self):
        """
        Parse file FIT
        """
        for mesg in self._messages.keys():
            if (isinstance(self._messages[mesg], list)):
                l0_idx = 0
                for l0 in self._messages[mesg]:
                    if (isinstance(l0, dict)):
                        for key, value in l0.items():
                            if ("_lat" in str(key) or "_long" in str(key)):
                                self._messages[mesg][l0_idx][key] = value / (2**32 / 360.0)
                    l0_idx += 1

    def record2str(self, record: float, unit: str = 's') -> str:
        """
        Converts the record number to a human-readable string.

        :param record: record value.
        :param unit: unit of measurement.

        :return human-readable string.
        """
        if (unit == 'ms'):
            return str(timedelta(seconds=int(record / 1000.0)))
        elif (unit == 'ms'):
            return str(timedelta(seconds=record))
        elif (unit == 'cm'):
            if (record > 100000):
                return "{} km".format(int(record / 100) / 1000)
            else:
                return "{} m".format(int(record / 100))
        elif (unit == 'm'):
            return "{} m".format(record)

    def get_list(self) -> list:
        """
        Get list of keys in messages

        :return list of keys
        """
        return self._messages.keys()

    def __debug_tree(self, archive: dict | list, fp, level: str = '') -> None:
        """
        Debug tree constructor from fit file contents.

        :param  archive: content of file fit.
        :param fp: object file.
        :param level: level of indentation.
        """
        if (isinstance(archive, dict)):
            for key, value in archive.items():
                fp.write("\n{}'{}': ".format(level, key))
                self.__debug_tree(value, fp, level + '\t')
        elif (isinstance(archive, list)):
            fp.write("(List) ")
            for value in archive:
                if (isinstance(value, dict) or isinstance(value, list)):
                    self.__debug_tree(value, fp, level + '\t')
                else:
                    fp.write("\n{}{}".format(level, value))
        else:
            fp.write("{}".format(archive))

    def debug_tree(self, output_dir: str) -> None:
        """
        Debug tree constructor from fit file contents.

        :param output_dir: absolute path to the directory output.
        """
        filename_debug = os.path.join(output_dir, str(self.file_id.get('type')),
                                      os.path.basename(self.__pathfile) + "_bak.txt")
        self.log.info("Write: " + filename_debug)
        dir = os.path.join(output_dir, str(self.file_id.get('type')))
        if (not os.path.exists(dir)):
            os.mkdir(dir)
        fp = open(filename_debug, 'w')
        self.__debug_tree(self._messages, fp)
        fp.close()

    def get_filefit(self) -> str:
        """
        Get path of current file Fit.

        :return: path file.
        """
        return self.__pathfile

    def get_description(self) -> str:
        """
        Description constructor.

        :return: simple file description, equivalent to the base name of the output file.
        """
        description = ''
        file_type = self.file_id.get('type')
        if (file_type == "activity"):
            description = self.file_id.get('time_created').isoformat().replace(':', '_').replace('+00_00', 'Z') + "_" + self.sport.get('sport')
        elif (file_type == "location"):
            description = "Location"
        elif (file_type == "course"):
            if (isinstance(self.course.get('name'), list)):
                name = self.course.get('name')[0]
            else:
                name = self.course.get('name')
            description = self.file_id.get('time_created').isoformat().replace(':', '_').replace('+00_00', 'Z') + "_" + name
        elif (file_type == "workout"):
            if (isinstance(self.workout.get('wkt_name'), list)):
                name = self.workout.get('wkt_name')[0]
            else:
                name = self.workout.get('wkt_name')
            if (name is not None):
                description = self.file_id.get('time_created').isoformat().replace(':', '_').replace('+00_00', 'Z') + "_" + name
            else:
                description = self.file_id.get('time_created').isoformat().replace(':', '_').replace('+00_00', 'Z') + "_None"
        elif (file_type == "record"):
            description = self.file_id.get('garmin_product')
        return description

    def get_gpx(self, output_dir: str, overwrite: bool = False, copy_fit: bool = False) -> None:
        """
        Gpx file constructor.

        :param output_dir: absolute path to the directory output.
        :param overwrite: permission to overwrite gpx output file.
        :param copy_fit: copy source file fit in directory output.
        """
        output_gpx = os.path.join(output_dir, self.get_description() + ".gpx")
        output_fit = os.path.join(output_dir, self.get_description() + ".fit")

        if (copy_fit and not os.path.exists(output_fit)):
            shutil.copyfile(self.__pathfile, output_fit)
            self.log.info("Copy: {} --> {}".format(self.__pathfile, output_fit))

        if (overwrite or not os.path.exists(output_gpx)):
            self.log.info("Write: " + output_gpx)
            file_type = self.file_id.get('type')

            fgpx = open(output_gpx, 'w')
            fgpx.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            fgpx.write("<gpx version=\"1.1\" creator=\"{} {}\" xmlns=\"http://www.topografix.com/GPX/1/1\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:gpxtpx=\"http://garmin.com\" xmlns:gpxx=\"http://www.garmin.com/xmlschemas/GpxExtensions/v3\" xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd\">\n".format(__name__, __version__))

            if (file_type == 'activity'):
                if (len(self.lap.mesgs) > 1):
                    lap = 1
                    for elem in self.lap.mesgs:
                        lat = str(elem["end_position_lat"])
                        long = str(elem["end_position_long"])
                        name = "Lap " + str(lap)
                        fgpx.write("\t<wpt lat=\"{}\" lon=\"{}\">\n\t\t<name>{}</name>\n\t</wpt>\n".format(lat, long, name))
                        lap += 1
                fgpx.write("\t<trk>\n")
                fgpx.write("\t\t<trkseg>\n")
                lap = 1
                for elem in self.record.mesgs:
                    if ("position_lat" in elem.keys() and "position_long" in elem.keys()):
                        time = elem["timestamp"].isoformat().replace('+00:00', 'Z')
                        lat = str(elem["position_lat"])
                        long = str(elem["position_long"])
                        extensions = ''
                        for other_k, other_v in elem.items():
                            if (other_k in ('heart_rate', 'temperature', 'cadence', 'distance', 'power')):
                                if (other_k == 'heart_rate'):
                                    other_k = 'gpxtpx:hr'
                                elif (other_k == 'distance'):
                                    other_k = 'gpxtpx:depth'
                                elif (other_k == 'temperature'):
                                    other_k = 'gpxtpx:atemp'
                                elif (other_k == 'cadence'):
                                    other_k = 'gpxtpx:cad'
                                elif (other_k == 'power'):
                                    other_k = 'gpxtpx:power'
                                extensions += "\t\t\t\t\t\t<{}>{}</{}>\n".format(other_k, other_v, other_k)
                        if (extensions != ''):
                            extensions = "\t\t\t\t<extensions>\n\t\t\t\t\t<gpxtpx:TrackPointExtension>\n{}\t\t\t\t\t</gpxtpx:TrackPointExtension>\n\t\t\t\t</extensions>\n".format(extensions)
                        if ("enhanced_altitude" in elem.keys()):
                            elev = str(elem["enhanced_altitude"])
                            fgpx.write("\t\t\t<trkpt lat=\"{}\" lon=\"{}\">\n\t\t\t\t<ele>{}</ele>\n\t\t\t\t<time>{}</time>\n{}\t\t\t</trkpt>\n".format(lat, long, elev, time, extensions))
                        else:
                            fgpx.write("\t\t\t<trkpt lat=\"{}\" lon=\"{}\">\n\t\t\t\t<time>{}</time>\n{}\t\t\t</trkpt>\n".format(lat, long, time, extensions))
                        if (len(self.lap.mesgs) > lap):
                            if (self.lap.mesgs[lap]['start_time'] < elem["timestamp"]):
                                fgpx.write("\t\t</trkseg>\n")
                                fgpx.write("\t\t<trkseg>\n")
                                lap += 1
                fgpx.write("\t\t</trkseg>\n")
                fgpx.write("\t</trk>\n")
            elif (file_type == "course"):
                fgpx.write("\t<rte>\n")
                for elem in self.record.mesgs:
                    if ("position_lat" in elem.keys() and "position_long" in elem.keys()):
                        time = elem["timestamp"].isoformat().replace('+00:00', 'Z')
                        lat = str(elem["position_lat"])
                        long = str(elem["position_long"])
                        if ("enhanced_altitude" in elem.keys()):
                            elev = str(elem["enhanced_altitude"])
                            fgpx.write("\t\t\t<rtept lat=\"{}\" lon=\"{}\">\n\t\t\t\t<ele>{}</ele>\n\t\t\t\t<time>{}</time>\n\t\t\t</rtept>\n".format(lat, long, elev, time))
                        else:
                            fgpx.write("\t\t\t<rtept lat=\"{}\" lon=\"{}\">\n\t\t\t\t<time>{}</time>\n\t\t\t</rtept>\n".format(lat, long, time))
                fgpx.write("\t</rte>\n")
            elif (file_type == "location"):
                for elem in self.location.mesgs:
                    lat = str(elem["position_lat"])
                    long = str(elem["position_long"])
                    name = str(elem["label"])
                    fgpx.write("\t<wpt lat=\"{}\" lon=\"{}\">\n\t\t<name>{}</name>\n\t</wpt>\n".format(lat, long, name))

            fgpx.write("</gpx>")
            fgpx.close()
        else:
            self.log.warning("Overwrite denied: {}".format(output_gpx))

    def get_md(self, output_dir: str, overwrite: bool = False) -> None:
        """
        Markdown file constructor.

        :param  output_dir: absolute path to the directory output.
        :param overwrite: permission to overwrite markdown output file.
        """
        output_md = os.path.join(output_dir, self.get_description() + ".md")

        if (overwrite or not os.path.exists(output_md)):
            self.log.info("Write: " + output_md)
            file_type = self.file_id.get('type')

            fmd = open(output_md, 'w')
            if (file_type == 'workout'):
                fmd.write("# {}\n\n".format(self.get_description()))
                fmd.write("|Item|Intensity|Exercise|Duration|\n")
                fmd.write("|---|---|---|---|\n")
                for elem in self.workout_step.mesgs:
                    # print(elem)
                    if ('duration_type' in elem.keys()):
                        if ('intensity' in elem.keys()):
                            if ('exercise_category' in elem.keys()):
                                if (elem['duration_type'] == 'time'):
                                    fmd.write("|{}|**{}**|*{}*|{}|\n".format(elem['message_index'] + 1, elem['intensity'].capitalize(), elem['exercise_category'].capitalize(), self.record2str(elem['duration_value'], 'ms')))
                                else:
                                    fmd.write("|{}|**{}**|*{}*|{}|\n".format(elem['message_index'] + 1, elem['intensity'].capitalize(), elem['exercise_category'].capitalize(), elem['duration_value']))
                            else:
                                if (elem['duration_type'] == 'time'):
                                    fmd.write("|{}|**{}**| - |{}|\n".format(elem['message_index'] + 1, elem['intensity'].capitalize(), self.record2str(elem['duration_value'], 'ms')))
                                elif (elem['duration_type'] == 'open'):
                                    fmd.write("|{}|**{}**| - |{}|\n".format(elem['message_index'] + 1, elem['intensity'].capitalize(), elem['duration_type']))
                                else:
                                    fmd.write("|{}|**{}**| - |{}|\n".format(elem['message_index'] + 1, elem['intensity'].capitalize(), self.record2str(elem['duration_value'], 'cm')))
                        elif ('repeat_steps' in elem.keys()):
                            fmd.write("|{}| **Repeat** | - |x{}|\n".format(elem['message_index'] + 1, elem['repeat_steps']))
                    else:
                        fmd.write("|{}| - | - | - |\n".format(elem['message_index'] + 1))
            elif (file_type == 'record'):
                fmd.write("# Device: {}\n\n".format(self.get_description().capitalize().replace('_', ' ')))
                fmd.write("|Sport|Target|UTC|Record|\n")
                fmd.write("|---|---|---|---|\n")
                for r in self.record.mesgs:
                    if ('record' in r.keys()):
                        fmd.write("|**{}**|".format(r['sport'].capitalize()))
                        if ('target' in r.keys()):
                            fmd.write("${} m$|".format(r['target']))
                        elif ('record_description' in r.keys()):
                            fmd.write("{}|".format(r['record_description']))
                        fmd.write("{}|{}|\n".format(r['timestamp'].isoformat(), self.record2str(r['record'], r['record_units'])))
                    else:
                        logging.warning("{} {} haven't record".format(r['timestamp'].isoformat(), r['sport']))
            fmd.close()
        else:
            self.log.warning("Overwrite denied: {}".format(output_md))
