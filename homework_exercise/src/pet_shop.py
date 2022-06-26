# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, amount_change):
    shop["admin"]["total_cash"] += amount_change

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, amount_change):
    shop["admin"]["pets_sold"] += amount_change

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    breed_pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            breed_pets.append(pet)
    return breed_pets