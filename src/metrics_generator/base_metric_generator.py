from abc import ABC, abstractmethod
from logging import Logger

import pandas


class BaseMetricGenerator(ABC):
    def __init__(self, logger: Logger, data_frame: pandas.DataFrame):
        self._logger = logger
        self._data_frame = data_frame.copy()

    @abstractmethod
    def enabled(self) -> bool:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def order_number() -> int:
        raise NotImplementedError()

    @abstractmethod
    def meets_condition(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def generate_metric(self):
        raise NotImplementedError()

    @abstractmethod
    def generate_metric_result(self) -> str:
        raise NotImplementedError()
