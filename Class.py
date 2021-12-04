#Custom class

#This program will determine whether the user can afford the current iphones in market based on their budget and preffered color
class iPhone:
    #puts iPhone prices and names into dictionary
    iphones_price = {
     "iPhone 13 Pro": 999.00,
     "iPhone 13": 699.00, 
     "iPhone 12": 599.00, 
     "iPhone SE": 399.00, 
     "iPhone 11": 499.00}
    iphone_colors = {
     "iPhone 13 Pro":["White", "Blue", "Black", "Gold"],
     "iPhone 13": ["Pink", "Blue", "Black", "White", "Red"], 
     "iPhone 12": ["Purple", "Blue", "Green", "White", "Black", "Red"], 
     "iPhone SE": ["White", "Black", "Red"], 
     "iPhone 11": ["Purple", "Green", "Yellow", "White", "Black", "Red"]
     }
    iphone_colors2 = { #allows argument to ignore capitalization
     "iPhone 13 Pro":["WHITE", "BLUE", "BLACK", "GOLD"],
     "iPhone 13": ["PINK", "BLUE", "BLACK", "WHITE", "RED"], 
     "iPhone 12": ["PURPLE", "BLUE", "GREEN", "WHITE", "BLACK", "RED"], 
     "iPhone SE": ["WHITE", "BLACK", "RED"], 
     "iPhone 11": ["PURPLE", "GREEN", "YELLOW", "WHITE", "BLACK", "RED"]
     }
    #sets 3 arguments, one for user iphone, their budget, and preffered color 
    def __init__(self, iphone, budget, color):
        self.__iphone = iphone
        self.__budget = budget
        self.__color = color
        self.__color2 = color.upper()
        return
    #returns list of available iphones
    def available_iphones(self):
        iphones_list = []
        iphones = self.iphones_price.keys()
        for i in iphones:
            iphones_list.append(i)
        return (f"The iPhones that are in the market right now are:\n{iphones_list}")
    #Gets price of iphone by putting into dictionary
    def get_price(self):
        if self.__iphone in self.iphones_price:
            return (f"The cost of the {self.__iphone} is:\n${self.iphones_price[self.__iphone]:.2f}")
        else:
            return (f"The {self.__iphone} was not found, or is not current market.")
    #Gets colors of specified iphone by putting into dictionary
    def get_colors(self):
        if self.__iphone in self.iphone_colors:
            return(f"Colors available for the {self.__iphone} are:\n{self.iphone_colors[self.__iphone]}")
        else:
            return (f"The {self.__iphone} was not found, or is not in current market.")
    #finds if budget is avaible to purchase iphone and tells them how much money is left over or how much money is left to buy
    def can_afford(self):
        if self.__iphone in self.iphones_price:
            price = self.iphones_price[self.__iphone]
            pass
        else:
            return (f"The {self.__iphone} was not found, or is not in current market.")
        if self.__budget >= price:
            remaining = self.__budget - price
            return (f"You can afford the {self.__iphone}, and will have ${remaining:.2f} remaining.")
        else:
            money_off = price - abs(self.__budget)
            return (f"You cannot afford the {self.__iphone}, you need ${money_off:.2f} left.")
    #if iphone is available, color is available, and price of iphone is within budget, message is printed stating user can purchase iphone
    def purchase_phone(self):
        if self.__iphone in self.iphones_price:
            pass
        else:
            return (f"The {self.__iphone} was not found, or is in current market.")
        #makes color argument capitol and searches through a dictionary with capitol values
        if self.__color2 in self.iphone_colors2[self.__iphone]:
            pass
        else:
            return (f"The color {self.__color.lower()} is not available for the {self.__iphone}")
        if self.__budget >= self.iphones_price[self.__iphone]:
            return (f"Congradulations! The {self.__iphone} is within your budget of ${self.__budget:.2f} and the color {self.__color.lower()} is available!")
        else:
            return(f"The {self.__iphone} is not within your budget")


def main():
    my_iphone = iPhone("iPhone 13 Pro", 1000, "Yellow")
        #sets variable to get class arguments: the iphone of interest, intiger of user's budget, and the prefered color
    print (my_iphone.available_iphones())
        #prints the avaible iphones that are in the market, uses class variable to get this information
    print (my_iphone.get_price())
        #prints the price of the iphone in first class argument
    print (my_iphone.get_colors())
        #prints the colors aviable for the iphone in first class argument
    print (my_iphone.can_afford())
        #finds the price of iphone in first argument and compares is to the user's budget in the second argument and prints affordability
    print (my_iphone.purchase_phone())
        #if the iphone in first argument is available, the cost of iphone is within user's budget, and the color is available in user's third arugment
            #prints mesage that all conditions are met for user to buy desired iphone
if __name__ == "__main__":
    main()