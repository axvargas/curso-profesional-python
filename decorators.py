'''
Created Date: Sunday August 1st 2021 3:56:07 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday August 1st 2021 4:16:39 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Execution time :{time_elapsed.total_seconds()}s")
    
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

#args arguments
@execution_time
def sumarize(a: int, b: int) -> int:
   return a + b

# kwargs arguments
@execution_time
def greet(name="Andrew") -> None:
   print(f'Hi {name}')

if __name__ == '__main__':
    random_func()
    sumarize(55, 45)
    greet("Ale")