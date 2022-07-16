from metrics_generator.base_metric_generator import BaseMetricGenerator


class TotalCarsGroupedByDayMetricGenerator(BaseMetricGenerator):
    def enabled(self) -> bool:
        return True

    @staticmethod
    def order_number() -> int:
        return 2

    def meets_condition(self) -> bool:
        column1_name = 'Timestamp'
        column1_type = 'datetime64[ns]'
        column2_name = 'Count'
        column2_type = 'int64'

        if column1_name in self._data_frame and self._data_frame.dtypes[column1_name] == column1_type \
                and column2_name in self._data_frame and self._data_frame.dtypes[column2_name] == column2_type:
            return True
        else:
            self._logger.error('Failed TotalCarsGroupedByDayMetricGenerator.meets_condition')
            return False

    def generate_metric(self):
        self._data_frame['Date'] = self._data_frame['Timestamp'].dt.strftime('%Y-%m-%d')
        return self._data_frame.groupby([self._data_frame['Date']])['Count'].sum().reset_index(name='Total')

    def generate_metric_result(self) -> str:
        result = self.generate_metric().to_string(index=False)
        return f"""
Total cars grouped by day:
{result}"""
