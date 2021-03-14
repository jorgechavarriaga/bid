from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visits, cities_visited):
    travel_log.append([{
        "country": country_visited,
        "visits": times_visits,
        "cities": cities_visited
        }])

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

def add_new_country_angelayu_solution(country_visited, times_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country_angelayu_solution("Canada", 6, ["Montreal", "Calgary", "Quebec City","Toronto"])
print(travel_log)
