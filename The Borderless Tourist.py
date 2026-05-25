#The Borderless Tourist

#Decalarations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#1. Get Index
## My solution
# def get_destination_index(destination):
#  for i in range(len(destinations)):
#    if destinations[i] == destination:
#      destination_index = i
#  return destination_index  

#CA solution
def get_destination_index(destination):
    return destinations.index(destination)

#print(get_destination_index("Los Angeles, USA"))


#2. Get Traveller Location
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    return traveler_destination

traveler_destination_index = get_destination_index(get_traveler_location(test_traveler))

#3. Attactions
# Basic Declare
#attractions = [[], [], [], [], []]

#Loop Declare
# attractions = []
# for i in range(5):
#     attractions.append([])

#List Comprehension
attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

add_attraction("Los Angeles, USA", ["Venice Beach", ["Beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#4. Find Attractions
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = possible_attraction[1]
        for interest in interests:
            for tags in attraction_tags:
                if interest == tags:
                    attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])

# print(la_arts)

#Get Attractions
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attactions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + " :"
    for attraction in traveler_attactions:
        interests_string += str(attraction)
    return interests_string

print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))