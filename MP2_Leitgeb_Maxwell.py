import my_mod #this module is where we'll perform all our data handling
    
# PART ONE - main menu and user interaction 

# main
print("\nHellloooo, Metalheads!!!")
print("Let's learn a little bit about your favorite Metal artists. \nPick an option below. (Enter Quit to leave)\n")


user_choice = ''

while(user_choice.lower() != 'quit'):                           # runs unless the user enters quit
    
    print()
    print("A: Bands per country")
    print("B: Bands formed in year")
    print("C: Bands with keyword")
    print("D: Longest rocking bands\n")



    user_choice = input()                   # get user's choice 

    if user_choice.lower() == 'quit':
        break                               # stops program once the user enters quit


    elif user_choice.lower() == "a":
        countries = my_mod.get_bands_per_country()                      # use the get_bands_per_country() function to get a nested list of countries and the number of bands formed in that country
        my_mod.print_table(countries, "Countries", "Number of Bands")   # print the results in a formatted table with print_table()


    elif user_choice.lower() == "b":
        user_year = input("\nWant to see how Metal a given year was? \nEnter a year and check out which bands formed that year: ")
        year_list = my_mod.get_bands_formed_in_year(user_year)      # Use get_bands_formed_in_year() to get a nested list of all bands formed that year and their country of origin
        my_mod.print_table(year_list, "Band", "Origin")             # Print the results with your print_table() function


    elif user_choice.lower() == "c":
        user_style = input("\nLooking for a specific flavor of Metal? Enter a keyword: ")   # Ask the user to enter a keyword. We'll find all the bands whose styles contain this keyword.
        styles = my_mod.get_bands_with_style(user_style.lower())                            # Use get_bands_with_style() to get a nested list of all bands whose styles contain this keyword.
        my_mod.print_table(styles, "Band", "Styles")                # Print the results with your print_table() function
    
    
    elif user_choice.lower() == "d":
        try:                                                                        # try statement to verify that the input is an integer
            user_num_bands = int(input("\nHow many bands do you want to see? "))
            band_years = my_mod.get_longest_lived_bands(user_num_bands)             # Use get_longest_lived_bands() and print_table to show them a table of bands
            my_mod.print_table(band_years, "Band", "Years Active")
        except ValueError:                                                          # except statement that will execute if there is a ValueError and the input is not an integer
            print("That is not a valid option.")

    
    else:
        print("Invalid options are not metal! Try again.")      # user is given another chance to enter a valid option after entering an invalid one


print("Thank you for learning more about metal bands!")         # final statement that thanks the user for learning more
    
