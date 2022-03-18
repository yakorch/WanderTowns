class Town():
    def __init__(self, town, hotels, shops, gas_stations):
        self.town = town
        self.hotels = hotels
        self.shops = shops
        self.gas_st = gas_stations

    def __str__(self):
        return f"{self.town}"
    
    def link_town(self, an_town, distance):
        if "linked" in dir(self):
            self.linked[an_town] = distance
        else:
            self.linked = dict()
            self.linked[an_town] = distance

    def go(self, place):
        return self.linked[place]

    def get_details(self):
        print("You are in", self.__str__())
        print("-"*20)
        print(f"The city has such hotels as: {', '.join(hotel.name for hotel in self.hotels)}")
        print(f"The city has these shops: {', '.join(shop.name for shop in self.shops)}")
        print(f"There are gas stations: {', '.join(gas.name for gas in self.gas_st)}")
        if "linked" in dir(self):
            print("Possible destinations are:")
            for town, distance in self.linked.items():
                print(town, "is", distance, "km away.")

class Vehicle():
    def __init__(self, name, speed, fuel_usage, give_happy):
        self.name = name
        self.speed = speed
        self.fuel_usage = fuel_usage
        self.give_happy = give_happy
        self.fuel_init = 0

    def __str__(self):
        return f"{self.name}"

class Car(Vehicle):
    def __init__(self, name, speed, fuel_usage, give_happy):
        super().__init__(name, speed, fuel_usage, give_happy)
        self.fuel_init = 0

class Bicycle(Vehicle):
    def __init__(self, name, speed, give_happy, fuel_usage=0):
        super().__init__(name, speed, fuel_usage, give_happy)
        self.fuel_init = 0

class Bike(Vehicle):
    def __init__(self, name, speed, fuel_usage, give_happy):
        super().__init__(name, speed, fuel_usage, give_happy)
        self.fuel_init = 0

class Building():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"You are at {self.name}"

class GasStation(Building):
    def __init__(self, name, fuel_price, maxim):
        super().__init__(name)
        self.fuel_price = fuel_price
        self.maxim = maxim
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle

    def offer(self):
        res = f'{self.name} offers {self.fuel_price} for 1l of fuel. {self.maxim} liters left'
        if self.vehicle is not None:
            res += f"\nThere is a {self.vehicle} out here!"
            print(res)
            print(f"Characteristics: fuel (l) consumption per 100 km - {self.vehicle.fuel_usage}, speed - {self.vehicle.speed}, happy for 1 drive - {self.vehicle.give_happy}")
        else:
            print(res)


class Shop(Building):
    def __init__(self, name, items):
        super().__init__(name)
        self.items = items

    def proposition(self):
        return f"{self.name} offers {self.items}"

class Hotel(Building):
    def __init__(self, name, price, happiness, breakfast):
        super().__init__(name)
        self.price = price
        self.happiness = happiness
        self.breakfast = breakfast

    def offer(self):
        return f"{self.name} costs {self.price}, happiness change: {self.happiness}, breakfast: {self.breakfast}"

class Item():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is {self.name}"

class Food(Item):
    def __init__(self, name, price, satiety):
        super().__init__(name)
        self.price = price
        self.satiety = satiety

    def __repr__(self):
        return f"{self.name} costs {self.price}, and feeds you for {self.satiety} hours"


class Character():
    def __init__(self, money, hours_hungry, walk_speed, happiness, vehicle=None):
        self.money = money
        self.hours_hungry = hours_hungry
        self.walk_speed = walk_speed
        self.happiness = happiness
        self.vehicle = vehicle

    def is_dead(self):
        if self.happiness < 0:
            print(f"Happiness is lower than zero ({self.happiness}) ")
            return True
        elif self.hours_hungry < 0:
            print(f"You were too hungry. Waited too long for {abs(self.hours_hungry)} hours!")
            return True
        return False

    def visited_hotel(self, hotel: Hotel):
        self.money -= hotel.price
        self.happiness += hotel.happiness
        if hotel.breakfast:
            self.hours_hungry += 4

    def bought(self, item: Food, shop: Shop):
        self.money -= item.price
        self.hours_hungry += item.satiety
        shop.items.remove(item)

    def take_fuel(self, how_much, gas_st):
        if "vehicle" in dir(self):
            self.vehicle.fuel_init += how_much
            gas_st.maxim -= how_much
            self.money -= gas_st.fuel_price * how_much
            print(f"You bought {how_much} liters of fuel for your {self.vehicle}")
        else:
            print("You don't have any vehicle now")

    def take_vehicle(self, gas_st):
        if "vehicle" in dir(self):
            self.vehicle, gas_st.vehicle = gas_st.vehicle, self.vehicle
        else:
            self.vehicle = gas_st.vehicle
            gas_st.vehicle = None

    def sell_fuel(self, amount):
        self.money += amount * 25
        self.vehicle.fuel_init -= amount
