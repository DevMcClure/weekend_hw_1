# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    return shop_name ["name"]


def get_total_cash(total):
    return total ["admin"]["total_cash"]


def add_or_remove_cash(pet_shop,number):
    pet_shop ["admin"] ["total_cash"] += number


def get_pets_sold(pet_shop):
    return pet_shop ["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, number):
    pet_shop ["admin"]["pets_sold"] += number


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    breed_count = []
    
    for pet_breed in pet_shop["pets"]:
        if pet_breed["breed"] == breed:
            breed_count.append(pet_breed)
    return breed_count 


def find_pet_by_name(pet_shop, animal_name):
    pet_name = None

    for name in pet_shop["pets"]:
        if name ["name"] == animal_name:
            pet_name = name
    return pet_name     


def remove_pet_by_name(shop, name):
    pets = shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            del pets[pets.index(pet)]



def add_pet_to_stock(pet_shop, new_pet):
   pet_shop ["pets"].append(new_pet)



 
           
def get_customer_cash(customers):
    return customers ["cash"]    


def remove_customer_cash(customer,number):
    customer["cash"] -= number


def get_customer_pet_count(customers):
    pet_count = customers["pets"]
    return len(pet_count)


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    add_pet = customer["pets"]
    return len(add_pet)






def customer_can_afford_pet(customer, new_pet):
    afford = True
    cant = False

    if customer ["cash"] >= new_pet ["price"]:
        return afford
    elif customer ["cash"] <= new_pet ["price"]:
        return cant
    elif customer ["cash"] == new_pet ["price"]:
        return afford   








              

    

    

         



    