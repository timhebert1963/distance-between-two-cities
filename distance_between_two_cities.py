from functions_distance_between_two_cities import *
import os

def main(debug):
    '''
    a googlemaps geocode api_key is needed to run this script
    
    2 youtube links which explain how to get the api_key and set environment variables
    https://www.youtube.com/watch?v=1MVDIFShE5Q
    https://www.youtube.com/watch?v=sI8py6soTWs
    '''

    # explain input is needed from user of the two cities, states to calculate distance
    intro_message(debug)

    continue_exploring = True

    while continue_exploring:

        # display 50 state abbreviations and names
        display_state_abbr()

        # display formatting. Need carriage return and prompt user to hit Enter key
        print('\n')
        input(" Press Enter to continue")

        # clear the screen
        if not debug:
            clear_screen()

        # display 50 state abbreviations and names
        display_state_abbr()
        print('\n')

        # call ask_for_two_cities() and return the cities and state names
        city1, state1, city2, state2 = ask_for_two_cities(debug)

        # calculate the distance between two cities
        distance = calculate_dist(debug, city1, state1, city2, state2)

        # clear the screen
        if not debug:
            clear_screen()

        # display a banner informing user of the distance
        distance_banner(debug, city1, state1, city2, state2, distance)

        for i in range(4):
            print('\n')

        continue_exploring = continue_exploring_distance(debug)

        if not debug:
            clear_screen()

    thank_you_for_exploring_banner(debug)

# **** End of function main() **** #

debug = False

if not debug:
    clear_screen()
    print('\n')
    print('\n')

#display_state_abbr()

main(debug)