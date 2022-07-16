import logging
from unittest import TestCase

import pandas

from src.metrics_generator.metric2_total_cars_grouped_by_day_metric_generator import \
    TotalCarsGroupedByDayMetricGenerator

datelist = pandas.date_range(start='1/1/2020', periods=3, freq="30min")
count = [1, 2, 3]
test_data_frame1 = pandas.DataFrame({'Timestamp': datelist, 'Count': count})
test_data_frame2 = pandas.DataFrame({'Timestamp': datelist, 'Counts': count})
logger = logging.getLogger()


class TestTotalCarsGroupedByDayMetricGenerator(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_meets_condition_success(self):
        result = TotalCarsGroupedByDayMetricGenerator(logger, test_data_frame1).meets_condition()
        self.assertEqual(result, True)

    def test_meets_condition_failure(self):
        result = TotalCarsGroupedByDayMetricGenerator(logger, test_data_frame2).meets_condition()
        self.assertEqual(result, False)

    def test_generate_metric(self):
        result = TotalCarsGroupedByDayMetricGenerator(logger, test_data_frame1).generate_metric()
        self.assertEqual(result.loc[0]['Total'], sum(count))
        self.assertEqual(result.loc[0]['Date'], '2020-01-01')
