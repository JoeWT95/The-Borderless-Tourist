#The Borderless Tourist

#1. Setup
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#2. Travelling to Faraway Lands
def get_destination_index(destination):
    try:
        return destinations.index(destination)
    except:
        print(f"Destination {destination} doesn't exist")
        return -1

def get_traveler_location(traveler):
    if len(traveler) < 1 :
        print("Travel has no location")
        return ""
    return traveler[1]

#Testing Returns
test_destination_location = get_traveler_location(test_traveler)
test_destination_index = get_destination_index(test_destination_location)
print("2. Testing Destination Index : " + str(test_destination_index))
print("2. Testing Destination Location : " + str(test_destination_location))

#3. Visiting Interesting Places
attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions[destination_index].append(attraction)
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

#4. Finding the Best Places to Go
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_at_location = attractions[destination_index]

    return [ attraction[0]
             for attraction in attractions_at_location
             for interest in interests
             for tags in attraction[1]
             if tags == interest]

#Testing Returns
print("4. " + str(find_attractions("Los Angeles, USA", ['art'])))
print("4. " + str(find_attractions("Shanghai, China", ['garden', 'skyscraper'])))

#5. See The Parts of a City You want to See
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + " : "
    for i in range(len(traveler_attractions)):
        interests_string += str(traveler_attractions[i])
        if i != len(traveler_attractions) - 1:
            interests_string += " and "
    return interests_string

#Testing Returns
print(f"5. {get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])}")
print(f"5. {get_attractions_for_traveler(['Joe Tilley', 'Cairo, Egypt', ['historical site', 'museum']])}")