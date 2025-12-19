#  -- reindeer race --
with open('1415input.txt', 'r') as file:
    capabilties = file.readlines()

    
def countKM(speed, stamina, rest, raceLength):
    seconds = 0
    coveredKM = 0
    running = True
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


def race(code, raceLength):
    distances = {}
    for line in code:
        reindeer = line.split()
        name = reindeer[0]
        speed = int(reindeer[3])
        stamina = int(reindeer[6])
        rest = int(reindeer[-2])
        distances[name] = countKM(speed, stamina, rest, raceLength)
    return distances


winners = {'Vixen': 0, 'Rudolph': 0, 'Donner': 0, 'Blitzen': 0, 'Comet': 0, 'Cupid': 0, 'Dasher': 0, 'Dancer': 0, 'Prancer': 0}


def main(code):
    i = 1
    while i <= 2503:
        distances = race(code, i)
        winner = max(distances.values())
        for name, dist in distances.items():
            if dist == winner:
                winners[name] += 1
        i += 1

main(capabilties)
print(winners)