from clases.areas import  Area

def main():
   calculo = Area()
   print("El area del triangulo es: ",calculo.triangulo(3,4))
   print("El area del rectangulo es: ",calculo.rectangulo(3,4))
   print("El area del circulo es: ",calculo.circulo(3))
   
if __name__ == "__main__":
    main()