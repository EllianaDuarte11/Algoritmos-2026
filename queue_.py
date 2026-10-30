class Queue():
    def __init__(self):
        self.__elements = []
    def arrive(self, value):
        self.__elements.append(value)
    def attention(self):
        return self.__elements.pop(0) if self.__elements else None
    def size(self):
        return len(self.__elements)
    def show(self):
        print(self.__elements)
