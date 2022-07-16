import logging

import pandas

from metrics_generator.base_metric_generator import BaseMetricGenerator


class TotalCarsMetricGenerator(BaseMetricGenerator):
    _logger = logging.getLogger(__name__)

    @classmethod
    def enabled(cls) -> bool:
        return True

    @staticmethod
    def order_number() -> int:
        return 1

    @staticmethod
    def meets_condition(data_frame: pandas.DataFrame) -> bool:
        column_name = 'Count'
        column_type = 'int64'

        if column_name in data_frame and data_frame.dtypes[column_name] == column_type:
            return True
        else:
            TotalCarsMetricGenerator._logger.error('Failed TotalCarsMetricGenerator.meets_condition')
            return False

    @staticmethod
    def generate_metric(data_frame: pandas.DataFrame):
        return data_frame['Count'].sum()

    @staticmethod
    def generate_metric_result(data_frame: pandas.DataFrame) -> str:
        total_cars = TotalCarsMetricGenerator.generate_metric(data_frame)

        response = f'Total Cars = {total_cars}'

        return response
