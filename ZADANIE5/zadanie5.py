import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Generowanie wartości x i y przy użyciu eval()
    # Rysowanie wykresu ale bez show()
    f_str, p=wejscie.split(',')
    minx, maxx=map(float,p.strip().split())
    x_val=np.linspace(minx, maxx, 10)
    y_val=np.array([eval(f_str, {"x": x, "sin": np.sin, "cos": np.cos}) for x in x_val])

    plt.plot(x_val, y_val, label='eval + numpy', linestyle='--', color='blue')
    plt.title(f"Wykres funkcji (eval): {f_str}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    # Zwracanie wartości na granicach przedziału
    return y_val[0], y_val[-1]

# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Definicja symbolu i konwersja do funkcji numerycznej za pomocą SymPy
    # Generowanie wartości x i y przy użyciu funkcji numerycznej
    # Rysowanie wykresu ale bez show()
    f_str, p=wejscie.split(',')
    minx, maxx=map(float,p.strip().split())
    x=symbols("x")
    w=sympify(f_str)
    f=lambdify(x, w, modules=['numpy'])
    x_val=np.linspace(minx, maxx, 10)
    y_val_sympy=f(x_val)
    plt.plot(x_val, y_val_sympy, label='SymPy + lambdify', linestyle='-', color='red')
    plt.title(f"Wykres funkcji (SymPy): {f_str}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # Zwracanie wartości na granicach przedziału
    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.show()
