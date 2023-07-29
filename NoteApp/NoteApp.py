# -*- coding: cp1251 -*-

from base64 import encode
import encodings
from itertools import filterfalse
import os
import csv
from datetime import datetime
import unicodedata


fistRow = ['ID �������', '���� �������', '����� �������', '�������']

#�������� ���� �� ������������ �����, ������ �� ��� ��� ���� ���� �� ����� ���������� � ���������� ��������, ����������� ��������
def checkDate():                                                            
    flag = True
    while flag == True:
        inputDate = input("������� ���� ������ (dd.mm.yyyy): ")
        try:
            datetime.strptime(inputDate, '%d.%m.%Y')
            flag = False
        except :
            print("������� ������������ ����, ��������� ����")
            flag = True        
    return inputDate                                                        

#�������� ������� �� ������������ �����, ������ �� ��� ��� ���� ����� �� ����� ���������� � ���������� ��������, ����������� ��������
def checkTime():                                                            
    flag = True
    while flag == True:
        inputTime = input("������� ����� ������ (hh:mm): ")
        try:
            datetime.strptime(inputTime, '%H:%M')
            flag = False
        except :
            print("������� ������������ �����, ��������� ����")
            flag = True
    return inputTime                                                        

#��������������� ����� ��� ��������� ������, �������� ����� ��� ������ �  �������������� ��� � ������
def changeNote(changeRow):
    flag = True
    while flag == True:
        count = 0
        print("��� ���� ��������: ")
        for x in enumerate(fistRow):
            if count != 0:
                print(x[0],'-',x[1])
            count+=1
        inputChange = int(input("������� ����� ����������� ��������: "))   
        if inputChange == 1:
            inputData = checkDate()
            flag = False
        elif inputChange == 2:
            inputData = checkTime()
            flag = False
        elif inputChange == 3:
            inputData = input("������� ������: ")
            flag = False
        else:
            print("������� ����� �� 1 �� 3")
    changeRow[inputChange] = inputData
    return changeRow

#����� ������ � ����, � �������� ��������� �������� ������ ��� ������ � �������� ������ "w", "a"
def writeNote(dataList, param):
    try:
        with open('notebook.csv', param, newline='') as fp:                       
            writer = csv.writer(fp, delimiter=";")
            writer.writerow(dataList)
    except :
        print("��� �� ����� �� ��� � ������ writeNote()")
    

#����� ��� ������ ����, ������ ������������ � ������, ��� ����������� ������ � ���
def readNote():
    dataList = []
    try:
        with open('notebook.csv', 'r') as fp:
            reader = csv.reader(fp, delimiter=';')
            for row in reader:
                dataList.append(row)
    except:        
        print("��� �� ����� �� ��� � ������ readNote()")
    return dataList

#����� ��� ��������� ������ ������, ���������� ����� �� ������ ��� ������������ ������
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
#����� ���������� ������, �������� ��� ������ 1 ������
def add():
    dataList = []
    ID = checkID()
    inputDate = checkDate()    
    inputTime = checkTime()    
    inputNote = input("������� ������: ")
    dataList = [ID, inputDate, inputTime,inputNote]
    writeNote(dataList, 'a')
    print("������ ���������")

#����� ��������� ������, ������ ���� � ��������� ��� � ������, ����������� ����� ������, 
#���� ��� � ������ � ������, ��� ������ ��������� �� ���������� �������� ������
def  change():
    dataList = readNote()
    if len(dataList) != 1:
        inputId = input("������� ����� ���������� ������: ")
        if inputId > str(len(dataList)-1):
            print("������� ����� �����������")
        else:
            clearNote()
            for row in dataList:
                if inputId == row[0]:
                    row = changeNote(row)                  
                writeNote(row, 'a')
                print("������ ��������")
    else:
        print("������� ��� �� �������, �������� �� ������ ����� 1.")
    

#����� ��� ������ �� ����� ������ �������, ������ ���� � ��������� ��� � ������, 
#���� ������ ������, ������� �������������� ���������
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
        print("������� ��� �� �������, �������� �� ������ ����� 1.")

def remove():
    dataList = readNote()
    if len(dataList) != 1:
        inputId = int(input("������� ����� ���������� ������: "))
        if inputId > len(dataList)-1:
            print("������� ����� �����������")
        else:
            clearNote()
            dataList.pop(inputId)
            print("������ �������")
            for row in dataList:
                writeNote(row, 'a')
                
    else:
        print("������� ��� �� �������, �������� �� ������ ����� 1.")
   

#����� ��� �������� ����� � ����������� ��� ��� ����������
def creatFile():
    isFile = False
    if isFile == os.path.isfile('notebook.csv'):
        writeNote(fistRow, "w")

#����� ������ ���������
def start():
    creatFile()        
    flag = True
    while flag == True:
        print (" 1 - �������� ������")
        print (" 2 - �������� ������")
        print (" 3 - ����������� ��� ������")
        print (" 4 - ������� ������")
        num = input("�������� ������: ")
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