#The author is Maggie Dunn
def input_7():
    country_na = input("Do you want to go to America or Canada? \n")
    country_na
    if country_na == "America":
        print("You and your best friend decided to go to America. You treck through the rocky mountains and explore Alaskan glaciers.")
        ending()
    else:
        print("You and your best friend decided to go to Canada. You see the beautiful lakes near Banff and the mountains nearby.")
        ending()
def input_6():
    country_africa = input("Do you want to go to Egypt or Zambia? \n")
    country_africa
    if country_africa == "Egypt":
        print("You and your best friend decided to go to Egypt. You have fun at the pyramids and learn lots about mummies.")
        ending()
    else:
        print("You and your best friend decided to go to Zambia. You enjoy the beautiful landscape and take pictures at Victoria Falls.")
        ending()
def input_5():
    country_Europe = input("Do you want to go to Russia or Germany? \n")
    country_Europe
    if country_Europe == "Germany":
        print("You and your best friend decided to go to Germany. You drink lots of beer and enjoy the landscape.")
        ending()
    else:
        print("You and your best friend decided to go to Russia. You explore St. Petersberg and bundle up in the mountains.")
        ending()
def input_4():
    continent_cold = input("Would you like to go somewhere in Europe or North America? \n")
    continent_cold
    if continent_cold == "Europe":
        print("You decided to go to Europe.")
        input_5()
    else:
        print("You decided to go to North America.")
        input_7()
def ending():
    answer = input("Would you like to go on another trip? \n")
    answer
    if answer == "yes":
        adventure()
    else:
        print("Thank you for playing!")
def input_3():
    country = input("Do you want to go to Indonesia or India? \n")
    country
    if country == "Indonesia":
        print("You and your best friend decided to go to Indonesia! You have the best time at different temples and enjoying the beaches.")
        ending()
    else:
        print("You and your best friend decided to go to India. You see the Taj Mahal and enjoy the food.")
        ending()
def input_2():
    continent = input("Would you like to go somewhere in Asia or Africa? \n")
    continent
    if continent == "Asia":
        print("You decided to go to Asia.")
        input_3()
    else:
        print("You decided to go to Africa.")
        input_6()

def input_1():
    weather = input("Do you want to go to somewhere cold or somewhere warm? \n")
    weather
    if weather == "warm":
        print("You decided to go somewhere warm.")
        input_2()
    else:
        print("You decided to go somewhere cold.")
        input_4()
def adventure():
    print("You are going on a vacation with your best friend. You need to decide where you want to go.")
    input_1()
