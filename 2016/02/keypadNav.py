with open('0216input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

    print(data)

    num = 5

    # 1 2 3 
    # 4 5 6 
    # 7 8 9

    # L R U D

    #0,0 - 0,1 - 0,2
    #1,0 - 1,1 - 1,2
    #2,0 - 2,1 - 2,2

    for i in range(10):
        try:
            print('hello')
        except (IndexError, KeyError):
            # ignore this one and move on
            continue

    #if instruction not exist, ignore. return the number you land on after each line. start on 5