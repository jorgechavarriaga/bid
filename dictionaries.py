from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

# Nesting

capitals = {
  "France": "Paris",
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "Colombia": "Bogota"
}

print(capitals)

# Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris","Lille","Dijon"],
  "Germany": ["Berlin","HAmburg","Stuttgart"],
  "Canada": ["Calgary","Montreal","Quebec City","Banff"],
  "Colombia": ["Bogota", "Medellin","Cali","Monteria","Cartagena","San Andres Islas","Bucaramanga","Rionegro"]
}

print(travel_log)

# Nasting a Dictionary in a Dictionary

travel_log1 = {
  "Canada": {"cities_visited":["Calgary","Montreal","Quebec City","Banff"], "total_visits":12},
  "Colombia": {"cities_visited":["Bogota", "Medellin","Cali","Monteria","Cartagena","San Andres Islas","Bucaramanga","Rionegro"], "total_visits":69},
}

print(travel_log1)
print(travel_log1["Canada"]["cities_visited"][1],travel_log1["Canada"]["total_visits"] )

# Nasting a Dictionary in a List

travel_log2 = [
    {
        "country": "Canada", 
        "cities_visited":["Calgary","Montreal","Quebec City","Banff"], 
        "total_visits":12
    },
    {
        "country": "Colombia",
        "cities_visited":["Bogota", "Medellin","Cali","Monteria","Cartagena","San Andres Islas","Bucaramanga","Rionegro"], 
        "total_visits":69
    }
]


print(travel_log2)
print(travel_log2[1]["country"])
print(travel_log2[1]["cities_visited"])
print(travel_log2[1]["cities_visited"][3])
print(travel_log2[1]["total_visits"])