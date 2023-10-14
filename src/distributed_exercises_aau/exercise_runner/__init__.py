import os

from .collector import FileCollector
from .runner import ExerciseRunner
from ..cli import CliParser


def main():
    args = CliParser().parse()
    _collector = FileCollector(os.getcwd()+"/exercises")
    _runner = ExerciseRunner(_collector)
    _runner.load()
    _runner.run(args.exercise)



__all__ = ["main"]
