def name():
	print("python")



def decorator(f):
	def wrapper():
		print("inside of decorator before calling thr function.")
		f()
		print("inside of decorator before calling thr function.")
	return wrapper

@decorator
def name():
	print("python")




def decorator(f):
	
	def wrapper(*args, **kwargs):
		print("inside of decorator before calling thr function.")
		
		f(*args, **kwargs)
		
		print("inside of decorator before calling thr function.")
	
	return wrapper

@decorator
def name(name):
	print(name)
