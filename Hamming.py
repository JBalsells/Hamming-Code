print "*************************************"
print "***Jorge Augusto Balsells Orellana***"
print "**********carne: 2008-19335**********"
print "************Hamming, k<=11***********"
print "*************************************"

def binarynumber(n):
	y=[]
	while (n>=1):
		y.insert(0,n%2)
		n=n/2
	return y

def creatematrix(a,b):
	matrixfunction=[]
	for i in range(a):
		matrixfunction.append([])
		for j in range(b):
			matrixfunction[i].append(None)
	return matrixfunction

def insertmatrix(imatrix,a,b,val):
	t1=imatrix.pop(a)
	t2=t1.pop(b)
	t1.insert(b,val)
	imatrix.insert(a,t1)
	return imatrix

def printmatrix(pmatrix):
	lon=len(pmatrix)
	for i in range(lon):
		print pmatrix[i]

def identitymatrix(n,idmatrix):
	for i in range(n):
		for j in range(n):
			if (i==j):
				idmatrix=insertmatrix(idmatrix,i,j,1)
			else:
				matig=insertmatrix(idmatrix,i,j,0)
	return idmatrix

print "\r\n"
print "Generacion de Codigo Hamming"
k=int(raw_input("Ingrese valor de K: "))

mat=0
n=1

while (mat<=n):
	mat=((2**(n-k))-1)
	n+=1
n=n-1
print "\r\n Generacion Hamming (%s,%s)"%(n-1,k)
m=n-k-1
print "\r\n Matriz de Paridad (%s,%s)"%(k,m)
matp=creatematrix(k,m)
p=n
for i in range(k):
	if (p!=16 and p!=8 and p!=4 and p!=2 and p!=1 and p!=0):
		tempnum=binarynumber(p)
	else:
		p-=1
		tempnum=binarynumber(p)
	
	tempnum=binarynumber(p)
	
	while(len(tempnum)<m):
		tempnum.insert(0,0)
	for j in range(m):
		matp=insertmatrix(matp,i,j,tempnum[j])
	p-=1	
print printmatrix(matp)

print "\r\n Matriz Identidad (Generadora)(%s,%s)"%(k,k)
matig=creatematrix(k,k)
matig=identitymatrix(k,matig)
print printmatrix(matig)

print "\r\n Matriz Generadora (%s,%s)"%(k,k+m)
matg=creatematrix(k,k+m)
for i in range(k):
	for j in range(k+m):
		if j<k:
			matg[i][j]=matig[i][j]
		else:
			matg[i][j]=matp[i][j-k]					
print printmatrix(matg)

print "\r\n Matriz Identidad (Chequeo de Paridad) (%s,%s)"%(m,m)
matic=creatematrix(m,m)
matic=identitymatrix(m,matic)
print printmatrix(matic)

print "\r\n Matriz de Chequeo de Paridad (%s,%s)"%(k+m,m)
matc=creatematrix(k+m,m)
for i in range(k+m):
	for j in range(m):
		if i<k:
			matc[i][j]=matp[i][j]
		else:
			matc[i][j]=matic[i-k][j]
print printmatrix(matc)

tot=(2**k)-1
print "\r\n Codigo a transmitir: %s posibles datos"%tot
i=0
while i<=tot:
	val=binarynumber(i)
	while(len(val)<k):
		val.insert(0,0)
	cod=[]
	while(len(cod)<m):
		cod.insert(0,0)
	print "Dato No. %s: %s"%(i,val)
	i+=1

t=int(raw_input("\r\n ingrese mensaje a transmitir: (No. de fila de Datos, valores de %s a %s )  "%(0,tot)))
val=binarynumber(t)
while(len(val)<k):
	val.insert(0,0)	
	
for i in range(k):
	if val[i]==1:
		cod=matp[i]

print "Mensaje a transmitir: %s"%(val)
val=val+cod
e=int(raw_input("\r\n Ingrese posicion de error en mensaje: (No. de %s a %s)  "%(0,n-2)))

err=[]
for i in range(n-1):
	if i==e:
		err.insert(n,1)
	else:
		err.insert(n,0)
print "Vector de Error: %s"%err
print "\r\n vector de mensaje:"
print "\r\n  %s \r\n +%s"%(val,err)
print "  _________________________________________________  "

matt=[]
for i in range(n-1):
	matt.insert(n,val[i])
	if err[i]==1:
		if matt[i]==1:
			matt[i]=0
		else:
			matt[i]=1
print "  %s"%matt
print "\r\n mensaje Recibido: %s"%matt

print "\r\n Matriz de Chequeo de Paridad (%s,%s)"%(k+m,m)
print printmatrix(matc)

fin=raw_input("presione una tecla para continuar")
