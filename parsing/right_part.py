import parsing as pr
import re
from collections import deque

def all_scob(data:str):
    result1 = len(re.findall('\[', data)) == len(re.findall('\]', data))
    result2 = len(re.findall('\(', data)) == len(re.findall('\)', data))
    if not result1 or not result2:
        return False
    return result1 == result2   

def right_calculate(data:str, memory:dict):
    pairs = {'(':')', '[':']'}
    pairs_keys = {')':'(', ']':'['}
    data = " ".join(data.split())
    k = 0
    #замена переменных если есть
    new_data = ''  
    regex_alowed = '[\s|\+|\-|\*|\/|\&|\||\)|\]|\(|\[|\~|\d]'  
    regex_after_perem = '\s|\+|\-|\*|\/|\&|\||\)|\]'
    regex_operators = '\+|\-|\*|\/|\&|\|'                          
    regex_start_with = '^[\-|\(|\[|а-я|\d|\~]'
    if not re.search(regex_start_with, data):
        if data[0] == '=':
            return f"zОшибка. Дублируется \'{data[0]}\'f"
        return f"zОшибка. Выражение не может начинаться с \'{data[0]}\'f"      
    m = re.search(f'[\(|\[][{regex_operators}]', data)
    if m:
        if m.group(0)[1] != '-':
            return f"zОшибка. После открывающей скобки не может идти операция \'{m.group(0)[1]}\'f"
        m = re.search(f'[{regex_operators}][\)|\]]', data)
    if m:
        return f"zОшибка. Перед закрывающей скобкой не может идти операция \'{m.group(0)[0]}\'f"   
    stack = deque()
    string_inside = ''
    for i in range(len(data)):
        if data[i] == '[':
            try:
                memory['glubina'] +=1
                if memory['glubina'] > 3:
                    return "zОшибка. Глубина вложенности у квадратных скобок - 2f"
            except:
                memory['glubina'] = 1      
        if pairs.get(data[i]):
            stack.append(data[i])
            if len(stack) > 1:
                string_inside += data[i]
            continue
        elif data[i] in pairs.values():
            try:
                if (pairs[stack.pop()] == data[i]):
                    if len(stack) > 0:
                        string_inside += data[i]
                        continue
                    if len(string_inside) == 0 or len(string_inside) ==2 and len(re.findall('\[\]|\(\)', string_inside)) == 1:
                        return 'zОшибка. В скобках ничего нет.f'
                    new_data += right_calculate(string_inside, memory)
                    string_inside = ''
                else:
                    if all_scob(data):
                        return "zСкобки пересекаютсяf"
                    return f"zОтсутствует открывающая скобка \'{pairs_keys[data[i]]}\'f"    
                continue
            except:
                return f"zОтсутствует открывающая скобка \'{pairs_keys[data[i]]}\'f"
        elif len(stack)>0:
            string_inside += data[i]
            continue 
        if k > 0:
            k-=1
            continue 
        if data[i].isspace():
            continue
        #замена переменной
        if data[i].isalpha():
            if not re.search('[а-я]', data[i]):
                return f"zОшибка. Недопустимый символ \'{data[i]}\'f"
            perem = data[i:i+5]
            if len(perem) < 5:  
                m = re.search('[а-я][0-7][0-7][0-7]', perem)  
                if not m:
                    return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f"
                try:
                    new_data += str(memory[perem])
                    break
                except:
                    return f"zОшибка. Переменная {perem} не объявлена.f"   
            elif len(perem) == 5:
                m = re.search(f'[а-я][0-7][0-7][0-7][{regex_after_perem}]', perem)  
                if not m:
                    return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f"
                try:
                    if data[i+4].isdigit() or data[i+4].isspace() and data[i+5].isdigit():
                        return "zОшибка. После переменной не может идти числоf"    
                    perem = perem[0:4]
                    new_data += str(memory[perem])
                    k = 3
                    continue
                except:
                    return f"zОшибка. Переменная {perem} не объявлена.f"  
        #работа с круглыми скобками                         

        #     if data.rfind(")") > -1 and data.rfind(')') > i:
        #         string_inside = right_calculate(data[i+1:data.rfind(')')], memory)
        #         if string_inside.find('z') > -1:
        #             return string_inside
        #         new_data += f"({string_inside})"    
        #         k =  data.rfind(')') - i
        #         continue      
        #     else:
        #         return "zОшибка. Отсутствует закрывающая скобка \')\'f"
        # if data[i] == ')':
        #      return "zОшибка. Отсутствует открывающая скобка \'(\'f" 
        # if data[i] == '[':
        #     if data.rfind("]") > -1 and data.rfind(']') > i:
        #         try:
        #             memory['glubina'] +=1
        #             if memory['glubina'] > 2:
        #                 return "zОшибка. Глубина вложенности у квадратных скобок - 2f"
        #         except:
        #             memory['glubina'] = 1  
        #         string_inside = data[i+1:data.rfind(']')]                   
        #         string_inside = right_calculate(string_inside, memory)
        #         if string_inside.find('z') > -1:
        #             return string_inside
        #         new_data += f"({string_inside})"    
        #         k =  data.rfind(']') - i
        #         continue 
        #     else:
        #         return "zОшибка. Отсутствует закрывающая скобка \']\'f"
        # if data[i] == ']':
        #      return "zОшибка. Отсутствует открывающая скобка \'[\'f" 
        if data[i] == '~':
            if i != len(data)-1:
                if data[i+1] == " ":
                    m = re.search(regex_operators, data[i+2])
                    if m:
                        return f"zОшибка. \'~\' не может стоять перед оператором {data[i+2]}.f"
                else:
                    m = re.search(regex_operators, data[i+1])
                    if m:
                        return f"zОшибка. \'~\' не может стоять перед оператором \'{data[i+1]}\'.f"        
            else: 
                return "zОшибка. Выражение не может заканчиваться на \'~\'f"
        if not data[i].isdigit() and not data[i].isalpha():
            if re.search(regex_operators, data[i]):
                if i != len(data)-1:
                    if data[i+1] == " ":
                        if re.search(regex_operators, data[i+2]):
                            return "zОшибка. Две операции не могут идти друг за другом.f"
                    else:
                        if re.search(regex_operators, data[i+1]):
                            return "zОшибка. Две операции не могут идти друг за другом.f"       
                else:
                    return f"zОшибка. Операция {data[i]} не может стоять в конце выражения.f"    
            elif data[i] != '~': 
                return f"zОшибка. Недопустимый символ \'{data[i]}\'f"    
        if data[i].isdigit():
            if int(data[i])> 7:
                return f"zОшибка. Цифра {data[i]} не в восьмеричной системе.f" 
            if i != len(data)-1:
                if data[i+1] == " ":
                    if data[i+2].isdigit():
                        return f"zОшибка. Два чила не могут идти друг за другом.f"       
        
        new_data += data[i]        
    try:
        del memory['glubina']
    except:
        pass
    if len(stack) > 0:
        # print(all_scob(data))
        return f"zОтсутствует закрывающая скобка \'{pairs[stack.pop()]}\'f"
    if new_data.find("z") == -1:
        try:
            return str(int(eval(new_data)))
        except ZeroDivisionError:
            return "zОшибка. Деление на 0f"  
              
    return new_data

