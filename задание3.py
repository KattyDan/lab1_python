n=int (input ("число n"))
ob=[] #обратный порядок
while n>1:
	ob+=[n]
	n=n-1
	if n==1:
		ob+=[n]
print (ob)

n=int (input ("чило n"))
fa=1 #факториал
while n>0:
	fa*=n
	n-=1
print (fa)