print("Bienvenido a Mamá Juana")
total_pizzas = int(input("Cuántas pizzas desea ordenar: "))
if total_pizzas > 0:
    precio_pizza = 0
    total_cantidad_ingredientes = 0
    for pizza in range(1, total_pizzas + 1):
        subtotal = 1000
        cantidad_ingredientes = int(input("Ingrese la cantidad de ingredientes de su pizza " + str(pizza) + " : "))
        total_cantidad_ingredientes = total_cantidad_ingredientes + cantidad_ingredientes
        print("1.- Tomate $300")
        print("2.- Piña $500")
        print("3.- Pepperoni $400")
        print("4.- Aceitunas $600")
        for ingrediente in range(1, cantidad_ingredientes + 1):
            ingrediente_seleccionado = int(input("Ingrese el ingrediente " + str(ingrediente) + " : "))
            while ingrediente_seleccionado > 4:
                print("Por favor, ingrese un ingrediente valido.")
                ingrediente_seleccionado = int(input("Ingrese el ingrediente " + str(ingrediente) + " : "))
            if ingrediente_seleccionado == 1:
                subtotal = subtotal + 300
            elif ingrediente_seleccionado == 2:
                subtotal = subtotal + 500
            elif ingrediente_seleccionado == 3:
                subtotal = subtotal + 400
            elif ingrediente_seleccionado == 4:
                subtotal = subtotal + 600
        print("Subtotal $ " + str(subtotal))
        precio_pizza = precio_pizza + subtotal
    if total_cantidad_ingredientes % 2 == 0 and total_pizzas % 2 ==0:
        print('Su compra tiene un 10 % de descuento')
        precio_pizza = int(precio_pizza - (precio_pizza/10))
        print('Total: ' + str(precio_pizza))
    else:
        print("Total: " + str(precio_pizza))