


digits = {'un' : 1, 'deux' : 2, 'trois' : 3, 
'quatre': 4, 'cinq':5, 'six':6, 'sept':7,'huit':8, 'neuf':9, 'dix':10, 
'onze':11, 'douze':12, 'treize':13, 'quatorze':14, 'quinze':15, 
'seize':16, 'dix-sept':17, 'dix-huit':18, 'dix-neuf':19, 'vingt':20,
'trente':30, 'quarante':40, 'cinquante':50, 'soixante':60,
'cent':100}

def to_rim(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result

def razryad(a):
    k = 0
    while (a>0):
        k +=1
        a //=10
    return k    

def razryad_to_str(l):
    if l == 1:
        return 'числа единичного формата'
    elif l == 2:
        return 'числа десятичного формата'
    elif l == 3:
        return 'cent'
def razryad_to_str2(l):
    if l == 1:
        return 'число единичного формата'
    elif l == 2:
        return 'число десятичного формата'
    elif l == 3:
        return 'cent'                   


def to_dig(string):
    words=string.split()
    words = [word.lower() for word in words]

    for word in words:
        if (digits.get(word) == None):
            return 'Лексическая ошибка. Слова ' + word + ' не существует'

    numbers = []
    for word in words:
        numbers.append(digits.get(word))


    if len(numbers) > 0:
        if razryad(numbers[0]) == 1:
            if len(numbers) == 1:
                return str(numbers[0]) + ' ' + str(to_rim(numbers[0]))
            else:
                if razryad(numbers[1]) == 3:
                    if len(numbers) > 2:
                        for i in range(2,len(numbers)):
                            if razryad(numbers[i-1]) <= razryad(numbers[i]) and numbers[i] != 20 and numbers[i-1] != 4:
                                return 'Синтаксическая ошибка. После ' + razryad_to_str(razryad(numbers[i-1]))+ ' не может идти ' + razryad_to_str2(razryad(numbers[i]))        
                        if razryad(numbers[2]) != 3:
                            if (razryad(numbers[2]) == 2):
                                if len(words) == 3:
                                    num = numbers[0] * numbers[1] + numbers[2]
                                    return str(num) + ' ' + str(to_rim(num))
                                else:
                                    if len(words) == 4:
                                        if numbers[2] > 19:
                                            if razryad(numbers[3]) == 1:
                                                num = numbers[0] * numbers[1] + numbers[2] + numbers[3]
                                                return str(num) + ' ' + str(to_rim(num))
                                            else: 
                                                return 'Синтаксическая ошибка в словах ' + words[2] + ' ' + words[3] +'. После ' + razryad_to_str(razryad(numbers[2]))+ ' не может идти ' + razryad_to_str2(razryad(numbers[3])) 
                                        else: 
                                            return 'Синтаксическая ошибка в словах ' + words[2] + ' ' + words[3] +'. После ' + razryad_to_str(razryad(numbers[2])) + ' не может идти ' + razryad_to_str2(razryad(numbers[3]))
                                    else:
                                        if razryad(numbers[3]) == 1: 
                                            return 'Синтаксическая ошибка. После ' + razryad_to_str(razryad(numbers[3])) + ' не должно идти ' + razryad_to_str2(razryad(numbers[4]))
                                        elif razryad(numbers[3]) == 2:
                                            return 'Синтаксическая ошибка. После ' + razryad_to_str(razryad(numbers[3])) + ' не может идти ' + razryad_to_str2(razryad(numbers[3]))
                                        elif razryad(numbers[2]) == 3:
                                            return 'Синтаксическая ошибка. После ' + razryad_to_str(razryad(numbers[3])) + ' не может идти ' + razryad_to_str2(razryad(numbers[3]))                       
                            elif razryad(numbers[2])==1:
                                if len(words) == 3:
                                    num = numbers[0] * numbers[1] + numbers[2]
                                    return str(num) + ' ' + str(to_rim(num))
                                elif numbers[2] == 4 and numbers[3] == 20 :
                                    if len(words) == 4:
                                        num = numbers[0] * numbers[1] + 80
                                        return str(num) + ' ' + str(to_rim(num))
                                    if len(words) == 5:
                                        if razryad(numbers[4]) == 1:
                                            num = numbers[0] * numbers[1] + 80 + numbers[4]
                                            return str(num) + ' ' + str(to_rim(num))
                                        else:    
                                            return 'Синтаксическая ошибка в словах quatre vingt ' +' '+ words[4] +'. После чисел десятичного формата могут идти только числа единичного формата.'
                                    else:
                                        if len(words) > 5:
                                            if razryad(numbers[4]) == 1:
                                                return 'Синтаксическая ошибка. После ' + razryad_to_str(razryad(numbers[4])) + ' не может идти ' + razryad_to_str2(razryad(numbers[5]))
                                        else:
                                            return 'Синтаксическая ошибка. После чисел десятичного формата не могут идти ' + razryad_to_str(razryad(numbers[4]))
                                elif razryad(numbers[2]) == 1: 
                                    if len(words) == 3:
                                        num = numbers[0] * numbers[1] + numbers[3] 
                                        return str(num) + ' ' + str(to_rim(num))
                                    else:
                                        return 'Синтасическая ошибка. После ' + razryad_to_str(razryad(numbers[2])) + ' не может идти ' + razryad_to_str2(razryad(numbers[3]))      
                        else: 
                            return 'Синтаксическая ошибка в словах ' + words[1] + ' '+ words[2] +'. После сотен не могут идти сотни'   
                    else:
                        num = numbers[0] * numbers[1]  
                        return str(num) + ' ' + str(to_rim(num))

                else:
                    if numbers[0] == 4 and numbers[1] == 20:
                        if len(words) == 2:
                            return '80 ' + str(to_rim(80))
                        elif len(words) == 3:
                            if razryad(numbers[2]) == 1:
                                num = 80 + numbers[2]
                                return str(num) + ' ' + str(to_rim(num))
                            elif razryad(numbers[2]) == 2:
                                return 'Синтаксическая ошибка в ' + words[0]+ ' ' + words[1] + ' и ' + words[2] + '. После десятков не могут идти десятки'    
                            elif razryad(numbers[2]) == 3:
                                 return 'Синтаксическая ошибка в ' + words[0]+ ' ' + words[1] + ' и ' + words[2] + '. После десятков не могут идти сотни'        
                        elif len(words) > 3:
                            return 'Синтаксическая ошибка. Лишние слова.'        
                    elif razryad(numbers[1]) == 2: 
                        return 'Синтаксическая ошибка в словах ' + words[0] + ' ' + words[1] +'. После числа единичного формата не может идти число десятичного формата'
                    else:
                        return  'Синтаксическая ошибка в словах ' + words[0]+ ' ' + words[1] +'. После числа единичного формата не может идти число единичного формата'           
        elif razryad(numbers[0]) == 2:
            if len(words) == 1: 
                return str(numbers[0]) + ' ' + str(to_rim(numbers[0]))
            elif len(words) == 2 and numbers[0] > 19:
                if razryad(numbers[1]) == 1:
                    num = numbers[0] + numbers[1]
                    return str(num) + ' ' + str(to_rim(num))
                elif razryad(numbers[1]) == 2:
                    return 'После числа десятичного формата не может идти число десятичного формата'
                elif razryad(numbers[1]) == 3:
                    return 'После числа десятичного формата не могут идти сотни'
            elif razryad(numbers[0]) !=2 and len(words)>1:
                return 'После ' + razryad_to_str(razryad(numbers[0]))+ ' не может идти ' + razryad_to_str2(razryad(numbers[1]))     
            elif len(words) > 2:
                if razryad(numbers[1]) == 1 and numbers[0] > 19:
                    return 'После ' + razryad_to_str(razryad(numbers[1]))+ ' не может идти ' + razryad_to_str2(razryad(numbers[2]))
                else: 
                    return 'После ' +razryad_to_str(razryad(numbers[0]))+ ' не может идти ' + razryad_to_str2(razryad(numbers[1]))
        elif razryad(numbers[0]) == 3:
            if len(words) == 1:
                return str(numbers[0]) + ' ' + str(to_rim(numbers[0]))
            elif len(words) == 2:
                if razryad(numbers[1]) != 3:
                    num = numbers[0] + numbers[1]
                    return str(num) + ' ' + str(to_rim(num))
                else:
                    return 'После сотни не может идти сотня'
            elif len(words) == 3:
                if razryad(numbers[1]) == 2 and razryad(numbers[2]) == 1 and numbers[1] > 19:
                    num = numbers[0] + numbers[1] + numbers[2]
                    return str(num) + ' ' + str(to_rim(num))
                else:
                    return 'Синтаксическая ошибка. После ' + razryad_to_str(razryad(numbers[1])) + ' не может идти ' + razryad_to_str2(razryad(numbers[2]))               
    else:
        return 'Строка пуста'                

                  

    
                                                     
                 


if __name__=='__main__':
    print(to_dig('quarante quatre'))