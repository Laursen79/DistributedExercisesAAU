import os


class ExerciseCollector:
    def collect(self):
        cwd = os.getcwd()
        exercises_dir = os.path.join(cwd, "exercises")
        assert "exercises" in os.listdir(cwd), f"No exercises subdirectory found in directory {cwd}."
        for exercise in os.listdir(exercises_dir):
            print(exercise)
