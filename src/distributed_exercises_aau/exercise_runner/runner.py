from .collector import ExerciseCollector


class ExerciseRunner:
    """
    A generic ExerciseRunner implementation.
    """
    _exercises: set

    def __init__(self, collector: ExerciseCollector):
        self._collector = collector

    def __repr__(self):
        return f"Default Exercise Runner: {self._collector}"

    def load(self):
        self._exercises = self._collector.collect()
        for exercise in self._exercises:
            exercise.load()

    def run(self, identifier: str):
        for exercise in self._exercises:
            if exercise.has_alias(identifier):
                exercise.run()
                break
