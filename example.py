"""testeando teclado al praecer algunas teclas aun estan muy duras segur
    que  con ele tiempo podre   acostumbrarme asi que debo seguir trabajando 
    """

autos = ['bbb','xxx','aaa','ddd','bmw']
autos.sort() 
for nuevo in autos:
    if nuevo == 'bmw':
        print(f"El auto es: {nuevo.upper()}.")
    else:
        print(f"Los autos son: {nuevo.title()}.")
print("se acabo")

# La exclamacion ! significa not por lo tanto 
    # != no son iguales  
casa = 'Verde'
if casa != 'rojo': # si casa no es igual a rojo entonces 
    #   si los valores no coinciden entonces retorna true 
    #   entonces ejecuta el codido siguiente a if   
    print("la casa no es verde")    #imprime esto


food = ['Apple','orange','carrot']
food1 = 'apple'
print( food1 not in food)


available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in  requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding topping: {requested_topping}")
    else:
        print(f"We dont have the topic {requested_topping}")
print("Your order is ready!!")