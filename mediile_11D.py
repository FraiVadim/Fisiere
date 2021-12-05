f= open('D:\school\INFOSHA\Lista clasei 11D.txt', 'r')
lst = list(f)
while True:
    linie = f.readline()
    if len(linie)==0:
        break
    print (linie,end="")
f.close()

for i in range (len(lst)):
    cimpuri = linie.split()
    print(i + 1, '\t', lst[i])

f= open('D:\school\INFOSHA\Lista clasei 11D.txt', 'a')
n = media = ngr1 = ngr2 = media1gr = media2gr = 0
print('Nume', 'Prenume','Nota', sep='\t')
for linie in lst:
    cimpuri = linie.split()
    nota = int(cimpuri[2])
    n , media= n+1, media+nota
    print(cimpuri[0], cimpuri[1], nota, sep='\t')
    if cimpuri[3]=='gr1':
        ngr1 , media1gr = ngr1+1 , media1gr+nota
    else:
        ngr2 , media2gr = ngr2+1 , media2gr+nota
line1=('\n'+'Media celor '+ str(n)+ ' studenti este '+ str(media/float(n)))
line2=('\n'+'Media celor '+ str(ngr1)+ ' studenti din prima grupa este '+ str(media1gr/float(ngr1)))
line3=('\n'+'Media celor '+ str(ngr2)+ ' studenti din a doua grupa este '+ str(media2gr/float(ngr2)))
f.write(str(line1))
f.write(str(line2))
f.write(str(line3))
f.close()