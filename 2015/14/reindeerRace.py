#  -- reindeer race --
with open('1415input.txt', 'r') as file:
    capabilties = file.readlines()

    
def countKM(speed, stamina, rest):
    seconds = 0
    coveredKM = 0
    running = True
    raceLength = 2503
    while seconds < raceLength:
        if running:
            for _ in range(stamina):
                if seconds >= raceLength:
                    break
                coveredKM += speed
                seconds += 1
            running = False
        else:
            seconds += min(rest, raceLength - seconds)
            running = True
    return coveredKM


def main(code):
    winner = 0
    for line in code:
        reindeer = line.split()
        coveredKM = countKM(int(reindeer[3]), int(reindeer[6]), int(reindeer[-2]))
        if coveredKM > winner:
            winner = coveredKM
    return winner


print(main(capabilties))