import random
gep=[]
while len(gep)<5:
	a=random.randrange(1,91)
	if not (a in gep):
		gep.append(a)
print(gep) 
