'''
Created Date: Sunday August 1st 2021 6:20:02 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday August 1st 2021 6:36:10 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from time import sleep

def fibonacci_gen(max: int = None) -> int:
    n1, n2, counter = 0, 1, 0

    while max == None or n1 <= max:
        yield n1
        n1, n2 = n2, n1 + n2

if __name__ == '__main__':
    fibo = fibonacci_gen()
    for element in fibo:
        print(element)
        sleep(0.5)