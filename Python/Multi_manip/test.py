l=["192.168.1.1",5,9,8]
for i in range (0,len(l)):
    a=l[i]
    print("Number", i+1, "is", a)
for i in range (0,4):
    l[i]=1
for i in range (0,4):
    print(l[i])