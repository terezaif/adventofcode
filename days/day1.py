
SUM = 2020

def get_product_of_2(numbers, SUM=SUM):
    product = 0
    for index1 in range(0,len(numbers)):
        number1 = numbers[index1]
        for index2  in range(index1,len(numbers)):
            number2 = numbers[index2]
            if (number1 + number2 == SUM):
                product = number1*number2
                return product
    return product

def get_product_of_3(numbers, SUM=SUM):
    product = 0
    for index1 in range(0,len(numbers)):
        number1 = numbers[index1]
        for index2  in range(index1,len(numbers)):
            number2 = numbers[index2]
            for index3 in range(index2,len(numbers)):
                number3 = numbers[index3]
                if (number1 + number2 + number3== SUM):
                    product = number1*number2*number3
                    return product
    return product