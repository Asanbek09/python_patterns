from abc import ABC, abstractmethod
from enum import Enum

State = Enum(
    "State",
    "NEW RUNNING SLEEPING RESTART ZOMBIE",
)

class User:
    pass

class Process:
    pass

class File:
    pass

class Server(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        self.name = "FileServer"
        self.state = State.NEW

    def boot(self):
        print(f"booting the {self}")
        self.state = State.RUNNING

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_file(self, user, name, perms):
        msg = (
            f"trying to create file '{name}' "
            f"for user '{user}' "
            f"with permissions {perms}"
        )
        print(msg)


class ProcessServer(Server):
    def __init__(self):
        self.name = "ProcessServer"
        self.state = State.NEW

    def boot(self):
        print(f"booting the {self}")
        self.state = State.RUNNING

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_process(self, user, name):
        msg = f"trying to create process '{name}' " f"for user '{user}'"
        print(msg)

class WindowServer:
    pass

class NetworkServer:
    pass

class OperatingSystem:
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, perms):
        return self.fs.create_file(user, name, perms)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file("foo", "hello.txt", "-rw-r-r")
    os.create_process("bar", "ls /tmp")


if __name__ == "__main__":
    main()