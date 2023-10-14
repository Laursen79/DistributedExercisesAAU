import abc
import os
import unittest
from typing import Any


class Exercise:
    _path: str
    _aliases: set[str]
    _code: Any

    @classmethod
    def from_file(cls, path: str) -> "Exercise":
        exercise = cls()
        exercise._path = path
        exercise._aliases = {os.path.basename(path)}
        return exercise

    def has_alias(self, identifier: str):
        return identifier in self._aliases

    def load(self):
        with open(self._path) as file:
            exercise = file.read()
        lines = exercise.split('\n')
        comments = []
        for line in lines:
            if line.startswith('#'):
                comments.append(line)

        # Compile
        self._code = compile(exercise, os.path.basename(self._path), "exec")

    def run(self):
        namespace = {}
        exec(self._code, namespace)
        suite = unittest.TestLoader().loadTestsFromTestCase(namespace["TestCase"])
        result = unittest.TestResult()
        suite.run(result)
        print(result)


class ExerciseCollector(abc.ABC):

    @abc.abstractmethod
    def collect(self) -> set[Exercise]:
        raise NotImplementedError()


class FileCollector(ExerciseCollector):
    def __init__(self, base_path):
        self._path = base_path

    def collect(self) -> set[Exercise]:
        exercises = set()
        for file in os.listdir(self._path):
            # Check for file extension.
            ext = file.split('.')
            length = len(ext)
            if length > 1:
                ext = ext[length-1]
            else:
                continue  # The file does not have an extension.

            if ext == "py":
                path = os.path.join(self._path, file)
                exercises.add(Exercise.from_file(path))
        return exercises
