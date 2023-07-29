# -*- coding: cp1251 -*-

from base64 import encode
import encodings
from itertools import filterfalse
import os
import csv
from datetime import datetime
import unicodedata


fistRow = ['ID заметки', 'Дата заметки', 'Время заметки', 'Заметка']

#проверка даты на правильность ввода, вводим до тех пор пока дата не будет корректной и возвращаем введеное, проверенное значение
def checkDate():                                                            
    flag = True
    while flag == True:
        inputDate = input("Введите дату записи (dd.mm.yyyy): ")
        try:
            datetime.strptime(inputDate, '%d.%m.%Y')
            flag = False
        except :
            print("Введена некорректная дата, повторите ввод")
            flag = True        
    return inputDate                                                        

#проверка времени на правильность ввода, вводим до тех пор пока время не будет корректным и возвращаем введеное, проверенное значение
def checkTime():                                                            
    flag = True
    while flag == True:
        inputTime = input("Введите время записи (hh:mm): ")
        try:
            datetime.strptime(inputTime, '%H:%M')
            flag = False
        except :
            print("Введено некорректное время, повторите ввод")
            flag = True
    return inputTime                                                        

#вспомогательный метод для изменения записи, выбираем пункт для замены и  перезаписываем его в массив
def changeNote(changeRow):
    flag = True
    while flag == True:
        count = 0
        print("Что надо изменить: ")
        for x in enumerate(fistRow):
            if count != 0:
                print(x[0],'-',x[1])
            count+=1
        inputChange = int(input("Введите номер изменяемого элемента: "))   
        if inputChange == 1:
            inputData = checkDate()
            flag = False
        elif inputChange == 2:
            inputData = checkTime()
            flag = False
        elif inputChange == 3:
            inputData = input("Введите запись: ")
            flag = False
        else:
            print("Введите число от 1 до 3")
    changeRow[inputChange] = inputData
    return changeRow

#метод записи в файл, в качестве аргумента передаем список для записи и парамент записи "w", "a"
def writeNote(dataList, param):
    try:
        with open('notebook.csv', param, newline='') as fp:                       
            writer = csv.writer(fp, delimiter=";")
            writer.writerow(dataList)
    except :
        print("Что то пошло не так в методе writeNote()")
    

#метод для чтения файл, чтение производится в массив, для последующей работы с ним
def readNote():
    dataList = []
    try:
        with open('notebook.csv', 'r') as fp:
            reader = csv.reader(fp, delimiter=';')
            for row in reader:
                dataList.append(row)
    except:        
        print("Что то пошло не так в методе readNote()")
    return dataList

#метод для получения номера записи, возвращаем номер на основе уже существующих данных
def checkID():
    ID = 1
    dataList = readNote()
    if len(dataList) - 1 == 0:
        return ID
    else:
         ID = len(dataList) 
    return ID

def clearNote():
    fileNote = open('notebook.csv', 'w')
    fileNote.seek(0)
    fileNote.close()
#метод добавления записи, работает при выборе 1 пункта
def add():
    dataList = []
    ID = checkID()
    inputDate = checkDate()    
    inputTime = checkTime()    
    inputNote = input("Введите запись: ")
    dataList = [ID, inputDate, inputTime,inputNote]
    writeNote(dataList, 'a')
    print("Запись добавлена")

#метод изменения записи, чиатем файл и сохраняем его в список, запрашиваем номер записи, 
#ищем его в списке и меняем, или выдаем сообщение об отсутствии искомого номера
def  change():
    dataList = readNote()
    if len(dataList) != 1:
        inputId = input("Введите номер изменяемой записи: ")
        if inputId > str(len(dataList)-1):
            print("Искомый номер отсутствует")
        else:
            clearNote()
            for row in dataList:
                if inputId == row[0]:
                    row = changeNote(row)                  
                writeNote(row, 'a')
                print("Запись изменена")
    else:
        print("Заметок еще не создано, создайте их выбрав пункт 1.")
    

#метод для вывода на экран списка заметок, чиатем файл и сохраняем его в список, 
#если список пустой, выводим соответсвующее сообщение
def show():
    count = 0
    dataList = readNote()
    if len(dataList) != 1:
        for row in dataList:
            if count == 0:
                print(row[0], '\t',row[1], '\t', row[2], '\t', row[3])
            else:
                print(row[0], '\t\t',row[1], '\t', row[2], '\t\t', row[3])
            count +=1
    else:
        print("Заметок еще не создано, создайте их выбрав пункт 1.")

def remove():
    dataList = readNote()
    if len(dataList) != 1:
        inputId = int(input("Введите номер изменяемой записи: "))
        if inputId > len(dataList)-1:
            print("Искомый номер отсутствует")
        else:
            clearNote()
            dataList.pop(inputId)
            print("Запись удалена")
            for row in dataList:
                writeNote(row, 'a')
                
    else:
        print("Заметок еще не создано, создайте их выбрав пункт 1.")
   

#метод для создания файла с заголовками при его отсутствии
def creatFile():
    isFile = False
    if isFile == os.path.isfile('notebook.csv'):
        writeNote(fistRow, "w")

#метод начала программы
def start():
    creatFile()        
    flag = True
    while flag == True:
        print (" 1 - Добавить запись")
        print (" 2 - Изменить запись")
        print (" 3 - Просмотреть все записи")
        print (" 4 - удалить запись")
        num = input("Выберите раздел: ")
        if num == '1':
            add()
        elif num == '2':
            change()
        elif num == '3':
            show()
        elif num == '4':
            remove()
        elif num == 'q':
            flag = False
start()