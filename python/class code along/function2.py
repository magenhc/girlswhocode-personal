'''
def calc_total(list):
    sum = 0
    for num in list:
        sum += num
    # outside the for loop
    print(sum)
    return sum

list = [2, 3, 4, 5, 9, 89]
calc_total(list)
'''

def add(num1, num2):
    sum = num1 + num2
    return sum

def double(number):
    result = number * 2
    print(result)
    return result

func1 = add(3, 4)
double(func1)
