def quarter(xcoord, ycoord):
    xcoord = int(input())
    ycoord = int(input())
    if xcoord > 0 and ycoord > 0:
        print("1 четверть")
    elif xcoord < 0 and ycoord > 0:
        print("2 четверть")
    elif xcoord < 0 and ycoord < 0:
        print("3 четверть")
    elif xcoord > 0 and ycoord < 0:
        print("2 четверть")
quarter(xcoord=2, ycoord=1),