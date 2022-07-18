
def fill_the_mass(string):
    mass = []
    while (string.find(" ") != -1):
        mass.append(string[0:string.find(" ")])
        string = string[string.find(" ")+1:len(string)]
    mass.append(string[0:len(string)])    
    return mass    

def fill_final_mass(mass1, mass2):
    final_mass = []
    count = 0
    for i in range (len(mass2)):
        try:
            final_mass.append(mass1[i])
            final_mass.append(mass2[i])
            count +=1   
        except Exception:
            del mass2[0:count]
            final_mass = final_mass + mass2 
            return final_mass        
    del mass1[0:count]     
    final_mass = final_mass + mass1 
    return final_mass

def Combine(st1, st2):
    st1 = " ".join(st1.split())
    st1 = st1.strip()
    st2 = " ".join(st2.split())
    st2 = st2.strip()
    
    mass1 = fill_the_mass(st1)
    mass2 = fill_the_mass(st2)

    final_mass = []
    
    if (len(mass1)==0 or len(mass2) == 0):
        return 'Строка пуста'

    final_mass = fill_final_mass(mass1, mass2) 

    final_string = ''
    for item in final_mass:
        final_string += item + " "      
    
    return final_string
    

if __name__=='__main__':
    print(Combine('11111 2222 333 4 5555 6666', 'aaa 12x sdd ssss 333'))