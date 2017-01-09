import turtle 

for y in [0, 30, 60]:
	turtle.setposition(0+y, 0+y)
	turtle.clear()
	turtle.delay(100)
	for steps in range(1):
		turtle.circle(100)
		
		
