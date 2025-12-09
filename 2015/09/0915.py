# --- Day 9: All in a Single Night ---

from itertools import permutations

with open('0915input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]


def formatJourneys(data):
    journeys = []
    for _ in data:
        x = _.split()
        journey = (x[0], x[2], int(x[4]))
        journeys.append(journey)
    return journeys


def listPlaceNames(journeys):
    places = []
    for _ in journeys:
        if _[0] not in places:
            places.append(_[0])
        if _[1] not in places:
            places.append(_[1])
    return places


def findCombos(p):
    combos = permutations(p)
    return combos


def getDistance(p1, p2, journeys):
    for tuple in journeys:
        if tuple[0] == p1 and tuple[1] == p2:
            return tuple[2]
        if tuple[0] == p2 and tuple[1] == p1:
            return tuple[2]


def getPathTotal(combo, journeys):
    pathTotal = 0
    for i in range(len(combo)-1):
        total = getDistance(combo[i], combo[i + 1], journeys)
        pathTotal += total
    return pathTotal


def calculateRoute(combos, journeys):
    lowestWinner = 10000
    highestWinner = 0
    lowestRoute = ()
    for combo in combos:
        x = getPathTotal(combo, journeys)
        if x < lowestWinner:
            lowestWinner = x
            lowestRoute = combo
        if x > highestWinner:
            highestWinner = x
    print('lower:', lowestWinner, 'higher:', highestWinner, lowestRoute)


def main(data):
    journeys = formatJourneys(data)
    placenames = listPlaceNames(journeys)
    combos = findCombos(placenames)
    calculateRoute(combos, journeys)


main(data)
