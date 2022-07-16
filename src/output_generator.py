class OutputGenerator:
    def __init__(self, file_content: str, output_path: str):
        self._file_content = file_content
        self._output_path = output_path

    def write_output(self):
        with open(self._output_path, 'w') as f:
            f.write(self._file_content)
