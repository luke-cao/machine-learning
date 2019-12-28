# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min = None
#         self.lookup = {}
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if x in self.lookup:
#             self.lookup[x] += 1
#         else:
#             self.lookup[x] = 1
#         if self.min is None:
#             self.min = x
#         elif x < self.min:
#             self.min = x
#
#     def pop(self) -> None:
#         x = self.stack.pop()
#         self.lookup[x] -= 1
#         if self.lookup[x] == 0:
#             del self.lookup[x]
#         if x == self.min and x not in self.lookup:
#             self.min = min(self.lookup) if self.lookup else None
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.min.append(min(self.min[-1], x)) if self.min else self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
