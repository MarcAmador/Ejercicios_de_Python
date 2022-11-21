print("1.-Tabla de multiplicacion");
print("2.-Mostrar listado de numeros impares");
print("3.-Mostrar los multiplos de un numero (1-100)");
print("4.-Salir");

opt=int(input("Ingrese una opcion: "));

if(opt==1):
    num = int(input("Ingrese un numero entero: "));
    if (num < 0):
        num *= -1;
    start=int(input("Ingrese la posicion inicial "));
    end=int(input("Ingrese la posicion final "));
    print("***TABLA DE MULTIPLICACION DEL ",num,"***");
    for n in range (start,end+1):
        print(num," * ",n," = ", num*n);

elif(opt==2):
    num=int(input("Ingrese un numero entero: "));
    print("");
    print("Lista de numeros impares del 1 al ", num);
    for i in range (1,num,2):
        print(i);
elif(opt==3):
    num=int(input("Ingrese un numero entero: "));
    if(num<0):
        num *= -1;
    print("");
    print("Lista de numeros multiplos de ",num,"(1-100)");
    for j in range (1,100):
        if(j%num==0):
            print(j);
else:
    print("Hasta pronto!");