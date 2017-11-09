def floydWarshall(matrix, numbersVertex):
    for k in range(numbersVertex):
        for i in range(numbersVertex):
            for j in range(numbersVertex):
                if matrix[i][j] > (matrix[i][k] + matrix[k][j]):
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

def girth(matrix, numbersVertex):
    girth = float('inf')
    for i in range(numbersVertex):
        for j in range(numbersVertex):
            if i == j:
                if matrix[i][j] < girth:
                    girth = matrix[i][j]
    return girth

def eccentricity(matrix, numbersVertex):
    eccentricity = []
    for i in range(numbersVertex):
        largest = float('-inf')
        for j in range(numbersVertex):
            if not(i == j):
                if (not matrix[i][j] == float('inf')) and (matrix[i][j] > largest):
                    largest = matrix[i][j]
        if not(largest == float('-inf')):
            eccentricity.append(largest)
    return eccentricity

def diameter(matrix, numbersVertex):
    diameter = float('-inf')
    for i in range(numbersVertex):
        for j in range(numbersVertex):
            if (not (matrix[i][j] == float('inf'))) and (matrix[i][j] > diameter) and (not(i==j)):
                diameter = matrix[i][j]
    return diameter

def radius(eccentricity):
    return min(eccentricity)

def center(radius, eccentricity):
    center = []
    for i in range(len(eccentricity)):
        if radius == eccentricity[i]:
            center.append(i+1)
    center.sort(reverse=True)
    return (' '.join([str(x) for x in center]))

matrix = []
infinite = float('inf')

numbers = [int(x) for x in input().split()]

for i in range(numbers[0]):
    line = []
    for j in range(numbers[0]):
        line.append(infinite)
    matrix.append(line)

# for i in range(numbers[0]):
#     for j in range(numbers[0]):
#         if i == j:
#             matrix[i][j] = 0

for k in range(numbers[1]):
    line = [int(x) for x in input().split()]
    if line[2] < matrix[line[0]-1][line[1]-1]:
        matrix[line[0]-1][line[1]-1] = line[2]

if numbers[1] == 0:
    # center = [int(x)+1 for x in range(numbers[0])]
    # center.sort(reverse=True)
    print("Error")
    print("Error")
    print("Error")
    #print(' '.join([str(x) for x in center]))
else:

    # for x in matrix:
    #     print(x)
    # print()


    floydWarshall(matrix, numbers[0])

    # for x in matrix:
    #     print(x)
    # print()

    eccentricity = eccentricity(matrix, numbers[0])

    a = girth(matrix, numbers[0])
    b = diameter(matrix, numbers[0])
    c = radius(eccentricity)
    center = center(radius(eccentricity), eccentricity)

    if not (a < 0):
        if not a == float('inf'):
            print(a)
        else:
            print("Error")
        if not b == float('-inf'):
            print(b)
        else:
            print("Error")
        print(c)
        print(center)
    else:
        print("Error")