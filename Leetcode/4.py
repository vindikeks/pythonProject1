d = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
num = 3
result = ''
while num != 0:
    for key in d:
        if key <= num:
            temp = num // key
            for i in range(temp):
                result = result + d[key]
            num = num % key
print(result)
