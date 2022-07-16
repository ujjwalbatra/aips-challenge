import logging
from unittest import TestCase

import pandas

from src.metrics_generator.metric3_top_three_values_metric_generator import TopThreeValuesMetricGenerator

datelist = pandas.date_range(start='1/1/2020', periods=4, freq="30min")
count = [1, 2, 3, 4]
test_data_frame1 = pandas.DataFrame({'Timestamp': datelist, 'Count': count})
test_data_frame2 = pandas.DataFrame({'Timestamp': datelist, 'Counts': count})
logger = logging.getLogger()


class TestTopThreeValuesMetricGenerator(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_meets_condition_success(self):
        result = TopThreeValuesMetricGenerator(logger, test_data_frame1).meets_condition()
        self.assertEqual(result, True)

    def test_meets_condition_failure(self):
        result = TopThreeValuesMetricGenerator(logger, test_data_frame2).meets_condition()
        self.assertEqual(result, False)

    def test_generate_metric(self):
        result = TopThreeValuesMetricGenerator(logger, test_data_frame1).generate_metric()
        self.assertEqual(result.shape[0], 3)
        self.assertEqual(result.iloc[0]['Count'], 4)
        self.assertEqual(result.iloc[1]['Count'], 3)
        self.assertEqual(result.iloc[2]['Count'], 2)
