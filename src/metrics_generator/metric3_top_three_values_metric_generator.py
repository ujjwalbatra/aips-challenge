import pandas

from metrics_generator.base_metric_generator import BaseMetricGenerator


class TopThreeValuesMetricGenerator(BaseMetricGenerator):
    def enabled(self) -> bool:
        return True

    @staticmethod
    def order_number() -> int:
        return 3

    def meets_condition(self) -> bool:
        column1_name = 'Timestamp'
        column1_type = 'datetime64[ns]'
        column2_name = 'Count'
        column2_type = 'int64'

        if column1_name in self._data_frame and self._data_frame.dtypes[column1_name] == column1_type \
                and column2_name in self._data_frame and self._data_frame.dtypes[column2_name] == column2_type:
            return True
        else:
            self._logger.error('Failed TopThreeValuesMetricGenerator.meets_condition')
            return False

    def generate_metric(self):
        self._data_frame['Timestamp'] = self._data_frame['Timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
        return self._data_frame.nlargest(n=3, columns=['Count'], keep='all')

    def generate_metric_result(self) -> str:
        result = self.generate_metric().to_string(index=False)
        return f"""
Top 3 half hours with most cars:
{result}"""
