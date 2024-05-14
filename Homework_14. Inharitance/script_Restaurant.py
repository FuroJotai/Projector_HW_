class Restaurant():
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)        
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name in self.menu:
            dish = self.menu[dish_name]
            if dish['quantity'] >= quantity: 
                dish['quantity'] -= quantity
                total_cost = dish['price'] * quantity
                return total_cost
            else:
                return 'This quantity is not available'
        else:
            return 'Sorry, dish is not available!'    
