a = ['1', '2', 'aa', 'b', '3']
b = ['3', '45', 'b']

###################################################################
def sum_of_lists(list1, list2):
    suma = list2[:]
    for i in list1:
        if i not in list2:
            suma.append(i)
    return suma

#print(f'a + b = {sum_of_lists(a, b)}')

###################################################################
def sub_of_lists(list1, list2):
    sub = list1[:]
    for i in list2:
        while i in sub:
            sub.remove(i)
    return sub

#print(f'b - a = {sub_of_lists(b,a)}')
#print(f'a - b = {sub_of_lists(a,b)}')

###################################################################
def mul_of_lists(list1, list2):
    mul = []
    for i in list1:
        if i in list2:
            mul.append(i)
    return mul

#print(f'a * b = {mul_of_lists(a,b)}')

###################################################################
def check_input(input):
    operations = ['+', '-', '*']

    operation = ''
    for i in operations:
        if i in input:
            operation += i

    count_of_brackets = 0
    for i in input:
        if i in ['{', '}']:
            count_of_brackets += 1
    
    if (1 != len(operation)) or (4 != count_of_brackets):
        return False
    else:
        return operation

###################################################################
def str_to_list(str):
    str = str.replace('{', '')
    str = str.replace('}', '')
    x = str.split(',')
    return x

###################################################################
def main():
    user = input("Give us operation to make: ").replace(' ', '')
    x = check_input(user)
    match x:
        case False:
            print("There is something wrong with given operation")
        case '-': 
            a, b = user.split(x)
            a, b = str_to_list(a), str_to_list(b)
            print(f'a - b = {sub_of_lists(a,b)}')
        case '*':
            a, b = user.split(x)
            a, b = str_to_list(a), str_to_list(b)
            print(f'a * b = {mul_of_lists(a,b)}')
        case '+': 
            a, b = user.split(x)
            a, b = str_to_list(a), str_to_list(b)
            print(f'a + b = {sum_of_lists(a, b)}')

main()