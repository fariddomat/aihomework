from collections import deque


class Map:
    
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    H = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu':  253,
        'Fagaras':176,
        'Rimnicu_Vilcea': 193,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Dobreta': 242,
        'Pitesti':100,
        'Craiova':160,
        'Bucharest':0,
        'Giurgiu':77,
        'Urziceni': 80,
        'Vaslui':199,
        'Iasi':226,
        'Neamt':234,
        'Hirsova':151,
        'Eforie':161
        }
    def h(self, n):
        return self.H[n]

    

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}
        g[start_node] = 0
        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None
            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;
            if n == None:
                return 'Path does not exist!'
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                return 'Path found: {}'.format(reconst_path)
            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + int(weight)
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + int(weight):
                        g[m] = g[n] + int(weight)
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
        return 'Path does not exist!'

    
adjacency_list = {'Arad': [('Sibiu', '140'), ('Timisoara', '118'), ('Zerind', '75')], 'Sibiu': [('Arad','140'), ('Fagaras', '99'), ('Oradea', '151'), ('Rimnicu_Vilcea', '80')], 'Timisoara': [('Arad', '118'), ('Lugoj', '111')], 'Zerind': [('Arad', '75'), ('Oradea', '71')], 'Bucharest': [('Fagaras', '211'), ('Giurgiu', '90'), ('Pitesti', '101'), ('Urziceni', '85')], 'Fagaras': [('Bucharest', '211'), ('Sibiu', '99')], 'Giurgiu': [('Bucharest', '90')], 'Pitesti': [('Bucharest', '101'), ('Craiova', '138'), ('Rimnicu_Vilcea', '97')], 'Urziceni': [('Bucharest', '85'), ('Hirsova', '98'), ('Vaslui', '142')], 'Craiova': [('Dobreta', '120'), ('Pitesti', '138'), ('Rimnicu_Vilcea', '146')], 'Dobreta': [('Craiova', '120'), ('Mehadia', '75')], 'Rimnicu_Vilcea': [('Craiova', '146'), ('Pitesti', '97'), ('Sibiu', '80')], 'Mehadia': [('Dobreta', '75'), ('Lugoj', '70')], 'Eforie': [('Hirsova', '86')], 'Hirsova': [('Eforie', '86'), ('Urziceni', '98')], 'Iasi': [('Neamt', '87'), ('Vaslui', '92')], 'Neamt': [('Iasi', '87')], 'Vaslui': [('Iasi', '92'), ('Urziceni', '142')], 'Lugoj': [('Mehadia', '70'), ('Timisoara', '111')], 'Oradea': [('Zerind', '71'), ('Sibiu', '151')]}



# this function take data from site and pass it to a_star_algorithm function
def searchAlgorithm(city1, city2):
    global response
    global adjacency_list
    response="" 
    #if one of the city is not in the map
    if city1 not in adjacency_list or city2 not in adjacency_list:
        response= 'City Not In Map'
    #if city in the map do a_star function
    else:
        map1 = Map(adjacency_list)
        response=map1.a_star_algorithm(city1, city2)
    return response

# convet cities distance to List
def createAdjacencyList(cityString):
    global adjacency_list
    map = {}
    #split line by line
    for i in cityString.split('\n'):
        node_val = i.split(",")
        #if city1 and city2 in the map update the current value
        if node_val[0] in map and node_val[1] in map:
            c = map.get(node_val[0])
            c.append((node_val[1], node_val[2]))
            map.update({node_val[0]: c})
            c = map.get(node_val[1])
            c.append((node_val[0], node_val[2]))
            map.update({node_val[1]: c})
        # else if city1 in map append city2 to it
        elif node_val[0] in map:
            c = map.get(node_val[0])
            c.append((node_val[1], node_val[2]))
            map.update({node_val[0]: c})
            map[node_val[1]] = [(node_val[0], node_val[2])]
        # else if city2 in map append city1 to it
        elif node_val[1] in map:
            c = map.get(node_val[1])
            c.append((node_val[0], node_val[2]))
            map.update({node_val[1]: c})
            map[node_val[0]] = [(node_val[1], node_val[2])]
        # if both of the cities are new add them to list
        else:
            map[node_val[0]] = [(node_val[1], node_val[2])]
            map[node_val[1]] = [(node_val[0], node_val[2])]
    
    return map

# convert heuristics value from [city,value] to list
def createtHeuristics(f):
    heuristics = {}
    # split lines
    for i in f.split('\n'):
        # split on ","
        node_heuristic_val = i.split(",")
        heuristics[node_heuristic_val[0]] = int(node_heuristic_val[1])
    return heuristics

# store new map value
def storeNewMap(mapSet,st):
    global adjacency_list
    global GRAPH
    global straight_line
    try:
        adjacency_list=createAdjacencyList(mapSet)
        Map.H=createtHeuristics(st)
        return "Country updated"
    except:
        return "Data Error"
    
    
#reset map value to romania 
def SetRomaniaMap():
    global adjacency_list
    Map.H = {
                    'Arad': 366,
                    'Zerind': 374,
                    'Oradea': 380,
                    'Sibiu':  253,
                    'Fagaras':176,
                    'Rimnicu_Vilcea': 193,
                    'Timisoara': 329,
                    'Lugoj': 244,
                    'Mehadia': 241,
                    'Dobreta': 242,
                    'Pitesti':100,
                    'Craiova':160,
                    'Bucharest':0,
                    'Giurgiu':77,
                    'Urziceni': 80,
                    'Vaslui':199,
                    'Iasi':226,
                    'Neamt':234,
                    'Hirsova':151,
                    'Eforie':161
                    }
    adjacency_list = {'Arad': [('Sibiu', '140'), ('Timisoara', '118'), ('Zerind', '75')], 'Sibiu': [('Arad','140'), ('Fagaras', '99'), ('Oradea', '151'), ('Rimnicu_Vilcea', '80')], 'Timisoara': [('Arad', '118'), ('Lugoj', '111')], 'Zerind': [('Arad', '75'), ('Oradea', '71')], 'Bucharest': [('Fagaras', '211'), ('Giurgiu', '90'), ('Pitesti', '101'), ('Urziceni', '85')], 'Fagaras': [('Bucharest', '211'), ('Sibiu', '99')], 'Giurgiu': [('Bucharest', '90')], 'Pitesti': [('Bucharest', '101'), ('Craiova', '138'), ('Rimnicu_Vilcea', '97')], 'Urziceni': [('Bucharest', '85'), ('Hirsova', '98'), ('Vaslui', '142')], 'Craiova': [('Dobreta', '120'), ('Pitesti', '138'), ('Rimnicu_Vilcea', '146')], 'Dobreta': [('Craiova', '120'), ('Mehadia', '75')], 'Rimnicu_Vilcea': [('Craiova', '146'), ('Pitesti', '97'), ('Sibiu', '80')], 'Mehadia': [('Dobreta', '75'), ('Lugoj', '70')], 'Eforie': [('Hirsova', '86')], 'Hirsova': [('Eforie', '86'), ('Urziceni', '98')], 'Iasi': [('Neamt', '87'), ('Vaslui', '92')], 'Neamt': [('Iasi', '87')], 'Vaslui': [('Iasi', '92'), ('Urziceni', '142')], 'Lugoj': [('Mehadia', '70'), ('Timisoara', '111')], 'Oradea': [('Zerind', '71'), ('Sibiu', '151')]}
    return "Reset Romania map successfully"
    