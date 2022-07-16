import logging
from datetime import datetime

from data_reader import LocalTextFileReader
from output_generator import OutputGenerator
from metrics_generator.base_metric_generator import BaseMetricGenerator
from metrics_generator.metric1_total_cars_metric_generator import TotalCarsMetricGenerator

if __name__ == "__main__":
    logger = logging.getLogger()
    try:
        data_reader = LocalTextFileReader()
        data_frame = data_reader.get_content()
        result: str = ''

        for metric_cls in sorted(BaseMetricGenerator.__subclasses__(), key=lambda x: x.order_number()):
            if metric_cls.enabled() and metric_cls.meets_condition(data_frame):
                result += f"\n{metric_cls.generate_metric_result(data_frame)}"

        if len(result) > 0:
            OutputGenerator(result, f'output/report:{datetime.now()}.txt').write_output()
    except Exception as e:
        logger.error(e, exc_info=True)
