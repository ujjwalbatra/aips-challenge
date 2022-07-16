import logging
from unittest import TestCase

import pandas

from src.metrics_generator.metric4_three_least_consecutive_total_metric_generator import \
    ThreeLeastConsecutiveTotalMetricGenerator

datelist = pandas.date_range(start='1/1/2020', periods=4, freq="30min")
count = [1, 2, 3, 4]
test_data_frame1 = pandas.DataFrame({'Timestamp': datelist, 'Count': count})
test_data_frame2 = pandas.DataFrame({'Timestamp': datelist, 'Counts': count})


class TestThreeLeastConsecutiveTotalMetricGenerator(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_meets_condition_success(self):
        result = ThreeLeastConsecutiveTotalMetricGenerator.meets_condition(test_data_frame1)
        self.assertEqual(result, True)

    def test_meets_condition_failure(self):
        result = ThreeLeastConsecutiveTotalMetricGenerator.meets_condition(test_data_frame2)
        self.assertEqual(result, False)

    def test_generate_metric(self):
        result = ThreeLeastConsecutiveTotalMetricGenerator.generate_metric(test_data_frame1)
        self.assertEqual(result.iloc[0]['ConsecutiveSum'], 6)
