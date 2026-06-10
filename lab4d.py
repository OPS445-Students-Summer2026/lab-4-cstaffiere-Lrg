#!/usr/bin/env python3

# Author: Christian Staffiere
# Author ID: 144393246
# Date: 2026/06/09
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    # Place code here - refer to function specifics in section below
    f5 = string[:5]
    return f5

def last_seven(string):
    # Place code here - refer to function specifics in section below
    l7 = string[-7:]
    return l7

def middle_number(number):
    # Place code here - refer to function specifics in section below
    str_num = str(number)
    mn = str_num[1:3]
    return mn


def first_three_last_three(string1, string2):
    # Place code here - refer to function specifics in section below
    f3 = string1[:3]
    l3 = string2[-3:]
    return f3 + l3


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))