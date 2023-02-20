import math
cities = []
f = open("adjacencies.txt", "r")

# list of cities is created
for x in f:
    adjs = list(x.split())
    for ad in adjs:
        add = True
        for city in cities:
            if city == ad:
                add = False
        if add == True:
            cities.append(ad)
f.close()

city_count = len(cities)

# Graph for keeping track of adjacencies and costs
graph = [[] for i in range(city_count)]

# Best-first search function. When choosing next city, always chooses lowest cost. Will move backwards in order if at dead end. Tries new routes untill successful
def best_first_search(actual_Src, target):
    order = []
    order.append(actual_Src)
    visited = [False] * city_count
    current = actual_Src
    visited[actual_Src] = True

    run = True
    while run == True:
        min_c = 999999
        found = False
        new_index = 0
        for v, c in graph[current]:
            # if target is adjacent, it is chosen and the loop breaks
            if v == target:
                order.append(v)
                run = False
                break
            # next location is chosen if it hasn't been visited before and its cost is the lowest of the current options from the current location
            if c < min_c and visited[v] == False:
                new_index = v
                min_c = c
                found = True
        if run == False:
            break
        # if no locations that haven't been visited were available, return to previous location and remove current location from order
        if found == False:
            order.pop()
            current = order[-1]
        # adds next location to order and marks as having been visited
        else:
            order.append(new_index)
            current = new_index
            visited[new_index] = True

    # once an order that leads to the destination is found, it is printed to the console.
    for location in order:
        if location == target:
            print(cities[location], end=" ")
            break
        print(cities[location], end=" -> ")

    print()
 
# addpath adds an adjacency and its cost to the graph
def addpath(p1, p2, cost):
    x = 0
    y = 0
    i = 0
    j = 0
    for city in cities:
        if p1 == city:
            x = i
        i += 1
    for city in cities:
        if p2 == city:
            y = j
        j += 1
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# determines distance between two cities
def find_cost(p1, p2):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    f = open("coordinates.txt", "r")
    for x in f:
        line = list(x.split())
        if line[0] == p1:
            x1 = float(line[1])
            y1 = float(line[2])
        if line[0] == p2:
            x2 = float(line[1])
            y2 = float(line[2])
    num = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))
    num = math.sqrt(num)
    return num

# goes through adjacencies text file and calls addpath function to add them to graph
f = open("adjacencies.txt", "r")
for x in f:
    adjs = list(x.split())
    for ad in adjs:
        if ad != adjs[0]:
            cost = find_cost(adjs[0], ad)
            addpath(adjs[0], ad, cost)
f.close()

program = True
while program == True:
    source = 0
    target = 0
    run = True
    while run == True:
        # asks user for starting location
        start_city = input("Enter starting city (Enter \"E\" to exit the program): ")
        if start_city == "E":
            program = False
            break
        i = 0
        for city in cities:
            if start_city == city:
                source = i
                run = False
            i += 1
        if run == True:
            # asks user for another input if given city name isn't found
            print("City not found. Please try again.\n")

    if program == False:
        break
    
    run = True
    while run == True:
        # asks user for destination
        end_city = input("Enter destination: ")
        i = 0
        for city in cities:
            if end_city == city:
                target = i
                run = False
            i += 1
        if run == True:
            # asks user for another input if given city name isn't found
            print("City not found. Please try again.\n")

    print("\n")
    best_first_search(source, target)
    print("\n")
