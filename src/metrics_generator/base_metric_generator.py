from abc import ABC, abstractmethod
from logging import Logger

import pandas


class BaseMetricGenerator(ABC):
    def __init__(self, logger: Logger, data_frame: pandas.DataFrame):
        self._logger = logger
        self._data_frame = data_frame.copy()

    @abstractmethod
    def enabled(self) -> bool:
        """
        return if the reporting metric is enabled
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def order_number() -> int:
        """
        The serial number of metric. For processing metrics in order.
        """
        raise NotImplementedError()

    @abstractmethod
    def meets_condition(self) -> bool:
        """
        The self._dataframe qualifies for this metric or not
        """
        raise NotImplementedError()

    @abstractmethod
    def generate_metric(self):
        raise NotImplementedError()

    @abstractmethod
    def generate_metric_result(self) -> str:
        """
        string formulation of generate_metric for reporting purposes.
        """
        raise NotImplementedError()
