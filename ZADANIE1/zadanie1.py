def dodaj_element(wejscie):
    # może warto zdefiniować zagnieżdżoną funkcję
    dl=0
    wyn=[]
    def szukana(a,b):
        nonlocal dl, wyn
        if isinstance(a,list):
            if b>dl:
                dl=b
                wyn=[a]
            elif b==dl:
                wyn.append(a)
            for i in a:
                szukana(i,b+1)

        elif isinstance(a, tuple):
            for i in a:
                szukana(i,b+1)
                
        elif isinstance(a, dict):
            for i in a.values():
                szukana(i,b)
                
    szukana(wejscie, 1)

    for i in wyn:
        i.append(max(i) + 1 if i else 1)
    return wejscie

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)   