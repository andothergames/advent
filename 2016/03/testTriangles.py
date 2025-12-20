# --- Day 3: Squares With Three Sides ---

with open('0316input.txt', 'r') as file:
    data = file.readlines()


def formatData(input):
    triangles = []
    for line in input:
        triSides = line.split(' ')
        triangle = []
        for tri in triSides:
            if len(tri) != 0:
                triangle.append(int(tri.rstrip()))
        triangles.append(triangle)
    return triangles


def testTriangles(triangle):
    checker = True
    if triangle[0] + triangle[1] <= triangle[2]:
        checker = False
    if triangle[2] + triangle[1] <= triangle[0]:
        checker = False
    if triangle[2] + triangle[0] <= triangle[1]:
        checker = False
    return checker


def main(triangles):
    possibleTris = 0
    for triangle in triangles:
        if testTriangles(triangle):
            possibleTris += 1
    return possibleTris


triangles = formatData(data)
print(main(triangles))