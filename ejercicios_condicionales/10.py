#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
#y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
#Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
#Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.





print("Bienvenido pizzeria napoli tenenos estos tipo de pizza \n 1-Vegetarian \n 2-No_Vegetariana")
tipo = input("introdce el tipo de pizza que quieres: ")

if tipo == "1" :
    print("Ingrese con que ingrediente \n 1-Pimiento \n 2-Tofu ")
    ingrediente = input("Ingrese el tipo de ingrediente: ")
    print("Pizza vegetariana con mozarela , tomate y", end="")
    if ingrediente ==  "1":
        print("Pimiento")
    else :
        print("Tofu")    
    
else:
    print("Ingrese con que ingrediente \n 1-Peperoni \n 2-Jamon \n 3-Salmon") 
    ingrediente = input("Ingrese el tipo de ingerediente ") 
    print("Pizza no vegetariana con mozarela , tomate y", end="")
    if ingrediente  == "1" :
        print("Peperoni")      
    elif ingrediente == "2" :
        print("Jamon")
    else :
        print("Salmon")        
        
        
    