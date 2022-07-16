from metrics_generator.base_metric_generator import BaseMetricGenerator


class TotalCarsMetricGenerator(BaseMetricGenerator):

    def enabled(self) -> bool:
        return True

    @staticmethod
    def order_number() -> int:
        return 1

    def meets_condition(self) -> bool:
        column_name = 'Count'
        column_type = 'int64'

        if column_name in self._data_frame and self._data_frame.dtypes[column_name] == column_type:
            return True
        else:
            self._logger.error('Failed TotalCarsMetricGenerator.meets_condition')
            return False

    def generate_metric(self):
        return self._data_frame['Count'].sum()

    def generate_metric_result(self) -> str:
        total_cars = self.generate_metric()

        response = f'Total Cars = {total_cars}'

        return response
