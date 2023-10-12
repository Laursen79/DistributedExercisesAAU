from .collector import ExerciseCollector


def main():
    ExerciseCollector().collect()


__all__ = ["main", "ExerciseCollector"]
