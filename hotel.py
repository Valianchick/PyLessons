class Hotel:
    _prices = {"SGL": 1000, "DBL": 2500, "Junior Suite": 5000, "Suite": 15000} 
    _types = list(_prices.keys())
    _rooms = dict()

    def __init__(self, numRooms):
        for num in range(len(numRooms)):
            self._rooms[self._types[num]]=[1]*numRooms[num]
    
    def occupy (self, roomType, NumRoom):
        if (self._rooms[roomType][NumRoom-1]==1):
            self._rooms[roomType][NumRoom-1] = 0
            print ("Номер забронирован")
        else:
            raise RuntimeError("Номер занят")

    def __str__(self):
        infroom = ""
        for i in self._types:
            info = f"Тип {i}: \n"
            for num in range(len(self._rooms[i])):
                if self._rooms[i][num]==1:
                    info += f"{num+1} номер свободен \n"
                else:
                    info += f"{num+1} номер занят \n"
            infroom += info
        return infroom

    def all_occypy(self):
        for i in self._types:
            for num in range(len(self._rooms[i])):
                self._rooms[i][num]=0

    def all_free(self):
        for i in self._types:
            for num in range(len(self._rooms[i])):
                self._rooms[i][num]=1


    def income(self):
        income = 0
        for i in self._types:
            income += (self._rooms[i].count(0)) * self._prices[i]
        return (f"Выручка {income} \n")

    def change_prices(self, roomType, newPrice): 
        self._prices[roomType] = newPrice
        price = "Новые цены на номера \n"
        for i in self._types:
            price += f"{i} - {self._prices[i]} \n"
        return price
    
    def pricesAll(self): 
        price = "Текущие цены на номера \n"
        for i in self._types:
            price += f"{i} - {self._prices[i]} \n"
        return price

hotel = Hotel((10, 4, 7, 5))
hotel.occupy("SGL", 2) 
hotel.occupy("DBL", 1)
hotel.occupy("DBL", 2)
hotel.occupy("Suite", 4)
print(hotel)
print (hotel.income())
print (hotel.pricesAll())
print (hotel.change_prices("Suite", 12000))
