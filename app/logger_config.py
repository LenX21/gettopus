import pathlib
import os
from datetime import datetime
from app.config import EnvironmentData


class ReportingConfiguration:
    _report_name = None

    @staticmethod
    def ensure_log_folder(log_directory_path):
        if not os.path.isdir(log_directory_path):
            os.makedirs(log_directory_path)

    @classmethod
    def get_report_name(cls) -> str:
        if cls._report_name is None:
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d_%H%M")
            cls._report_name = '{}.log'.format(dt_string)
        return cls._report_name

    @staticmethod
    def get_log_directory_path():
        working_directory = pathlib.Path().absolute()
        return os.path.join(working_directory, EnvironmentData.REPORTING_FOLDER)

    @classmethod
    def get_log_path(cls):
        cls.ensure_log_folder(cls.get_log_directory_path())
        return os.path.join(cls.get_log_directory_path(), cls.get_report_name())
