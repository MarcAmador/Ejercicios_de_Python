print("***EJEMPLO DE IF");
print("1.- Mayor de dos numeros");
print("2.- Mayor de tres numeros");
print("3.- Operador MOD (múltipos de 7)");
print("4.- Promedio y evaluación (Par/Impar)");
print("5.- TELEFONÍA");
print("6.- Salir");
opt=int(input("Ingrese una opción: "));

if (opt==1):
    n1 = int(input("Digite el primer numero: "));
    n2 = int(input("Digite el segundo numero: "));
    if (n1 > n2):
        mayor = int(n1);
        menor = int(n2);
    elif(n2 > n1):
        mayor = int(n2);
        menor = int(n1);
    else:
        print("Los numeros son iguales");

    print("El numero mayor es ",mayor," , el menor es ",menor);
    """opt = int(input("\n Menu\n ---------------------------\n\t" +
                           "1.- Mayor de dos numeros\n\t2.-Mayor de tres numeros\n\t3.- Operador MOD (múltipos de 7)\n\t4.- Promedio y evaluación (Par/Impar)\n\t5.- Salir\n\t" +
                           "Favor ingrese una opción :"));"""

elif(opt==2):
    n1 = int(input("Digite el primer numero: "));
    n2 = int(input("Digite el segundo numero: "));
    n3 = int(input("Digite el tercer numero: "));
    if (n1 > n2):
        mayor = int(n1);
    else:
        mayor = int(n2);

    if (n3 > mayor):
        mayor = int(n3);

    print("El mayor número es: ", mayor);

elif(opt==3):
    n1 = int(input("Digite el primer numero: "));
    n2 = int(input("Digite el segundo numero: "));
    n3 = int(input("Digite el tercer numero: "));
    prom=float(n1+n2+n3)/3;

    if(prom%7==0):
        mensaje="El promedio de los numeros ingresados es multiplo de siete";
        print(mensaje);
    else:
        mensaje="El promedio de los numeros ingresados NO es multiplo de siete";
        print(mensaje);

elif (opt == 4):
    n1 = int(input("Digite el primer numero: "));
    n2 = int(input("Digite el segundo numero: "));
    n3 = int(input("Digite el tercer numero: "));
    prom = int((n1 + n2 + n3) / 3);
    print(prom);

    if(prom%2 == 0):
        mensaje= "El promedio es par";
        print(mensaje);
    else:
        mensaje = "El promedio es impar";
        print(mensaje);

elif(opt == 5):
    nombre=str(input("Ingrese su nombre: "));
    nac = int(input("Minutos nacionales consumidos: "));
    inter = int(input("Minutos internacionales consumidos: "));
    total = int(nac+inter);
    if(total > 25):
        if(nac > 25):
            nac -= 25;
            pago= float((nac*0.5)+ (inter*2.5));
            print(nombre, "tu monto de pago mensual ascinde a: Q", pago);
        else:
            resto = 25 -nac;
            inter -= resto;
            pago = float(inter*2.5);
            print(nombre, " tu monto de pago mensual ascinde a: Q", pago);
    else:
        print(nombre, " tus minutos son gratis!!");
else:
    print("Hasta pronto");
