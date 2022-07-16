from abc import ABC, abstractmethod

import pandas


class DataReader(ABC):
    @abstractmethod
    def get_content(self) -> pandas.DataFrame:
        raise NotImplementedError()


class LocalTextFileReader(DataReader):
    def __init__(self):
        self._input_directory = 'input_data/'

    def get_content(self) -> pandas.DataFrame:
        file_name = input('Enter the name of input file (in input_data directory). For e.g., input.txt: ')
        df = pandas.read_csv(f'{self._input_directory}{file_name}', header=None, delimiter=' ')
        df.columns = ['Timestamp', 'Count']
        df['Timestamp'] = pandas.to_datetime(df['Timestamp'])

        return df
