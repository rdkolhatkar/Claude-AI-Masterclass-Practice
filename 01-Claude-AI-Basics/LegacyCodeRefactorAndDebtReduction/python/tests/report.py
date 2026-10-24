# report.py
# Travel report script
# written by intern, june 2022
# TODO: clean this up someday

import datetime

TRIPS = [
    {"nm": "Paris", "dest": "France", "cst": 1200, "days": 5, "ppl": 2},
    {"nm": "Tokyo", "dest": "Japan", "cst": 3400, "days": 10, "ppl": 1},
    {"nm": "Bali", "dest": "Indonesia", "cst": 800, "days": 7, "ppl": 3},
    {"nm": "NYC", "dest": "USA", "cst": 2100, "days": 4, "ppl": 2},
    {"nm": "Sydney", "dest": "Australia", "cst": 2900, "days": 8, "ppl": 1},
]

# global total — used everywhere
totalSpent = 0
tripCount = 0


def doReport(t):
    # does everything — processes one trip and prints it
    global totalSpent
    global tripCount
    n = t["nm"]
    d = t["dest"]
    c = t["cst"]
    dy = t["days"]
    p = t["ppl"]
    cpp = c / p
    dpb = c / dy
    totalSpent = totalSpent + c
    tripCount = tripCount + 1
    print("Trip: " + n + " (" + d + ")")
    print("  Total cost:      $" + str(c))
    print("  People:          " + str(p))
    print("  Cost per person: $" + str(cpp))
    print("  Days:            " + str(dy))
    print("  Daily budget:    $" + str(dpb))
    # warn if expensive
    if c > 1000 and c <= 2000:
        print("  [WARNING] medium cost trip")
    if c > 2000 and c <= 3000:
        print("  [WARNING] high cost trip")
    if c > 3000:
        print("  [WARNING] very high cost trip — review budget")
    print("")


def CalcAvg(tripList):
    # calculates average cost
    x = 0
    for i in tripList:
        x = x + i["cst"]
    a = x / len(tripList)
    return a


def getMostExpensive(lst):
    # find most expensive
    m = lst[0]
    for i in range(0, len(lst)):
        if lst[i]["cst"] > m["cst"]:
            m = lst[i]
    return m


def getShortestTrip(lst):
    # find shortest
    s = lst[0]
    for i in range(0, len(lst)):
        if lst[i]["days"] < s["days"]:
            s = lst[i]
    return s


def printSummary():
    # prints the summary — uses globals
    global totalSpent
    global tripCount
    avg = CalcAvg(TRIPS)
    me = getMostExpensive(TRIPS)
    st = getShortestTrip(TRIPS)
    print("========================================")
    print("SUMMARY")
    print("========================================")
    print("Total trips:      " + str(tripCount))
    print("Total spent:      $" + str(totalSpent))
    print("Average cost:     $" + str(round(avg, 2)))
    print("Most expensive:   " + me["nm"] + " ($" + str(me["cst"]) + ")")
    print("Shortest trip:    " + st["nm"] + " (" + str(st["days"]) + " days)")
    print("Report date:      " + str(datetime.date.today()))
    print("========================================")


# main — just run everything
for t in TRIPS:
    doReport(t)

printSummary()
