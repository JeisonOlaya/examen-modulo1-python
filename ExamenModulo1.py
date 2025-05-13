products = {}   #here I create at the diccionarity

def menu():     #here I creaet at the menu, where you find all the options
    print("BIENVENIDO AL INVENTARIO")
    print("\n=====MENU DE OPCIONES=====\n")
    print("1.)Añadir producto")
    print("2.)Consultar Producto")
    print("3.)Actualizar producto")
    print("4.)Eliminar producto")
    print("5.)Calcular el valor total del inventario")

    return int(input("\nPor Favor selecciona una opcion: \n"))

DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"


def case1():
    print("\n---AGREGAR PRODUCTO---\n") #here star the option namber 1
    
    for i in range(5):
        nameproduct = input(f"\nPor favor ingresa el nombre del producto {i+1}: ") # ask for 5 products, name, price and quantity
        price = float(input("Por favor ingresa el precio del producto: "))
        quantity = int(input("Por favor ingresa la cantidad del producto: "))
        
        products[nameproduct] = {   #here all the atribut its save on diccioarity
            "price": price,
            "quantity": quantity
        }
        print(SUCCESS + f"Producto '{nameproduct}' agregado correctamente." + RESET)
def case2():
    print("\n---CONSULTAR PRODUCTO---\n")   #here star the option namber 1
    search_name = input("Por favor ingresa el nombre del producto que deseas consultar: ")
    
    if search_name in products: #here we can search the product that its save on the diccionarity
        print("\nInformación del producto:")
        print(f"Nombre: {search_name}")
        print(f"Precio: {products[search_name]['price']}")
        print(f"Cantidad: {products[search_name]['quantity']}")
        print(SUCCESS+"CONSULTA EXITOSA"+RESET)
    else:
        print(DANGER + "No se encontró el producto" + RESET)
def case3():
    while True:
        print("\n--- ACTUALIZAR PRODUCTO ---")  #here star the option namber 1
        if not products:
            print(DANGER+"No hay productos registrados."+RESET) #if you dont save anything product, this is the answer
            continue
        product_name = input("\nIngresa el nombre del producto a actualizar: ")

        if product_name in products:
            print("\nDeja en blanco los campos que no deseas cambiar")
            try:
                # Validation for the price (the prices its positive)
                new_price = input(f"Nuevo precio (actual: {products[product_name]['price']}): ")
                if new_price:
                    new_price = float(new_price)
                    if new_price <= 0:
                        print(DANGER+"Error: El precio debe ser un número positivo"+RESET)
                        continue
                    products[product_name]['price'] = new_price                    
                
                # Validation for the quantity (the quantity its positive)
                new_quantity = input(f"Nueva cantidad (actual: {products[product_name]['quantity']}): ")
                if new_quantity:
                    new_quantity = int(new_quantity)
                    if new_quantity < 0:
                        print(DANGER+"Error: La cantidad debe ser un número entero positivo"+RESET)
                        continue
                    products[product_name]['quantity'] = new_quantity
                    
                
                print(SUCCESS+f"Producto '{product_name}' actualizado correctamente."+RESET)
                break
            except ValueError:
               print(DANGER+"Error: Ingresa valores numéricos válidos"+RESET)
        else:
            print(DANGER+"Producto no encontrado"+RESET) 
def case4():
    print(WARNING +" Estas a punto de eliminar un usuario :O "+ RESET)
    if not products:
        print(WARNING+"Inventario vacio"+RESET)
    print("productos disponibles: ")
    for name in products.keys():
        print(f"-{name}")

    productname = input("Ingresa el nombre del producto a eliminar: ")
    if productname in products:
        confirm = input(f"Confirmas eliminar '{productname}'? (s/n)").lower()
        if confirm=='s':
            products.pop(productname)
            print(SUCCESS+"El producto fue eliminado exitosamente"+ RESET)
        else:
            print(SUCCESS+"eliminacion cancelada"+RESET)


def case5():
    print("\n--- VALOR TOTAL DEL INVENTARIO ---")
    if not products:
        print(DANGER+"No hay productos registrados."+RESET)

    total_value = 0
    print("\nDetalle del inventario:")
    for name, details in products.items():
        product_value = details['price'] * details['quantity']
        total_value += product_value
        print(f"{name}: {details['quantity']} x ${details['price']} = ${product_value}")
        
    print(SUCCESS+ f"\n VALOR TOTAL DEL INVENTARIO: ${total_value}"+RESET)  

def casenUll():
    print(DANGER+"\nOpción no válida. Por favor selecciona una opción del 1 al 4."+RESET)



menu1 = True

while menu1:
    answer = menu()

    match answer:
        case 1:
            case1()
            
        case 2:
            case2()
            
        case 3:
            case3()               

        case 4:
            case4()
        case 5:
            case5()

        case null:
            print("\n Opción no válida. Por favor selecciona una opción del 1 al 4.")