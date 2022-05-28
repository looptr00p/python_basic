# Tu cajero debe pedir un usuario y una clave para ingresar. Al principio debe tener 1.000.000 como saldo inicial. 
# Tu cajero debe dejar ingresar al usuario 10334151 con la clave 1803, quien tiene al inicio del programa 100.000 en su cuenta. 
# Lo único que se puede hacer en este nivel es retirar dinero de la cuenta corriente. 
# Tu programa debe validar la clave y el monto a retirar, indicando el mensaje “clave invalida” 
# cuando la clave no corresponde y al tercer intento fallido debe indicar “tarjeta bloqueada” y salir del programa. 
# Si la clave es válida, debe preguntar por el monto a retirar. 
# Cuando se hace el retiro de un monto que no es válido debe indicar “monto no permitido”, 
# si el monto se puede retirar debe actualizar los saldos e imprimir el nuevo saldo que quedó en la cuenta corriente 
# y el cajero, por ejemplo al retirar 45.000 debiera imprimir:

#     saldo cuenta=55000
#     saldo cajero=955000

# Tu programa debe repetirse continuamente, para salir la persona debe ingresar algo distinto a la letra “N”.

saldo_cajero = 1000000
saldo_usuario = 100000
intento = 0
letra_continuar = 'N'
usuario = input("usuario: ")
clave = input("contraseña: ")
while letra_continuar.upper() == 'N':
    if (clave == '1803' and usuario == '10334151'):
        monto_retiro = int(input("monto de retiro: "))
        if monto_retiro > saldo_usuario or monto_retiro > saldo_cajero:
            print("monto no permitido")
        else:
            saldo_cajero -= monto_retiro
            saldo_usuario -= monto_retiro
            print(['saldocuenta=' + str(saldo_usuario), 'saldo cajero=' + str(saldo_cajero)])
            letra_continuar = input('para continuar presione la letra "N": ')
    else:
        intento += 1
        if intento >= 3:
            print("tarjeta bloqueada")
            letra_continuar = 'L'
        else:
            print("clave invalida")
            usuario = input("usuario: ")
            clave = input("clave: ")
