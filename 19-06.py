def find_farthest_orbit(orbits):
    s = [3.14*max(x) for x in orbits]
    return(orbits[s.index(max(s))])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))