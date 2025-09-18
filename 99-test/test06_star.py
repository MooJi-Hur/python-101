# 해석하는 숙제
# 1
"""
줄이 바뀔 때마다 별을 하나씩 추가하며 출력됨
*
**
***
****
*****
"""
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))
print('-----')

# 2
"""
줄이 바뀔 때마다 별을 하나씩 줄여가면서 출력
*****
****
***
**
*
"""
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))
print('-----')

# 3
"""
줄이 바뀔 때마다 공백은 줄이고 별은 늘림
    *
   **
  ***
 ****
*****
"""
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(i + 1)]) for i in range(5)]))
print('-----')

# 4
"""
줄이 바뀔 때마다 공백이 증가하고 별은 줄어듦
*****
 ****
  ***
   **
    *
"""
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(5 - i)]) for i in range(5)]))
print('-----')

# 5
"""
줄이 바뀔 때마다 공백은 줄어들고, 별은 홀수 개씩 늘어남
    *
   ***
  *****
 *******
*********
"""
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(2 * i + 1)]) for i in range(5)]))
print('-----')
