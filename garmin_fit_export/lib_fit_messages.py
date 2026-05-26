#!python
"""
Class Collection of FitMessages.

:Author: Roberto Quintiliani
:Copyright: Copyright (c) Roberto Quintiliani
:License: to be defined

"""


class FitMessages():
    """
    Class FitMessages
    """
    def get(self, key: str) -> list:
        """
        Get block by key

        :param key: key descriptor
        :return: list
        """
        ll = []
        for elm in self.mesgs:
            if (key in elm.keys()):
                ll.append(elm[key])
        if (len(ll) == 1):
            ll = ll[0]
        elif (len(ll) == 0):
            ll = None
        return ll

    def key_list(self) -> list:
        """
        Get list of keys

        :return: list
        """
        list = []
        for elm in self.mesgs:
            for k in elm.keys():
                if (k not in list):
                    list.append(k)
        if (len(list) == 1):
            list = str(list[0])
        elif (len(list) == 0):
            list = None
        return list


class FileId(FitMessages):
    """
    Class definition of file_id_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['file_id_mesgs']


class FileCreator(FitMessages):
    """
    Class definition of file_creator_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['file_creator_mesgs']


class Event(FitMessages):
    """
    Class definition of event_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['event_mesgs']


class DeviceInfo(FitMessages):
    """
    Class definition of device_info_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['device_info_mesgs']


class DeviceSettings(FitMessages):
    """
    Class definition of device_settings_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['device_settings_mesgs']


class UserProfile(FitMessages):
    """
    Class definition of user_profile_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['user_profile_mesgs']


class Sport(FitMessages):
    """
    Class definition of sport_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['sport_mesgs']


class TrainingSettings(FitMessages):
    """
    Class definition of training_settings_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['training_settings_mesgs']


class ZonesTarget(FitMessages):
    """
    Class definition of zones_target_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['zones_target_mesgs']


class Record(FitMessages):
    """
    Class definition of record_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['record_mesgs']


class Record2(FitMessages):
    """
    Class definition of record2_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['record2_mesgs']


class GpsMetadata(FitMessages):
    """
    Class definition of gps_metadata_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['gps_metadata_mesgs']


class Lap(FitMessages):
    """
    Class definition of lap_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['lap_mesgs']


class TimeInZone(FitMessages):
    """
    Class definition of time_in_zone_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['time_in_zone_mesgs']


class Split(FitMessages):
    """
    Class definition of split_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['split_mesgs']


class SplitSummary(FitMessages):
    """
    Class definition of split_summary_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['split_summary_mesgs']


class Session(FitMessages):
    """
    Class definition of session_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['session_mesgs']


class Activity(FitMessages):
    """
    Class definition of activity_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['activity_mesgs']


class Location(FitMessages):
    """
    Class definition of location_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['location_mesgs']


class Course(FitMessages):
    """
    Class definition of course_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['course_mesgs']


class Workout(FitMessages):
    """
    Class definition of workout_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['workout_mesgs']


class WorkoutStep(FitMessages):
    """
    Class definition of workout_step_mesgs

    :param mesgs: dict
    """
    def __init__(self, mesgs):
        self.mesgs = mesgs['workout_step_mesgs']
