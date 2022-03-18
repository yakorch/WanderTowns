import my_game
import random
from itertools import combinations as comb

hours_left = 72
need_to_sleep = 2
dead = False
visited_towns = list()

def level_choose():
    print("Choose your difficulty level")
    print("'hard' - 2000 UAH, 'medium' - 2500 UAH, 'easy' - 3500 UAH")
    while True:
        level = input(">>> ")
        if level in ('hard', 'medium', 'easy'):
            break
        else:
            print("Try again :)")

    if level == "hard":
        amount = 2500
    elif level == "medium":
        amount = 3000
    elif level == "easy":
        amount = 3500

    return amount

character = my_game.Character(money=level_choose(), hours_hungry=4, walk_speed=5, happiness=50)

# goal is to vist all these towns in 72 hours with nice sleep, warmness, happiness.

all_hotels = [my_game.Hotel("BestTown", 300, happiness=10, breakfast=True),
              my_game.Hotel("QuitePlace", 250, happiness=5, breakfast=True),
              my_game.Hotel("Hehotel", 200, happiness=5, breakfast=False),
              my_game.Hotel("Cheap", 150, happiness=-10, breakfast=False),
              my_game.Hotel("Vata", 100, happiness=-15, breakfast=False)]

def create_vehicles():
    return  [my_game.Car("Volkswagen", 160, 10, give_happy=5),
                my_game.Car("Lada", 75, 9, give_happy= -10),
                my_game.Car("Porsche", 220, 16, give_happy=10),
                my_game.Car("Volvo", 120, 5, give_happy=-5),
                my_game.Bike("HarleyDavidson", 140, 12, give_happy=5),
                my_game.Bike("Yamaha", 110, 14, give_happy= -5),
                my_game.Bicycle("Bicycle", 25, 0)]

def create_gas_stations():
    stations = [my_game.GasStation("WOG", 35, 35),
                    my_game.GasStation("OKKO", 30, 25),
                    my_game.GasStation("UkrNafta", 28, 20),
                    my_game.GasStation("Stoppy", 32, 30)]
    stations = random.choice(list(comb(stations, 2)))
    return stations

def create_shops():
    all_items = [my_game.Food(name="water", price=20, satiety=2),
             my_game.Food(name="burger", price=50, satiety=4), 
             my_game.Food("free_potato", 40, 3), 
             my_game.Food("bread", 15, 2),
             my_game.Food("banana", 30, 2),
             my_game.Food("meat", 100, 6)]
    pairs = list(comb(all_items, 2))
    return [my_game.Shop("Rukavichka", list(random.choice(pairs))),
             my_game.Shop("ATB", list(random.choice(pairs))),
             my_game.Shop("Silpo", list(random.choice(pairs)))]


hotels_lviv = random.choice(list(comb(all_hotels, 2)))
shops_lviv = random.choice(list(comb(create_shops(), 2)))
gas_lviv = create_gas_stations()
gas_lviv[0].assign_vehicle(random.choice(create_vehicles()))
lviv = my_game.Town("Lviv", hotels_lviv, shops_lviv, gas_lviv)

hotels_drohobych = random.choice(list(comb(all_hotels, 2)))
shops_dro = random.choice(list(comb(create_shops(), 2)))
gas_dro = create_gas_stations()
gas_dro[0].assign_vehicle(random.choice(create_vehicles()))
drohobych = my_game.Town("Drohobych", hotels_drohobych, shops_dro, gas_dro)

hotels_ternopil = random.choice(list(comb(all_hotels, 2)))
shops_ter = random.choice(list(comb(create_shops(), 2)))
gas_ter = create_gas_stations()
gas_ter[0].assign_vehicle(random.choice(create_vehicles()))
best_town = my_game.Town("Ternopil", hotels_ternopil, shops_ter, gas_ter)

hotels_rivne = random.choice(list(comb(all_hotels, 2)))
shops_rivne = random.choice(list(comb(create_shops(), 2)))
gas_rivne = create_gas_stations()
gas_rivne[0].assign_vehicle(random.choice(create_vehicles()))
rivne = my_game.Town("Rivne", hotels_rivne, shops_rivne, gas_rivne)

hotels_zhytomyr = random.choice(list(comb(all_hotels, 2)))
shops_zhyto = random.choice(list(comb(create_shops(), 2)))
gas_zhyto = create_gas_stations()
gas_zhyto[0].assign_vehicle(random.choice(create_vehicles()))
zhytomyr = my_game.Town("Zhytomyr", hotels_zhytomyr, shops_zhyto, gas_zhyto)

hotels_lutsk = random.choice(list(comb(all_hotels, 2)))
shops_lutsk = random.choice(list(comb(create_shops(), 2)))
gas_lutsk = create_gas_stations()
gas_lutsk[0].assign_vehicle(random.choice(create_vehicles()))
lutsk = my_game.Town("Lutsk", hotels_lutsk, shops_lutsk, gas_lutsk)

