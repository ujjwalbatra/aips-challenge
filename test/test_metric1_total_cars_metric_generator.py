import logging
import unittest
from unittest import TestCase

import pandas

from src.metrics_generator.metric1_total_cars_metric_generator import TotalCarsMetricGenerator

df_input = [1, 2, 3]
test_data_frame1 = pandas.DataFrame(df_input, columns=['Count'])
test_data_frame2 = pandas.DataFrame(df_input, columns=['Counts'])

logger = logging.getLogger()


class TestTotalCarsMetricGenerator(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_meets_condition_success(self):
        result = TotalCarsMetricGenerator(logger, test_data_frame1).meets_condition()
        self.assertEqual(result, True)

    def test_meets_condition_failure(self):
        result = TotalCarsMetricGenerator(logger, test_data_frame2).meets_condition()
        self.assertEqual(result, False)

    def test_generate_metric(self):
        result = TotalCarsMetricGenerator(logger, test_data_frame1).generate_metric()
        self.assertEqual(result, sum(df_input))


if __name__ == '__main__':
    unittest.main()
