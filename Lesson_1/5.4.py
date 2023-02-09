# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).

#n = input()
nums = input()
print(nums[::-1])

# Или

def rev_num(num):
    if num == 0:
        return ""
    nums = input()
    return rev_num(num - 1) + f"{nums} "


print(rev_num(int(input())))