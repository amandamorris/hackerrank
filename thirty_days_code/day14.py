class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        """Finds the maximum difference between any two elements in
        self.__elements"""

        length = len(self.__elements)
        max_diff = abs(self.__elements[0] - self.__elements[1])
        for i in range(length):
            for j in range(i+1, length):
                difference = abs(self.__elements[i] - self.__elements[j])
                if difference > max_diff:
                    max_diff = difference
        self.maximumDifference = max_diff
