from abc import ABC, abstractmethod

import pandas


class BaseMetricGenerator(ABC):
    @staticmethod
    @abstractmethod
    def enabled() -> bool:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def order_number() -> int:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def meets_condition(data_frame: pandas.DataFrame) -> bool:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def generate_metric(data_frame: pandas.DataFrame):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def generate_metric_result(data_frame: pandas.DataFrame) -> str:
        raise NotImplementedError()
