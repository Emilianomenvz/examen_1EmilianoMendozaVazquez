from clases import  areas  

def main():

    base_t, altura_t = 10, 5
    print(f"Área del triángulo ({base_t}, {altura_t}):", areas.trian(base_t, altura_t))

    base_r, altura_r = 8, 4
    print(f"Área del rectángulo ({base_r}, {altura_r}):", areas.rectangulo(base_r, altura_r))

if __name__ == "__main__":
    main()