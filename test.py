'''
Created Date: Sunday August 1st 2021 5:17:40 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday August 1st 2021 6:32:04 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from time import sleep
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    fibonacci = fibonacci_gen()
    for element in fibonacci:
        print(element)
        sleep(1)