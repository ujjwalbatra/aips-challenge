import logging

import pandas

from metrics_generator.base_metric_generator import BaseMetricGenerator


class ThreeLeastConsecutiveTotalMetricGenerator(BaseMetricGenerator):
    _logger = logging.getLogger(__name__)

    @staticmethod
    def enabled() -> bool:
        return True

    @staticmethod
    def order_number() -> int:
        return 4

    @staticmethod
    def meets_condition(data_frame: pandas.DataFrame) -> bool:
        column1_name = 'Timestamp'
        column1_type = 'datetime64[ns]'
        column2_name = 'Count'
        column2_type = 'int64'

        if column1_name in data_frame and data_frame.dtypes[column1_name] == column1_type \
                and column2_name in data_frame and data_frame.dtypes[column2_name] == column2_type:
            return True
        else:
            ThreeLeastConsecutiveTotalMetricGenerator._logger.error(
                'Failed ThreeLeastConsecutiveTotalMetricGenerator.meets_condition')
            return False

    @staticmethod
    def generate_metric(data_frame: pandas.DataFrame):
        df = data_frame.copy()
        df = df.sort_values(by=['Timestamp'])
        df['ConsecutiveSum'] = df['Count'].rolling(3).sum().shift(-2)
        df = df.drop('Count', axis=1)
        df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')

        df = df[df['ConsecutiveSum'] == df['ConsecutiveSum'].min()]
        df['ConsecutiveSum'] = df['ConsecutiveSum'].astype(int)
        return df

    @staticmethod
    def generate_metric_result(data_frame: pandas.DataFrame) -> str:
        result = ThreeLeastConsecutiveTotalMetricGenerator.generate_metric(data_frame)
        return f"""
Top 3 half hours with most cars:
{result.to_string(index=False)}"""
