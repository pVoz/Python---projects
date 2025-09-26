
# # List v dictionary !

# travel_diary = {
#     "Spain": ["Madrid", "Leon", "Valencia"],
#     "France": ["Paris", "Nice", "Rennes"]
# }
# print(travel_diary["France"][0])
### stale to je len KEY = VALUE či to tam je 5x abo raz 

# travel_diary = {
#     "Spain":{"visited_cities":["Madrid", "Leon", "Valencia"], "visits": 5},
#     "France":{"visited_cities":["Paris", "Nice", "Rennes"], "visits":2}
# }

# print(travel_diary["France"]["visited_cities"][1])
# print(travel_diary["France"]["visits"])


travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2
    }
]
# print(travel_diary[1]["visited_cities"])
def add_country(country_name,towns_list,visits_number):
    new_dictionary = {}
    new_dictionary["country"] = country_name
    new_dictionary["visited_cities"] = towns_list
    new_dictionary["visits"] = visits_number
    travel_diary.append(new_dictionary)
    # print(new_diary)

add_country("Italy",["Rome","Florence","Milan"],9)
print(travel_diary)
print(travel_diary[2]["visited_cities"][1],travel_diary[2]["visits"])
# print(travel_diary[2]["visits"])