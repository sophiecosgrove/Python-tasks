
route = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
newroute = []
plannedroute = []

for i in range(len(route)-1):
    if route[i] < route[i + 1]:
        peak = route[i]
        newroute.append(peak)
    else:
        continue

print(newroute)

