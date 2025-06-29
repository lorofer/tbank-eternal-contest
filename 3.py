n, t = map(int, input().split())

floors = input().split()
floors = list(map(int, floors))

leavingColleagueIndex = int(input())


lowerFloor = floors[0]
upperFloor = floors[-1]
leavingColleagueFloor = floors[leavingColleagueIndex - 1]

if (leavingColleagueFloor - lowerFloor <= t) or (upperFloor - leavingColleagueFloor <= t):
	print(upperFloor - lowerFloor)
else:
	if (leavingColleagueFloor - lowerFloor) < (upperFloor - leavingColleagueFloor):
		print(leavingColleagueFloor - lowerFloor + upperFloor - lowerFloor)
	else:
		print(upperFloor - leavingColleagueFloor + upperFloor - lowerFloor)