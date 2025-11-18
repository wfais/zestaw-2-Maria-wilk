tab=[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
    (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
dane={y: x for x, y in tab}

def rzymskie_na_arabskie(rzymska):
    wartosc=0
    i=0
    while(i<len(rzymska)):
        if(i+1<len(rzymska) and rzymska[i:i+2] in dane):
            wartosc+=dane[rzymska[i:i+2]]
            i+=2
        else:
            wartosc+=dane[rzymska[i]]
            i+=1
    return wartosc

def arabskie_na_rzymskie(arabskie):
    wartosc=''
    while arabskie>0:
       for i,j in tab:
           while arabskie>=i:
               wartosc+=j
               arabskie-=i
    return wartosc
 
if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska=1994
        if not (1<=arabska<=3999):
            raise ValueError("Liczba musi być w zakresie 1-3999")
        else:
            print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
