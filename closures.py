'''
Created Date: Sunday August 1st 2021 2:58:59 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday August 1st 2021 3:05:44 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
def print_many_times(n: int):
    def specify_word(word: str):
        return word * n

    return specify_word

def main() -> None:
    times10 = print_many_times(10)
    times4 = print_many_times(4)

    print(times10("Ale"))
    print(times4("Andrew"))

if __name__ == '__main__':
    main()