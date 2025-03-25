n=int(input ("Введите число n: ")) 
p=[] #числа от 1 до n
k=[] #квадрат
su=[] #cyммa 
for i in range(1, n+1):
	p+=[i]
print(p)
for i in range(1,n+1):
	k+=[i**2]
print(k)
for i in range (1,n+1):
	su+=[i]
print(sum(su))