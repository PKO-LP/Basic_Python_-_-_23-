cities = input().split()
first_city = cities[0]
second_city = cities[1]

if first_city[-1].lower() == second_city[0].lower():
    print("Слово подходит")
else:
    print("Слово не подходит")