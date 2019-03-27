# Sum1.py


# программа считает количество числе, введенных с клавиатуры (count), их сумму (total), 
# их их среднее арифметическое (mean)


print ("Type integers, each followed be Enter; or just Enter to finish") # приглашение к вводу очередного числа


count = 0 
total = 0


while True:      
    line = input ("integer: ")    
    if line: 
        try: 
            number = int (line)            
        except ValueError as err: # действия в случае возникновения исключения ValueError
            print (err) # печатает сообщение об ошибке
            continue 
        count = count + 1
        total = total + number
    else: 
        break


if count: # предотвращает вывод информации, если count = 0, т.е. пользователь в течение сеанса не ввел ни одного числа
    print ('count = ', count, 'total = ', total, 'mean = ', total / count)
    
