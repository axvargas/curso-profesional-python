'''
Created Date: Sunday August 1st 2021 4:41:12 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday August 1st 2021 5:59:15 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''

from time import sleep


class FibonacciIter():

    def __init__(self, max: int = None) -> None:
        self.max = max

    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self

    def __is_in_range(self, num) -> bool:
        return num <= self.max

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            if(self.max == None or self.__is_in_range(self.num1)):
                return self.num1
            else:
                raise StopIteration
        elif self.counter == 1:
            self.counter += 1
            if(self.max == None or self.__is_in_range(self.num2)):
                return self.num2
            else:
                raise StopIteration
        else:
            self.counter += 1
            self.aux = self.num1 + self.num2
            self.num1, self.num2 = self.num2, self.aux
            if(self.max == None or self.__is_in_range(self.aux)):
                return self.aux
            else:
                raise StopIteration


if __name__ == '__main__':
    fibo = FibonacciIter(121393)
    # fibo2 = FibonacciIter()
    for element in fibo:
        print(element)
        sleep(0.1)
    
    # for element in fibo2:
    #     print(element)
    #     sleep(0.1)
