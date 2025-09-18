'''
*
**
***
****
*****
'''
def star01():
    print('\n'.join(['*' * i for i in range(1, 6)]))




'''
*****
****
***
**
*
'''
def star02():
    print('\n'.join(['*' * i for i in range(5, 0, -1)]))




'''
    *
   **
  ***
 ****
*****
'''
def star03():
    print('\n'.join([' ' * i + '*' * (5 - i) for i in range(4, -1, -1)]))




'''
*****
 ****
  ***
   **
    *
'''
def star04():
    print('\n'.join([' ' * (5 - i) + '*' * i for i in range(5, 0, -1)]))




'''
    *
   ***
  *****
 *******
*********
'''
def star05():
    print('\n'.join([' ' * i + '*' * (2*(5 - i) -1) for i in range(4, -1, -1)]))


if __name__ == '__main__':
    star01()
    star02()
    star03()
    star04()
    star05()
