p = int(input("Enter the initial amount: "))
r = int(input("Enter the rate: "))
t = int(input("Enter the number of months: "))
interest = (p*r)/100
for x in range(t):
	total_money = p + interest
	p = total_money
print(total_money)
