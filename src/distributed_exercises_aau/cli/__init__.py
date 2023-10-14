import argparse


class CliParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("exercise")

        self._parser = parser

    @property
    def parser(self):
        return self._parser

    def parse(self):
        return self._parser.parse_args()

__all__ = ["CliParser"]
