#crear una calculadora 
#operaciones
opcion = ""
while opcion != "q":
    opcion = input( "escoje por favor una de las opciones:\n\
        suma = 1\n\
        resta = 2\n\
        multiplicacion = 3\n\
        divicion = 4\n\
        salir = q\n\
        :")
    if (opcion != "q"):
        #numero uno 
        numero1 =float( input( "\n\
        ingresa el primer numero: ") )

        #numero dos 
        numero2 =float( input("\n\
        ingresa segundo numero: ") )

    resultado = float(0)
    if (opcion == "1"):
        resultado = numero1 + numero2
        print("\n\
        el resultado es:", resultado, "\n\
                " )
    elif (opcion == "2"):
        resultado = numero1 - numero2
        print("\n\
        el resultado es:", resultado, "\n\
                " )
    elif (opcion == "3"):
        resultado = numero1 * numero2
        print("\n\
        el resultado es:", resultado, "\n\
                " )
    elif (opcion == "4"):
        if (numero2 == 0 ):
            print("\n\
            no se puede dividir entre 0")
        else:
            resultado = numero1 / numero2
            print("\n\
            el resultado es:", resultado, "\n\
                " )
    elif (opcion=="q"):
        print( "gracias por utilizar.")
        quit()
    else:
        print("no es una opcion correcta")

