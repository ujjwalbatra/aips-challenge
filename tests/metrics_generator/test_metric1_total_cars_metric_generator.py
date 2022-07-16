from unittest import TestCase

import pandas

from src.metrics_generator.metric1_total_cars_metric_generator import TotalCarsMetricGenerator

df_input = [1, 2, 3]
test_data_frame1 = pandas.DataFrame(df_input, columns=['Count'])
test_data_frame2 = pandas.DataFrame(df_input, columns=['Counts'])


class TestTotalCarsMetricGenerator(TestCase):
    def test_meets_condition_success(self):
        result = TotalCarsMetricGenerator.meets_condition(test_data_frame1)
        self.assertEqual(result, True)

    def test_meets_condition_failure(self):
        result = TotalCarsMetricGenerator.meets_condition(test_data_frame2)
        self.assertEqual(result, False)

    def test_generate_metric(self):
        result = TotalCarsMetricGenerator.generate_metric(test_data_frame1)
        self.assertEqual(result, sum(df_input))
