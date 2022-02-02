import sys

def loadFile(file):
    results = []
    with open(file, 'r') as f:
        for line in f:
            if(line != 'cookie,timestamp\n'):
                new = []

                words = line.split(',')

                new.append(words[0])
                temp_time = words[1][0:len(words[1])-1]

                time = temp_time.split('T')

                new.append(time[0])
                new.append(time[1])
                results.append(new)
    return results

def processData(day, results):
    correct_day = False
    counters = {}

    for stamp in results:
        if(stamp[1] == day):
            correct_day = True
            if(counters.get(stamp[0]) == None):
                counters[stamp[0]] = 1
            else:
                counters[stamp[0]] +=1
        elif(correct_day == True):
            break
    return counters

def findHighest(counters):
    highest = max(counters.values())
    for cookie in counters:
        if(counters[cookie] == highest):
            print(cookie)

def main():
    argList = sys.argv

    day = argList[3]
    file = argList[1]

    results = loadFile(file)
    counters = processData(day, results)
    findHighest(counters)

if __name__ == "__main__":
    main()