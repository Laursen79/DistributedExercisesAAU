import unittest

__aliases__ = ["0", "welcome", "start"]


# Exercise    0 ====================================================================================================== #
#
#   This is a demonstration exercise to teach you how to use the framework.
#   To solve this exercise, modify the method `return_i_understand` to return "I understand".
#
#   Before you solve the exercise, you should try to run `ds-exercise 0` in your terminal. You should see something
#   Like this:
#
#   Exercise 0: 1 Tests failed, 0 Succeeded =============================================================
#       0.1: The method `return_i_understand must return the string: "I understand".
#            Hint available for this exercise:  To receive a hit, type `ds-exercise hint 0.1`
#
#   When you are ready to try again, run `ds-exercise 0.1`
#   ====================================================================================================
#
#   After you have solved the exercise, run `ds-exercise 0` again. Now you should see:
#
#   Exercise 0: 0 Tests failed, 1 Succeeded =============================================================
#       0.1: ✅
#
#   All tests passed, Exercise solved.
#
#   Congratulations :)
#   ====================================================================================================
#
# ==================================================================================================================== #

class TestClass:
    def return_i_understand(self):
        return ...


# ! DO NOT EDIT ! ==================================================================================================== #
# The code below is tests that will determine whether your solution is correct.                                        #
# You should not edit anything below this point.                                                                       #
# ==================================================================================================================== #


class TestCase(unittest.TestCase):
    def test_i_understand(self):
        self.assertTrue(
            TestClass().return_i_understand() == "I understand",
            "The method `return_i_understand must return the string: \"I understand\""
        )
