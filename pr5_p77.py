f= open ('C:/Users/user/Desktop/input.txt','r')
cr=f.read()
print(cr)
f.close()
v=''
for i in range(0,len(cr)):
    if cr[i]=='a' or cr[i]=='A' or cr[i]=='e'or cr[i]=='E'or cr[i]=='u' or cr[i]=='U'or cr[i]=='i'or cr[i]=='I'or cr[i]=='o' or cr[i]=='O':
        v+=str(cr[i])
f = open('C:/Users/user/Desktop/vocale.txt','w')
f.write(str(v))
f.write('\n')
f.write("sunt "+str(len(v))+" vocale")
f.close
f = open('C:/Users/user/Desktop/vocale.txt','r')
print(f.read())
