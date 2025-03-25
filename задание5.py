import random
s=[]
for i in range (20):
	s+=[random. randint (1,100)]
ch=[] #четные
d3=[] #делятся на 3
for i in s:
	if i%2==0:
		ch+=[i]
	if  i%3==0:
		d3+=[i]
sr=sum(s)/len(s) #среднее арифм
print(s)
print(ch)
print(d3)
print(sr)