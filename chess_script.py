 
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
    mass1 = st1.split()
    mass2 = st2.split()

    final_mass = []
    
    if (len(mass1)==0 or len(mass2) == 0):
        return 'Строка пуста'

    final_mass = fill_final_mass(mass1, mass2)       
    
    return " ".join(final_mass)
    

if __name__=='__main__':
    print(Combine('11            8 9                         ', 'aaa 12x sdd ssss 333'))