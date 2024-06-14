def f(money, Interest, month):
    result = 0
    for i in range(month):
        result += money*((Interest+100)/100)**(month - i)
    return result
print(f(1000,10,12))