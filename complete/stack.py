__author__ = 'tyler'


class Stack(object):

    def __init__(self):
        self.__list = []

    def push(self, elem):
        self.__list.append(elem)

    def pop(self):
        if len(self.__list) > 0:
            return self.__list.pop()
        else:
            raise RuntimeError("Cannot pop from empty Stack")

    def top(self):
        if len(self.__list) > 0:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.__list) == 0

    def __len__(self):
        return len(self.__list)
