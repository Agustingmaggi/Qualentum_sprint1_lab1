def sumar(a, b):
 return a + b

def restar(a, b):
 return a - b

def multiplicar (a,b):
 return a*b

def dividir(a, b):
    if b == 0:
        print("No se puede dividir por 0.")
    else:
        return a / b
 

if __name__ == "__main__":
 print(sumar(5, 3))
 print(restar(6,1))
 print(multiplicar(8,7))
 print(dividir(22,0))
 print(dividir(22,2))