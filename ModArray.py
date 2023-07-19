'''
You are given a large number in the form of a array A of size N where each element denotes a digit of the number.
You are also given a number B. You have to find out the value of A % B and return it.

Input 1:
A = [1, 4, 3] B = 2

Input 2:
A = [4, 3, 5, 3, 5, 3, 2, 1] B = 47

Output 1:
1

Output 2:
20
'''

def modArray_1(array,num):
    power = 1 
    result = 0
    for i in range(len(array)-1, -1, -1):
        result = (result + ((array[i] % num) * power)) % num
        power = (power*10) % num
    return result


def modArray_2(array,num):
    result = 0
    for i in range(0,len(array)):
        result += (((10**(len(array)-i-1)))* array[i])
    return(result % num)

array = list(map(int, input().split()))
num = int(input())

print(modArray_1(array,num))
print(modArray_2(array,num))