hotels_vinnytsia = random.choice(list(comb(all_hotels, 2)))
shops_vinn = random.choice(list(comb(create_shops(), 2)))
gas_vinn = create_gas_stations()
gas_vinn[0].assign_vehicle(random.choice(create_vehicles()))
vinnytsia = my_game.Town("Vinnytsia", hotels_vinnytsia, shops_vinn, gas_vinn)

hotels_khmelnytskyi = random.choice(list(comb(all_hotels, 2)))
shops_khmel = random.choice(list(comb(create_shops(), 2)))
gas_khmel = create_gas_stations()
gas_khmel[0].assign_vehicle(random.choice(create_vehicles()))
khmelnytskyi = my_game.Town("Khmelnytskyi", hotels_khmelnytskyi, shops_khmel, gas_khmel)

hotels_ivano_frankivsk = random.choice(list(comb(all_hotels, 2)))
shops_ivano_f = random.choice(list(comb(create_shops(), 2)))
gas_ivanof = create_gas_stations()
gas_ivanof[0].assign_vehicle(random.choice(create_vehicles()))
ivano_frankivsk = my_game.Town("Ivano-Frankivsk", hotels_ivano_frankivsk, shops_ivano_f, gas_ivanof)








lviv.link_town(drohobych, 77)
lviv.link_town(lutsk, 150)
lviv.link_town(rivne, 210)
lviv.link_town(best_town, 129)
lviv.link_town(ivano_frankivsk, 134)

drohobych.link_town(best_town, 207)
drohobych.link_town(lviv, 77)
drohobych.link_town(ivano_frankivsk, 128)

lutsk.link_town(rivne, 73)
lutsk.link_town(lviv, 150)
lutsk.link_town(best_town, 167)
lutsk.link_town(ivano_frankivsk, 260)
lutsk.link_town(khmelnytskyi, 257)

best_town.link_town(ivano_frankivsk, 135)
best_town.link_town(drohobych, 207)
best_town.link_town(lviv, 129)
best_town.link_town(lutsk, 167)
best_town.link_town(rivne, 154)
best_town.link_town(khmelnytskyi, 112)
best_town.link_town(zhytomyr, 287)

ivano_frankivsk.link_town(lviv, 134)
ivano_frankivsk.link_town(drohobych, 128)
ivano_frankivsk.link_town(best_town, 135)
ivano_frankivsk.link_town(khmelnytskyi, 243)
ivano_frankivsk.link_town(vinnytsia, 367)
ivano_frankivsk.link_town(lutsk, 260)
ivano_frankivsk.link_town(rivne, 275)

rivne.link_town(lviv, 150)
rivne.link_town(lutsk, 73)
rivne.link_town(best_town, 154)
rivne.link_town(khmelnytskyi, 195)
rivne.link_town(zhytomyr, 188)
rivne.link_town(vinnytsia, 277)
rivne.link_town(ivano_frankivsk, 275)

khmelnytskyi.link_town(best_town, 112)
khmelnytskyi.link_town(ivano_frankivsk, 243)
khmelnytskyi.link_town(rivne, 195)
khmelnytskyi.link_town(lutsk, 257)
khmelnytskyi.link_town(vinnytsia, 120)
khmelnytskyi.link_town(zhytomyr, 189)

vinnytsia.link_town(khmelnytskyi, 120)
vinnytsia.link_town(zhytomyr, 129)
vinnytsia.link_town(rivne, 277)
vinnytsia.link_town(ivano_frankivsk, 367)

zhytomyr.link_town(best_town, 287)
zhytomyr.link_town(rivne, 188)
zhytomyr.link_town(khmelnytskyi, 189)
zhytomyr.link_town(vinnytsia, 129)



towns = [lviv, drohobych, lutsk, best_town, ivano_frankivsk, rivne, khmelnytskyi, vinnytsia, zhytomyr]
towns_str = [el.town for el in towns]
cur_town = random.choice(towns)

def rules_input():
    print("Possible options for input are 'hotel', 'shop', 'go', 'gas'. Second input - name of the object to interrupt with")


def character_attr():
    print()
    print(f"You have already visited {', '.join(visited_towns)}.")
    print(f"{hours_left} hours left, {character.money} UAH in charge.")
    print(f"You are {character.happiness} % happy, have food for {character.hours_hungry} hours")
    if need_to_sleep > 0:
        print(f"You need to sleep {need_to_sleep} time(s)")
    else:
        print("No need to sleep more")
    if character.vehicle is not None:
        print(f"You drive {character.vehicle} now, it has {character.vehicle.fuel_init} liters of fuel")
        print(f"Characteristics: fuel (l) consumption per 100 km - {character.vehicle.fuel_usage}, speed - {character.vehicle.speed}")

