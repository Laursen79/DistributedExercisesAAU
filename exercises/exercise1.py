import unittest

from distributed_exercises_aau import Process

# Exercise    1 ====================================================================================================== #
#
#   This is a demonstration exercise to teach you how to use the framework.
#   To solve this exercise, modify the method `return_i_understand` to return "I understand".
#
#   Before you solve the exercise, you should try to run `ds-exercise 0` in your terminal. You should see something
#   Like this:
#
#
# ==================================================================================================================== #


class GossipMessage(MessageStub):

    def __init__(self, sender: int, destination: int, secrets):
        super().__init__(sender, destination)
        # we use a set to keep the "secrets" here
        self.secrets = secrets

    def __str__(self):
        return f'{self.source} -> {self.destination} : {self.secrets}'


class Gossip(Process):
    def __init__(self):
        self.secrets = {self.pid}

    def run(self):
        # the following is your termination condition, but where should it be placed?
        # if len(self._secrets) == self.number_of_devices():
        #    return
        self.
        return

    def print_result(self):
        print(f'\tDevice {self.index()} got secrets: {self._secrets}')



# ! DO NOT EDIT ! ==================================================================================================== #
# The code below is tests that will determine whether your solution is correct.                                        #
# You should not edit anything below this point.                                                                       #
# ==================================================================================================================== #

class TestCase(unittest.TestCase):
    def test_every_secret_known(self):
        ...