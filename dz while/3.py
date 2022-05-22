def check(password: str):
    k = 0
    if len(password) >= 8:
        k += 1
    low = 0
    high = 0
    digit = 0
    for item in password:
        if item.isupper():
            low += 1
        else:
            high += 1
        if item.isdigit():
            digit += 1
    if k > 0 and low > 0 and high > 0 and digit > 0:
        print('True')
    else:
        print('False')

check("eeeeeeeeeeee")
check("1234567")
check("HuggyWuGGY")
check("MorozDi111")