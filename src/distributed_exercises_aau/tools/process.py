import abc
from queue import Queue
from typing import Any

type PID = int


class Message:
    ...

class World:
    ...

class CommunicationMedium:
    _queue: Queue

    def send(self, message: Message, recipient_pid: PID) -> None:
        ...

    def receive(self, sender: PID) -> Message:
        ...

    def receive_all(self) -> [Message]:
        ...


class Process(abc.ABC):
    _world: World
    _pid: PID
    _medium: CommunicationMedium

    @abc.abstractmethod
    def run(self) -> None:
        """
        The ``run`` method of the ``Process`` class contains the logic that is performed during a **run**. When ``run``
        returns, the process is done.

        .. code-block:: python
           :caption: Example

            from distributed_exercises_aau import Process

            class Gossip(Process):
                def __init__(self):
                    self.secrets = {self.pid}

                def run(self):
                    while not len(secrets) == self.process_count:
                        self.medium.send(secrets, self.pid + 1)


        :return: ``None``
        """
        raise NotImplementedError()

    @property
    def pid(self) -> PID:
        """
        The Process ID: An integer that represents the identity of the Process.
        """
        return self._pid

    @property
    def medium(self) -> CommunicationMedium:
        """
        The medium facilitates communication between different processes.
        """
        return self._medium

    @property
    def process_count(self):
        return self._world.process_count