print(f"This is a game where you spawn in a random city. Now you are at {cur_town.town}")
print(f"You have {character.money} UAH, full for {character.hours_hungry} hours, and happy for {character.happiness} %.")
print(f"Visit all towns ({', '.join(towns_str)}) in {hours_left} hours and survive.\nYou can use different vehicles and must sleep at least two times")
rules_input()


def check_if_end():
    if character.is_dead():
        print("You died :(")
        return True

    if hours_left < 0:
        print("Time has expired, you lost")
        return True

    if character.vehicle is not None and character.vehicle.fuel_init < 0:
        print("The fuel has expired, it is a loss...")
        return True

    if len(set(visited_towns)) == 9 and need_to_sleep <= 0:
        print("Congratulations!!! You won!")
        return True

    if len(set(visited_towns)) == 9 and need_to_sleep > 0:
        print("You need to sleep more!", need_to_sleep, "time(s)")
        return False

    if len(set(visited_towns)) < 9:
        print(f"You need to visit {9 - len(set(visited_towns))} more town(s)")
        return False

    return False

while not dead:
    print()
    print()

    cur_town.get_details()
    character_attr()
    print()
    rules_input()
    to_do = input(">>> ")


    if to_do == "hotel":
        for hotel in cur_town.hotels:
            print(hotel.offer())
        print("Enter the name of the hotel")
        which_one = input(">>> ")
        try:
            user_hotel = list(filter(lambda x: x.name == which_one, cur_town.hotels))[0]
            if user_hotel.price > character.money:
                print(f"Not enough money... You onlu got {character.money}")
            else:
                need_to_sleep -= 1
                hours_left -= 8
                character.visited_hotel(user_hotel)
        except:
            print("Something went wrong :/")

    elif to_do == "shop":
        for shop in cur_town.shops:
            print(shop.proposition())
        print("Enter the name of the shop")
        which_one = input(">>> ")
        try:
            user_shop = list(filter(lambda x: x.name == which_one, cur_town.shops))[0]
            print(user_shop.proposition())
            print("What do you want to buy?")
            user_item = input(">>> ")
            item = [el for el in user_shop.items if el.name == user_item][0]
            if item.price > character.money:
                print(f"Not enough money... You only got {character.money}")
            else:
                character.bought(item, user_shop)
        except:
            print("Something went wrong :/")

    elif to_do == "gas":
        for gas_station in cur_town.gas_st:
            gas_station.offer()
        print("Enter the name of the gas station")
        which_one = input(">>> ")
        try:
            user_gas_st = list(filter(lambda x: x.name == which_one, cur_town.gas_st))[0]
            user_gas_st.offer()
            print()
            print("Enter 'fuel' (to buy fuel), 'take' (to take a vehicle), or 'sell' (to sell fuel from your car, 25 UAH per l)")
            user_resp = input(">>> ")
            if user_resp == "fuel":
                how_much = int(input(">>> Liters of fuel: "))
                if how_much in range(1, user_gas_st.maxim + 1):
                    character.take_fuel(how_much, user_gas_st)
                else:
                    print("Invalid number")
            elif user_resp == "take":
                if user_gas_st.vehicle is not None:
                    character.take_vehicle(user_gas_st)
                else:
                    print("No vehicle here")
            elif user_resp == "sell":
                how_much = int(input(">>> Liters of fuel to give away: "))
                if how_much in range(1, character.vehicle.fuel_init + 1):
                    character.sell_fuel(how_much)
                else:
                    print("Incorrect number")
        except:
            print("Something went wrong :/")

    elif to_do == "go":
        print("What town?")
        town = input(">>> ")
        print("'walk' or 'vehicle'?")
        how = input(">>> ")
        try:
            if how in ('walk', 'vehicle'):
                for key in cur_town.linked.keys():
                    if key.town == town:
                        destination = key
                        break
                # destination = list(filter(lambda x: x.name == town, towns))[0] # cur_town.linked.
                distance = cur_town.linked[destination]
                if how == 'walk':
                    time_needed = distance / character.walk_speed
                    hours_left -= time_needed
                    character.hours_hungry -= time_needed
                    visited_towns.append(town)
                    cur_town = destination
                elif how == 'vehicle':
                    character.happiness += character.vehicle.give_happy
                    time_needed = distance / character.vehicle.speed
                    fuel_used = int(character.vehicle.fuel_usage * distance / 100)
                    character.vehicle.fuel_init -= fuel_used
                    hours_left -= time_needed
                    character.hours_hungry -= time_needed
                    visited_towns.append(town)
                    cur_town = destination
            else:
                print("Invalid input")
        except:
            print("Something went wrong :/")

    dead = check_if_end()
    if dead:
        print("The end!")
