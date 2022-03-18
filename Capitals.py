capitals = ["Amsterdam", "Andorra la Vella", "Athens", "Berlin", "Bratislava", "Brussels", "Dublin", "Helsinki",
            "Lisbon", "Ljubljana", "Luxembourg", "Madrid", "Monaco", "Nicosia", "Paris", "Riga", "Rome", "San Marino",
            "Tallinn", "Valletta", "Vatican City", "Vienna", "Vilnius"]
# len_cities = len(capitals)
# print("length of capital arrays = ",len_cities)
countries = ["Netherlands", "Andorra", "Greece", "Germany", "Slovakia", "Belgium", "Ireland", "Finland", "Portugal",
             "Slovenia", "Luxembourg", "Spain", "Monaco", "Cyprus", "France", "Latvia", "Italy", "San Marino",
             "Estonia", "Malta", "Vatican City", "Austria", "Lithuania"]
# print(capitals.index("Berlin"))
print("Rules: All countries and capitals have to be capitalized!\n"
      "If no correct answers apply enter 'none'\n")
capitals_input = input("Name a capital city of a eurozone country: ")
if capitals_input in capitals:
    print("Well done!")
    countries_input = input("Which country is it the capital of? ")
    if countries_input in countries:
        if capitals.index(capitals_input) == countries.index(countries_input):
            print("That's correct")
            neighbors = {
                "Netherlands": ["Germany", "Belgium"],
                "Andorra": ["Spain", "France"],
                "Greece": ["none"],
                "Germany": ["France", "Austria", "Netherlands", "Belgium", "Luxembourg"],
                "Slovakia": ["Austria"],
                "Belgium": ["Netherlands", "Luxembourg", "Germany", "France"],
                "Ireland": ["none"],
                "Finland": ["none"],
                "Portugal": ["Spain"],
                "Slovenia": ["Austria", "Italy"],
                "Luxembourg": ["Belgium", "Germany", "France"],
                "Spain": ["Portugal", "Andorra", "France"],
                "Monaco": ["France"],
                "Cyprus": ["none"],
                "France": ["Germany", "Spain", "Andorra", "Italy", "Luxembourg", "Monaco", "Belgium"],
                "Latvia": ["Estonia", "Lithuania"],
                "Italy": ["San Marino", "Vatican City", "France", "Slovenia", "Austria"],
                "San Marino": ["Italy"],
                "Estonia": ["Latvia"],
                "Malta": ["none"],
                "Vatican City": ["Italy"],
                "Austria": ["Italy", "Slovenia", "Slovakia", "Germany"],
                "Lithuania": ["Latvia"],
                            }
            neighbor_input = input("Can you name any of its neighboring countries that also use the Euro? (excluding "
                                   "maritime borders) ")
            if neighbor_input in (neighbors[countries_input]):
                print("That is correct!")
                capitals_input_2 = input("Do you also know its capital? ")
                if capitals_input_2 in capitals:
                    if capitals.index(capitals_input_2) == countries.index(neighbor_input):
                        print("Well done!")
                    else:
                        print("That's not the capital.")
            else:
                print("That's not a neighboring country!")
        else:
            print("Wrong country!")
    else:
        print("Country is not on the list!")
elif capitals_input == str("no"):
    print("haiyaaa, why not?")

else:
    print("Wrong!")
