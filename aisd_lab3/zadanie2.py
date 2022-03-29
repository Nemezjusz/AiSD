import math


class Circle:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return math.pi * self.r * self.r

    def obwód(self):
        return math.pi * 2 * self.r


class Triangle:
    def __init__(self, b1, b2, b3, h1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.h1 = h1

    def pole(self):
        return (self.b1 * self.h1)/2

    def obwód(self):
        return self.b1 + self.b2 + self.b3


class Square:
    def __init__(self, a):
        self.a = a

    def pole(self):
        return self.a * self.a

    def obwód(self):
        return 4 * self.a