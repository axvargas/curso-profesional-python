'''
Created Date: Sunday August 1st 2021 6:54:47 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday August 1st 2021 6:56:43 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
def remove_duplicates(some_list):
    return list(set(some_list))

def main():
    my_list = [1,2,3,4,5,6,7,4,5,21,1,2,3,5,4,8,2,3,1,45,6,2,3]
    print(remove_duplicates(my_list))
if __name__ == '__main__':
    main()