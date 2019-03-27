﻿# Sum1.py


# программа считает количество числе, введенных с клавиатуры (count), их сумму (total), 
# их их среднее арифметическое (mean)


print ("Type integers, each followed be Enter; or just Enter to finish") # приглашение к вводу очередного числа


count = 0 #инициализируем переменную для подсчета количества чисел
total = 0


while True:      # бесконечный цикл. т.к. объект True всегда True
    line = input ("integer: ")    # сохраняем в переменной инфу, введенное пользователем, или пустую # строку, в случае если пользователь просто нажал Enter  
    #?? число по умолчанию считывается в формате str (строка)?
    if line: # верно всегда, пока line -- не пустая строка
        try: # конструкция с try для перехвата исключения, если пользователь ввел значение, кот. не #м.б. преобразовано в число для подсчета 
            number = int (line) # преобразование введенной пользователем строки в число и сохранение её в переменной number
            # ?? может ли быть между именем функции и аргументами в скобках пробел? можно ли ставить пробелы вокруг
            # оператора присваивания “ = “
        except ValueError as err: # действия в случае возникновения исключения ValueError
            print (err) # печатает сообщение об ошибке
            continue # продолжает выполнение while-цикла -- снова печатает приглашение ввести переменную
        count = count + 1
        total = total + number
    else: # т.е. в случае, если line -- пустая строка
        break #прерывает выполнение while-цикла


if count: # предотвращает вывод информации, если count = 0, т.е. пользователь в течение сеанса не ввел ни одного числа
    print ('count = ', count, 'total = ', total, 'mean = ', total / count)
    