# Pedir el saldo inicial
saldo = float(input("Ingrese su saldo inicial: "))

# Bucle para repetir el menú
while True:
    print("\nCajero Automático")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Elija una opción: ")

    # Consultar saldo
    if opcion == "1":
        print("Su saldo es: $", saldo)
    
    # Depositar dinero
    elif opcion == "2":
        deposito = float(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo = saldo + deposito
            print("Depósito exitoso. Nuevo saldo: $", saldo)
        else:
            print("Error: El monto debe ser mayor a 0.")

    # Retirar dinero
    elif opcion == "3":
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > 0:
            if retiro <= saldo:
                saldo = saldo - retiro
                print("Retiro exitoso. Nuevo saldo: $", saldo)
            else:
                print("Error: No tiene suficiente saldo.")
        else:
            print("Error: El monto debe ser mayor a 0.")

    # Salir del programa
    elif opcion == "4":
        print("Gracias por usar el cajero automático.")
        break

    # Opción incorrecta
    else:
        print("Opción no válida, intente de nuevo.")
