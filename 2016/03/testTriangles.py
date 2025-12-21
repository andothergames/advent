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


def formatDataInColumns(rows):
    triangles = []
    row = 0
    while row < len(rows):
        triangle = []
        i = 0
        while i < len(rows[0]):
            triangle.append(rows[row][i])
            triangle.append(rows[row + 1][i])
            triangle.append(rows[row + 2][i])
            i += 1
            triangles.append(triangle)
            triangle = []
        row += 3
    return(triangles)
    

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
triangles = formatDataInColumns(triangles)
print(main(triangles))