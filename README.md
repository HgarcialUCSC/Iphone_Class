# Iphone_Class
Description of Class
	The iPhone class’s purpose is to show the current iPhones in the Apple market, list the colors and price of the specified iPhone, determine whether if the iPhone is within the user’s budget, and whether all these specifications are met. The class takes in 3 arguments, a string argument of the name of the iPhone, an integer argument of the user’s budget, and a string argument of the color of the iPhone. The iPhone name argument is used to find the colors available and to find the price. The color augment is to find if the color is available for the specified iPhone. And the budget argument finds if the iPhone price is within the user’s budget. 

Date Variables & Class Variables
Class Variables 
	iphones_price: dictionary that holds iPhone names as keys and prices values
	iphones_colors: dictionary that holds iPhone names as keys and colors as values
iphones_colors2: dictionary that holds iPhone names as keys and colors as values (all     capital letters to ignore user caps spelling in argument)
Data Variables
	self.__iphone: holds the string argument of specified iPhone
	self.__budget: holds integer argument of user’s budget
	self.__color: holds string argument of specified color
	self.__color2: holds string argument of specified color in all caps

Methods
	__init__: sets arguments for iPhone, budget, and color
	available_iphones(): returns list of available iPhones in Apple market
	get_price(): gets the price of the specified iPhone argument
get_colors(): gets the colors available for iPhone argument
can_afford(): determines whether the specified iPhone is within the budget argument
purchase_phone(): if specified iPhone is available, the specified color is available, the cost of the iPhone is within budget, returns a message that all requirements are satisfied.

Demo Program
	To run the demo program, first, you need to set a variable to call the iPhone class inside the main() function. This can be done by doing “my_phone = iPhone()”. The variable name does not change program performance. Inside “iPhone()”, 3 arguments are required: the iPhone name as a string argument (case sensitive), the budget as an integer argument, and the color as a string argument (not case sensitive). This can be done by doing the following:  “my_phone = iPhone(“iPhone 13 Pro”, 1000, “Black”)”. In this example, “my_phone” is the name to call this class and its arguments. Now, to use the methods, put a period after the variable name and follow with the desired method: “my_phone.get_colors()”. In this example, the colors of the iPhone 13 Pro would be displayed. 
