for n in range(5):
	
	#loop over from 0 to 5(exclusive)

	print(n)

	# 0 1 2 3 4


for n in range(3,10):

	print(n)

	# 3 4 5 6 7 8 9

for n in range(0,20,4):
	
	print(n)

	# 0 4 8 12 16

friends = ['prateek','nischal','navneet']

for friend in range(len(friends)):

		print(friend,friends[friend])

############################

# REVERSE LOOP

for n in range(len(friends)-1,-1,-1):
	
	print(n,friends[n])