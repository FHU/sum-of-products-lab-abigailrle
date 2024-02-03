def sum_of_products(list1, list2):
    if len(list1) == len(list2):
        list1 = list1.split(' ')
        list2 = list2.split(' ')
        #if list1.isdigit() and list2.isdigit():
        length = len(list1)
        index = 0
        number_total = 0
        while index < length:
            number = int(list1[index]) * int(list2[index])
            number_total = number_total + number
            index = index + 1
        print(number_total, '\r\n')
        #else:
         #    print('Error')
         #   index = 0 #pass #rint('Error: you must only input integers')
    else:
        print('Error') #: numbers must be the same length
#yo


if __name__ == '__main__':
    input_list1 = input() #'type the first number'
    input_list2 = input() #'type the second number'   
    sum_of_products(input_list1, input_list2)  