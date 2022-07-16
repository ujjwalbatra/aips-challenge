import logging

import pandas

from metrics_generator.base_metric_generator import BaseMetricGenerator


class TopThreeValuesMetricGenerator(BaseMetricGenerator):
    _logger = logging.getLogger(__name__)

    @staticmethod
    def enabled() -> bool:
        return True

    @staticmethod
    def order_number() -> int:
        return 3

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
            TopThreeValuesMetricGenerator._logger.error('Failed TopThreeValuesMetricGenerator.meets_condition')
            return False

    @staticmethod
    def generate_metric(data_frame: pandas.DataFrame):
        df = data_frame.copy()
        df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
        return df.nlargest(n=3, columns=['Count'], keep='all')

    @staticmethod
    def generate_metric_result(data_frame: pandas.DataFrame) -> str:
        result = TopThreeValuesMetricGenerator.generate_metric(data_frame).to_string(index=False)
        return f"""
Top 3 half hours with most cars:
{result}"""
