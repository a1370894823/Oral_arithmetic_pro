import numpy as np
import random


def calculator(input1, cal, input2=0):

    a, num1 = load_a(input1, cal)
    if cal == 3:  # 乘法
        b_max = 99 // a
        b = random.randint(1, b_max)
        c = a * b
        num2 = b

    if cal == 4:  # 除法
        b = factorization(a)
        c = a / b
        num2 = b

    if cal == 1:  # 加法
        if input1 == 0:
            if input2 == 0:
                b_max = 100 - a
                b = random.randint(1, b_max+1)
                num2 = b
            else:
                b = ans[step-1]
                a_max = 99 - int(b)
                a = random.randint(1, a_max+1)
                num1 = a
                num2 = input2
        else:
            if input2 == 0:
                b_max = 100 - a
                b = random.randint(1, b_max+1)  # 加1，防止b_max = 0,
                num2 = b
            else:
                b = ans[step-1]
                a = ans[step - 2]
                num1 = input1
                num2 = input2
        c = a + b

    if cal == 2:  # 减法
        if input1 == 0:
            if input2 == 0:
                b_max = a
                b = random.randint(1, b_max)
                num2 = b
            else:
                b = ans[step-1]
                a = random.randint(b, 100)
                num1 = a
                num2 = input2
        else:
            if input2 == 0:
                b = random.randint(1, a)
                num2 = b
            else:
                b = ans[step-1]
                a = ans[step-2]
                num1 = input1
                num2 = input2
        c = a - b
    return num1, num2, c


def load_a(input1, cal):
    if input1 == 0:
        if cal == 3:
            a = random.randint(1, 49)
        else:
            a = random.randint(1, 99)
        num1 = a
    else:
        a = ans[step-1]
        num1 = input1
    return a, num1


def factorization(num):
    factor = []
    for i in range(2, num):
        while i != num:
            if num % i == 0:
                factor.append(i)
                num = num / i
            else:
                break
    long = len(factor)
    random.shuffle(factor)
    aa = random.randint(0, long)
    out = int(np.prod(factor[:aa]))
    return out




calc_trans = {1: '+',
              2: '-',
              3: '*',
              4: '/'}

# num_cal = random.randint(2, 3)
# calculators_num = np.random.randint(1, 4.1, size=num_cal)
num_cal = 2
calculators_num =[3,1]
results = [0]*(2 * num_cal + 1)
ans = [0]*num_cal
step = 0

for index, cal in enumerate(calculators_num):
    if cal > 2.5:  # 先算乘除
        results[index * 2 + 1] = calc_trans[cal]
        results[index * 2], results[index * 2 + 2], ans[step] = calculator(results[index * 2], cal)  # 乘除运算符后面的数一定没有生成呢
        step += 1

for index, cal in enumerate(calculators_num):
    if cal < 2.5:  # 再算加减
        results[index * 2 + 1] = calc_trans[cal]
        results[index * 2], results[index * 2 + 2], ans[step] = calculator(results[index * 2], cal, results[index * 2 + 2]) # 加减运算符前后的数可能都生成过了
        step += 1

results.append('=')
results.append(ans[-1])
print(results[:])