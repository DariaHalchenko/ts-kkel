#1
#for
#r=0
#for i in range(15):
#    arv=float(input("Sisesta {0}.arv ".format(i+1)))
#    if arv==int(arv):
#        r+=1
#print("Täisarvude arv on "+str(r))
##while True
#r=0
#i=1
#while True:
#    i+=1
#    arv=float(input("Sisesta {0}.arv ".format(i)))
#    if arv==int(arv):
#        r+=1
#    if i==15: break
#print("Täisarvude arv on"+str(r))
##while i<15:
#r=0
#i=0
#while i<15:
#    i+=1
#    arv=float(input("Sisesta {0}.arv ".format(i)))
#    if arv==int(arv):
#        r+=1
#print("Täisarvude arv on"+str(r))

#2
A=int(input("Sisesta number: sum"))
summa=0
for i in range(1, A+1):
    arv=float(input("Sisesta {0}.arv ".format(i+1)))
    if arv==int(arv):
        A+=1
print("Täisarvude arv on "+str(A))
#while True
A=0
i=1
while True:
    i+=1
    arv=float(input("Sisesta {0}.arv ".format(i)))
    if arv==int(arv):
        A+=1
    if i==1: break
print("Täisarvude arv on"+str(A))
#while i<15:
A=0
i=0
while i<A+1:
    i+=1
    arv=float(input("Sisesta {0}.arv ".format(i)))
    if arv==int(arv):
        A+=1
print("Täisarvude arv on"+str(A))
