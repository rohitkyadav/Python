p = int(input("Enter the initial amount: "))
r = int(input("Enter the rate: "))
t = int(input("Enter the number of months: "))
interest = (p*r)/100
for x in range(t):
	p += interest

print(total_money)