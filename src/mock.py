#!/usr/bin/env python3

import sys

from pathlib import Path


class MockApp:
    def __init__(self, file_path, output_dir="\0"):
        self.path = Path(file_path).resolve()
        if output_dir == "\0":
            self.output_dir = self.path if self.path.is_dir() else self.path.parent
        else:
            self.output_dir = output_dir
        if not self.path.exists():
            raise FileNotFoundError

    def process(self):
        if self.path.is_file():
            self.__process_as_file()
        if self.path.is_dir():
            files = self.path.iterdir()
            for file in files:
                mock = MockApp(file)
                mock.process()

    def __process_as_file(self, file_name=""):
        with open(self.path, 'r') as file_in:
            ext = self.path.suffix
            with open(str(self.output_dir / self.path.stem) + "_out" + str(self.path.suffix), 'w') as file_out:
                for line in file_in:
                    file_out.write(line.upper())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "/resources/text.txt"
    mock = MockApp(path)
    mock.process()
