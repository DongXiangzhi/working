def division(divideby):
    return 42/divideby


print(division(2))
print(division(12))
# print(division(0))

def new_division(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('0除错误')


new_division(0)