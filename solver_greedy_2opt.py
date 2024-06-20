import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)



def solve(cities): #greedy + 2opt
    N = len(cities)
    
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

        
    #heuristic is 2-opt
    while True:
        score = 0

        for i in range(N - 3):
            for j in range(i + 1, N - 1):
                #before
                dist1 = dist[tour[i]][tour[i + 1]]
                dist2 = dist[tour[j]][tour[j + 1]]
                #after
                dist3 = dist[tour[i]][tour[j]]
                dist4 = dist[tour[i + 1]][tour[j + 1]]

                if dist1 + dist2 > dist3 + dist4:
                    new_path = tour[i + 1:j + 1][::-1]
                    tour[i + 1:j + 1] = new_path
                    score += 1

        if score == 0:
            break

        
    return tour

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)