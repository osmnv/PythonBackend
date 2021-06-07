
'''
    Class, extending built-in list functionality
'''

from functools import total_ordering

@total_ordering
class CustomList(list):
    ''' CustomList '''

    def __add__(self, other):
        temp_self = self[:]
        temp_other = other[:]
        if len(self) > len(other):
            temp_other.extend((0,) * (len(self) - len(other)))
        elif len(self) < len(other):
            temp_self.extend((0,) * (len(other) - len(self)))
        for i in range(len(temp_self)):
            temp_self[i] += temp_other[i]
        return CustomList(temp_self)

    def __neg__(self):
        temp_list = self[:]
        for i in range(len(temp_list)):
            temp_list[i] *= -1
        return CustomList(temp_list)

    def __radd__(self, other):
        return CustomList.__add__(self, other)

    def __sub__(self, other):
        return CustomList.__add__(self, CustomList.__neg__(other))

    def __rsub__(self, other):
        return CustomList.__sub__(other, self)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)
