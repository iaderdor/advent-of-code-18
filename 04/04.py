import re

class NotInstaceOfNap(Exception):
    pass

class NotInstanceOfGuard(Exception):
    pass

class Staff:

    def __init__(self):
        self.list = list()

    def add_guard(self, guard):
        if (not isinstance(guard, Guard)):
            raise(NotInstanceOfNap)
        if not any(element == guard.id for element in self.list):
            self.list.appen(guard)


class Guard:

    def __init__(self, id):
        self.id = id
        self.naps = list()

    def add_nap(self, nap):
        if (not isinstance(nap, Nap)):
            raise(NotInstaceOfNap)
        self.naps.append(nap) 


        

class Nap:

    def __init__(self, date, start, end):
        self.date = date
        self.start = start
        self.end = end


class Manager:
    
    def __init__(self):
        print('Got new Manager')

    def get_input(self, file):
        self.lines = list()
        with open(file, mode='r') as f:
            for line in f:
                self.lines.append()

    def parse_input(line):
        timestamp = re.split('[|]', line)
        return timestamp

print(Manager.parse_input(["[1518-07-26 00:51]"]) )
