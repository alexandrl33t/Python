

from copy import copy
from dataclasses import replace
from distutils.filelist import findall
from doctest import OutputChecker
from genericpath import exists
from logging import exception
from ntpath import join
import string
from turtle import right
from unicodedata import digit
import re
import right_part as rp

import re

memory = {}

class Check():
    command = ''
    data = ''
    glubina = 0
    skobka_is_opened = False
    def __init__(self, data):
        self.command = ''
        self.data = data
        self.glubina = 0
        self.skobka_is_opened = False

    def calculate(self, command:str, last_word):
        if len(command) == 0:
            if last_word == 'metka' or last_word == 'metka space':
                return f"zОшибка. После метки должно стоять \':\''f{self.command}f1"
            if last_word == ':' or last_word == ': space' :
                return f"zОшибка. После \':\' должна идти переменная'f{self.command}f1"  

        for i in range(len(command)):
            if last_word == 'metka space':
                if command[i] == ":":
                    return self.calculate(command[i+1:len(command)], ':')
                else:
                    return f"zОшибка. После метки должно стоять \':\''f{self.command}f1" 

            if last_word == 'metka':
                if command[i].isdigit():
                        return self.calculate(command[i+1:len(command)], 'metka') 
                elif command[i] != ":" and not command[i].isspace():
                    return f"zОшибка. Метка должна быть целочисленной'f{self.command}f1"                 
                elif command[i].isspace():
                    return  self.calculate(command[i+1:len(command)], 'metka space')              
                elif command[i] == ":":
                    return  self.calculate(command[i+1:len(command)], ':') 
            elif last_word == ':' or last_word == ': space':
                if command[i].isalpha():
                    perem = command[i:i+4]
                    m = re.search('[а-я][0-7][0-7][0-7]', perem)   
                    if not m:
                        return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f{self.command}f1"
                    try:
                        if command[i+4] == " ":
                            if command [i+5] == '=':
                                memory[perem] =  rp.right_calculate(command[i+6:len(command)], memory)
                                if memory[perem].find("z")>-1:
                                    return memory[perem][memory[perem].find("z"):memory[perem].find("f")+1] + self.command + "f1"   
                                return ""
                            else: 
                                return f"zОшибка. После переменной должно стоять \'=\'f{self.command}f1" 
                        elif command[i+4] == '=':
                            memory[perem] = rp.right_calculate(command[i+5:len(command)], memory)
                            if memory[perem].find("z")>-1:
                                return memory[perem][memory[perem].find("z"):memory[perem].find("f")+1] + self.command + "f1" 
                            return ""
                        else: 
                            return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f{self.command}f1"    
                    except:
                        return f"zОшибка. После переменной должно стоять \'=\'f{self.command}f1" 
                elif command[i].isspace():
                     return  self.calculate(command[i+1:len(command)], ': space')
                elif command[i] == ':':
                        return f'zОшибка. Дублируется \':\'f::f1'      
                else: 
                    return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f{self.command}f1"  
        return ""         
                    

    def command_processing(self, command:str):
        if not command.startswith("ввод "):
            return f"zОшибка. Звено должно начинаться со слова \'Ввод\'f{command}f1"
        command = command[command.find("ввод ")+5:len(command)]
        
        return self.calculate(command, 'metka') 

    def check_for_errors(self):
        self.data = self.data.lower()
        self.data = " ".join(self.data.split())
        #начинается со слов программа и конец
        if not self.data.startswith("программа"):
            return "zОшибка. Программа должна начинаться со слова \'Программа\'f"
        if not re.search('.*[\s|\\n]*(конец)$', self.data):
            return "zОшибка. Программа должна заканчиваться словом \'Конец\'f"
        #проверка наличия разделителя
        self.data = " ".join(self.data.split()[1:-1])
        if len(re.findall('ввод', self.data)) - len(re.findall(';', self.data)) > 1:
            place = re.findall('\S*[\w|\)|\]]\s*ввод', self.data)[0]
            return "zОшибка. Отсутствует \';\' между \"" + place + "\"f" + f"{place}f1" 
        
        #разделение на массив команд и обработка каждой
        command_list = re.split(';', self.data)        

        answer = 'Результат выполнения команд: \n'
        for i in range(len(command_list)):
            command_list[i] = " ".join(command_list[i].split())
            self.command = command_list[i]
            if len(command_list[i]) == 0:
                try:
                    len(command_list[i+1])
                    return "zОшибка. Дублируется \';\'f;;f1"
                except:    
                    continue
            answer += self.command_processing(command_list[i])
            if answer.find("z") > -1:
                break

        if answer.find("z") == -1:             
            for item in memory.keys():
                answer += item + " = " + str(memory[item]) + " "
              
        if answer.find("z") > -1:
            if answer.find('f1') > -1:
                answer = answer[answer.find("z"):answer.find('f1')+2]
            else:
                answer = answer[answer.find("z"):answer.find('f')+1]    

        return  answer


    


if __name__ == '__main__':
    #print(check_for_errors('Программа 42:а455 = [[455 + 3]] + 350 конец'))    
    #a = Check('Программа Ввод 42:А565 = [(61)] + а5 конец')
    a = Check('Программа Ввод 55 :А565 = 5 / 5; ввод 55 : ф455 =а565 + 5 ; ввод 6: к666 = ([7) + а565] + ф455 + 100 конец')
    #a = Check('Программа ввод 42:а455 = 455 + 3 + ~350; ввод 55:ы222 = [а455+4] + 5 ; конец')
    #a = Check('Программа ввод 42: а666 = s   конец')
    print(a.check_for_errors())
