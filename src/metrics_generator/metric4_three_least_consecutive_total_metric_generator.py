from metrics_generator.base_metric_generator import BaseMetricGenerator


class ThreeLeastConsecutiveTotalMetricGenerator(BaseMetricGenerator):
    def enabled(self) -> bool:
        return True

    @staticmethod
    def order_number() -> int:
        return 4

    def meets_condition(self) -> bool:
        column1_name = 'Timestamp'
        column1_type = 'datetime64[ns]'
        column2_name = 'Count'
        column2_type = 'int64'

        if column1_name in self._data_frame and self._data_frame.dtypes[column1_name] == column1_type \
                and column2_name in self._data_frame and self._data_frame.dtypes[column2_name] == column2_type:
            return True
        else:
            self._logger.error('Failed ThreeLeastConsecutiveTotalMetricGenerator.meets_condition')
            return False

    def generate_metric(self):
        # Assuming the input will have all timestamps (including 0). Also mentioned in README.md
        self._data_frame = self._data_frame.sort_values(by=['Timestamp'])
        self._data_frame['ConsecutiveSum'] = self._data_frame['Count'].rolling(3).sum().shift(-2)
        self._data_frame = self._data_frame.drop('Count', axis=1)
        self._data_frame['Timestamp'] = self._data_frame['Timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')

        self._data_frame = self._data_frame[
            self._data_frame['ConsecutiveSum'] == self._data_frame['ConsecutiveSum'].min()]
        self._data_frame['ConsecutiveSum'] = self._data_frame['ConsecutiveSum'].astype(int)
        return self._data_frame

    def generate_metric_result(self) -> str:
        result = self.generate_metric()
        return f"""
Top 3 half hours with most cars:
{result.to_string(index=False)}"""
