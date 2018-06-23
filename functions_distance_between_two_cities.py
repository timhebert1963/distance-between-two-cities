from math import sin, cos, sqrt, atan2, radians
#from modules_distance_between_two_cities import *
from Tim_common import *
import os
import googlemaps

def display_state_abbr():

    print(" State Abbreviations:")
    print('\n')

    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('AL', 'Alabama',\
                                                                                                'HI', 'Hawaii',        \
                                                                                                'MA', 'Massachusetts', \
                                                                                                'NM', 'New Mexico',    \
                                                                                                'SD', 'South Dakota'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('AK', 'Alaska', \
    	                                                                                        'ID', 'Idaho',         \
    	                                                                                        'MI', 'Michigan',      \
                                                                                                'NY', 'New York',      \
                                                                                                'TN', 'Tennessee'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('AZ', 'Arizona',\
    	                                                                                        'IL', 'Illinois',      \
    	                                                                                        'MN', 'Minnesota',     \
                                                                                                'NC', 'North Carolina',\
                                                                                                'TX', 'Texas'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('AR', 'Arkansas',\
    	                                                                                        'IN', 'Indiana',       \
    	                                                                                        'MS', 'Mississippi',   \
                                                                                                'ND', 'North Dakota',  \
                                                                                                'UT', 'Utah'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('CA', 'California',\
    	                                                                                        'IA', 'Iowa',          \
    	                                                                                        'MO', 'Missouri',      \
    	                                                                                        'OH', 'Ohio',          \
    	                                                                                        'VT', 'Vermont'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('CO', 'Colorado', \
                                                                                                'KS', 'Kansas',        \
                                                                                                'MT', 'Montana',       \
                                                                                                'OK', 'Oklahoma',      \
                                                                                                'VA', 'Virginia'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('CT', 'Connecticut',\
    	                                                                                        'KY', 'Kentucky',      \
    	                                                                                        'NE', 'Nebraska',      \
                                                                                                'OR', 'Oregon',        \
                                                                                                'WA', 'Washington'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('DE', 'Delaware',  \
    	                                                                                        'LA', 'Louisiana',     \
    	                                                                                        'NV', 'Nevada',        \
                                                                                                'PA', 'Pennsylvania',  \
                                                                                                'WV', 'West Virginia'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('FL', 'Florida',   \
    	                                                                                        'ME', 'Maine',         \
    	                                                                                        'NH', 'New Hampshire', \
                                                                                                'RI', 'Rhode Island',  \
                                                                                                'WI', 'Wisconsin'))
    print(" {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}    {:2s} : {:15s}".format('GA', 'Georgia',   \
    	                                                                                        'MD', 'Maryland',      \
    	                                                                                        'NJ', 'New Jersey',    \
                                                                                                'SC', 'South Carolina',\
                                                                                                'WY', 'Wyoming'))

# **** End of function display_state_abbr() **** #


def intro_message(debug):

    # intro message explaining user will be asked for input of the two cities to calculate the distance between
    print(" You will be asked to enter the city and the state for the start city and state,")
    print(" and for the destination city and state. You can enter the abbreviation for the state.")
    print('\n')

# **** End of function intro_message() **** #


def ask_for_two_cities(debug):

    # get input from user of the two cities and states
    city1  = input(" Enter 1st city to calculate distance from:  ")
    state1 = input(" Enter the state {} is located  ".format(city1))

    print('\n')

    city2  = input(" Enter 2nd city to calculate distance to  :  ")
    state2 = input(" Enter the state {} is located  ".format(city2))

    for i in range(2):
        print('\n')

    # return the two cities and states to caller
    return city1, state1, city2, state2

# **** End of function ask_for_two_cities() **** #


def calculate_dist(debug, city1, state1, city2, state2):

    # approximate radius of earth in km
    # Rm is the mile representation for Radius
    R = get_radius_of_earth_km(debug)
    Rm = convert_km_to_miles(debug, R)

    # start city latitue and Longitude in degrees - lat1 and lon1
    # you need to get the degrees for lat1 and lon1
    #
    # radians(x) converts degrees to radians
    lat1_d, lon1_d = get_degrees(debug, city1, state1)
    lat1_r, lon1_r = get_radians(debug, lat1_d, lon1_d)

    # destination city latitue and Longitude in degrees - lat2 and lon2
    #
    # radians(x) converts degrees to radians
    lat2_d, lon2_d = get_degrees(debug, city2, state2)
    lat2_r, lon2_r = get_radians(debug, lat2_d, lon2_d)

    # distance between lon2_r and lon1_r (two longitudes)
    # distance between lat2_r and lat1_r (two latitudes)
    dlon = lon2_r - lon1_r
    dlat = lat2_r - lat1_r

    # formulas
    a = sin(dlat / 2)**2 + cos(lat1_r) * cos(lat2_r) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # calculate distance in miles
    #
    # convert distance to int
    distance = Rm * c
    distance = int(distance)

    return distance

# **** End of function calculate_dist() **** #


def get_radius_of_earth_km(debug):

    # radius of earth in kilometers
    R = 6373.0
    return R

# **** End of function radius_of_earth_km() **** #


def convert_km_to_miles(debug, distance):

    # convert km to miles
    KILOMETERS_TO_MILES = 0.621371

    return distance * KILOMETERS_TO_MILES

# **** End of function convert_km_to_miles() **** #


def get_degrees(debug, city, state):

    city_state = city + ', ' + state

    # api_key for googlemaps and geocode app
    api_key = os.environ['APIKEY']

    # start googlemaps Client
    gm = googlemaps.Client(key=api_key)

    #geocode_result = gm.geocode(city_state)[0] is another option that could be used
    lat = gm.geocode(city_state)[0]['geometry']['location']['lat']
    lng = gm.geocode(city_state)[0]['geometry']['location']['lng']

    return lat,lng

# **** End of function get_degrees() **** #


def get_radians(debug, lat, lon):

    # return radians of lat, lon
    lat_r = radians(lat)
    lon_r = radians(lon)

    return lat_r, lon_r

# **** End of function get_radians() **** #


def distance_banner(debug, city1, state1, city2, state2, distance):

    # strings to display in display banner
    first_string  = ("Distance Between Two Cities")
    second_string = ("The starting city is {}, {}".format(city1, state1))
    third_string  = ("Destination  city is {}, {}".format(city2, state2))
    fourth_string = ("The distance between {}, {} and {}, {} is {} miles".format(city1, state1, city2, state2, distance))

    # assign values to Banner object attributes
    banner_object = assign_banner_attributes(debug, first_string, second_string, third_string, fourth_string)

    # call display_banner
    display_banner(debug, banner_object)
    del banner_object

# **** End of function get_radians() **** #


def thank_you_for_exploring_banner(debug):

    # strings to display in display banner
    first_string  = ("Thank You for Exploring the")
    second_string = ("Distance Between Two Cities!!")

    # assign values to Banner object attributes
    banner_object = assign_banner_attributes(debug, first_string, second_string)

    # call display_banner
    display_banner(debug, banner_object)
    del banner_object

# **** End of function get_radians() **** #


def continue_exploring_distance(debug):

    valid_answer = False

    while not valid_answer:
        answer = input(" Would you like to continue exploring the distance between two cities?  'y' or 'n' ")

        if answer.lower() == 'y' or answer.lower() == 'n':
            valid_answer = True

        else:
            print(" You did not enter 'y' or 'n'. Please try again!")
            print('\n')

    if answer.lower() == 'y':
        return True

    else:
        return False

# **** End of function continue_exploring_distance() **** #