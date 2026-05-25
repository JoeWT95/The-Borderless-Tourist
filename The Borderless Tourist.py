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

