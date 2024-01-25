#1
#for
#r=0
#for i in range(15):
#    arv=float(input("Sisesta {0}.arv ".format(i+1)))
#    if arv==int(arv):
#        r+=1
#print("Täisarvude arv on "+str(r))

#1.1
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

#1.2
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
#A=int(input("Sisestage number A: "))
#summa=0
#for i in range (1, A+1):
#    A=float(input("Sisestage {0}.number A".format(i+1)))
#    if A==int(A):
#        summa +=1
#print("Kõigi naturaalarvude summa"  +str(summa))

#2.1
#A=int(input("Sisestage number A: "))
#i=1
#summa=0
#while i<=A:
#    i+=1
#    A=float(input("Sisestage {0}.number A".format(i+1)))
#    if A==int(A):
#        summa += i
#print("Kõigi naturaalarvude summa"  +str(summa))

#2.2
#A=int(input("Sisestage number A: "))
#summa=0
#i=1
#while True:
#    i+=1
#    A=float(input("Sisestage {0}.number A ".format(i+1)))
#    if A==int(A):
#        summa+=1
#    if i> A: break
#print("Täisarvude arv on"+str(summa))

#3
#positiivne=1
#for i in range(8):
#    arv=int(input("Sisesta {0}.arv ".format(i+1)))
#    if arv>0:
#        positiivne*=arv 
#print("Positiivsed numbrid on "+str(positiivne))

#3.1
#positiivne=1
#i=0
#while True:
#    arv=float(input("Sisesta {0}.arv ".format(i)))
#    if arv>0:
#        positiivne*=arv
#        i += 1
#    if i ==8:break
#print("Täisarvude arv on "+str(positiivne))

#3.2
#positiivne=1
#i=0
#while i<8:
#    arv=int(input("Sisesta {0}.arv ".format(i)))
#    if arv>0:
#        positiivne*=arv
#        i+=1
#print("Positiivsed numbrid on "+str(positiivne))

#4
#for arv in range(10,20):
#    numbrite_ruut=arv**2
#    print("Numbrite ruut on: "+str(numbrite_ruut))

#4.1
#arv=10 #от 10 начальное значение 
#while True:
#    numbrite_ruut=arv**2
#    print("Numbrite ruut on: "+str(numbrite_ruut))
#    arv+=1
#    if arv>20:break

#4.2
#arv=10 
#while arv<=20:
#    numbrite_ruut=arv**2
#    print("Numbrite ruut on: "+str(numbrite_ruut))
#    arv+=1


#5
#negatiivne=0
#N=int(input("Sisestage number N: "))
#for i in range(N):
#    arv=int(input("Sisesta {0}.arv ".format(i+1)))
#    if arv<0:
#        negatiivne+=arv 
#print("Negatiivsete arvude summa on "+str(negatiivne))

#5.1
#negatiivne=0
#N=int(input("Sisestage number N: "))
#i=1
#while True:
#    arv=float(input("Sisesta {0}.arv ".format(i)))
#    if arv<0:
#        negatiivne+=arv
#        i += 1
#    if i ==N:break
#print("Negatiivsete arvude summa on "+str(negatiivne))

#5.2
#N=int(input("Sisestage number N: "))
#negatiivne=0
#i=0
#while i<N:
#    i+=1
#    arv=float(input("Sisesta {0}.arv ".format(i)))
#    if arv<0:
#        negatiivne+=arv
#        i+=1
#print("Negatiivsete arvude summa on "+str(negatiivne))

#6
#N=int(input("Sisestage number N: "))
#negatiivne=0
#positiivne=0
#nullid=0
#for i in range(N):
#    arv=int(input("Sisesta {0}.arv ".format(i+1)))
#    if arv<0:
#        negatiivne+=1
#    elif arv>0:
#        positiivne+=1
#    else:
#        nullid+=1
#print("Negatiivsete arvude arv: "+str(negatiivne))
#print("Positiivsete arvude arv: "+str(positiivne))
#print("Nullide arv sisestatud numbrite hulgas: "+str(nullid))

#6.1
#negatiivne=0
#positiivne=0
#nullid=0
#while True:
#    arv=int(input("Sisesta {0}.arv "))
#    if arv<0:
#        negatiivne+=1
#    elif arv>0:
#        positiivne+=1
#    elif arv==0:
#        nullid+=1
#        break
#print("Negatiivsete arvude arv: "+str(negatiivne))
#print("Positiivsete arvude arv: "+str(positiivne))
#print("Nullide arv sisestatud numbrite hulgas: "+str(nullid))

#6.2
#N=int(input("Sisestage number N: "))
#negatiivne=0
#positiivne=0
#nullid=0
#while N>0:
#    arv=int(input("Sisesta {0}.arv "))
#    if arv<0:
#        negatiivne+=1
#    elif arv>0:
#        positiivne+=1
#    else:
#        nullid+=1
#    N-=1
#print("Negatiivsete arvude arv: "+str(negatiivne))
#print("Positiivsete arvude arv: "+str(positiivne))
# print("Nullide arv sisestatud numbrite hulgas: "+str(nullid))

#7


#8
#for tolli in range (1,20):
#    sentimeetrit=tolli*2,5
#    print("Tõlge alates"+str(tolli), "tollist="+str(sentimeetrit), "sentimeetriks")

#8.1
#tolli=1
#while True:
#    sentimeetrit=tolli*2,5
#    print("Tõlge alates"+str(tolli), "tollist="+str(sentimeetrit), "sentimeetriks")
#    tolli+=1
#    if tolli>20:break

#8.2
#tolli=1 
#while tolli<=20:
#    sentimeetrit=tolli*2,5
#    print("Tõlge alates"+str(tolli), "tollist="+str(sentimeetrit), "sentimeetriks")
#    tolli+=1

#9
#S=int(input("Panka hoiustati: "))
#N=int(input("Mitu aastat: "))
#for aastat in range(1):
#    kuud=N*12
#    summa=S+((S*0.03)*kuud)
#    print("Sissemakse summa "+str(N), "aasta pärast võrdub "+str(summa), "euroga")

#9.1
#S=int(input("Panka hoiustati: "))
#N=int(input("Mitu aastat: "))
#while True:
#    kuud=N*12
#    summa=S+((S*0.03)*kuud)
#    print("Sissemakse summa "+str(N), "aasta pärast võrdub "+str(summa), "euroga")
#    if N<-1: break
    
#9.2
#S=int(input("Panka hoiustati: "))
#N=int(input("Mitu aastat: "))
#while S> N:
#    kuud=N*12
#    summa=S+((S*0.03)*kuud)
#    print("Sissemakse summa "+str(N), "aasta pärast võrdub "+str(summa), "euroga")


                                      #10
#for i in range(10):
#    print=("Sisesta {0}.arv ".format(i+1))
#    A=int(input("Sisestage number: ")) #первое число для сравнение
#    B=int(input("Sisestage number: ")) #второе число для сравнение
#    if A<B:
#        print("Suurem arv: " +str(B))
#    elif A>B:
#        print("Suurem arv: " +str(A))
#    else :
#        print("Nad on identsed!")

#10.1
#arv=1
#while True:
#    print=("Sisesta {0}.arv ".format(arv+1))
#    A=int(input("Sisestage number: ")) 
#    B=int(input("Sisestage number: "))
#    if A<B:
#        print("Suurem arv: " +str(B))
#    elif A>B:
#        print("Suurem arv: " +str(A))
#    else :
#        print("Nad on identsed!")
#    arv+=1
#    if arv>10: break

#10.2
#arv=1
#while arv<=10:
#    print=("Sisesta {0}.arv ".format(arv+1))
#    A=int(input("Sisestage number: ")) 
#    B=int(input("Sisestage number: "))
#    if A<B:
#        print("Suurem arv: " +str(B))
#    elif A>B:
#        print("Suurem arv: " +str(A))
#    else :
#        print("Nad on identsed!")
#    arv+=1
    
#11

#12 (незнаю)
#N=int(input("Sisestage niidukite arv: "))
#m=int(input("Ühe niiduki tööaeg: "))
#aega=m
#for i in range(2,N+1):
#    aega=m+(i-1)*10
#    brigaad=aega+N
#print("Meeskond töötas " +str(aega), "aega")

#13
#kogus=0
#summa=0
#for arv in range(100,1000):
#    if arv //7==arv/7:     // это для проверки, является ли каждое число кратным 7(целочисленное деление)
#        kogus+=1
#        summa+=arv
#print("Naturaalarvud 100 kuni 1000 кратные 7: " +str(kogus))
#print("Arvude summa: "+str(summa))

#13.1
#kogus=0
#summa=0
#arv=100
#while arv<=1000:
#    if arv //7==arv/7:  #делим на 7
#        kogus+=1
#        summa+=arv
#    arv+=1
#print("Naturaalarvud 100 kuni 1000 кратные 7: " +str(kogus))
#print("Arvude summa: "+str(summa))

#13.2
#kogus=0
#summa=0
#arv=100
#while True:
#    if arv //7==arv/7:  #делим на 7
#        kogus+=1
#        summa+=arv
#    arv+=1
#    if arv>1000:break
#print("Naturaalarvud 100 kuni 1000 кратные 7: " +str(kogus))
#print("Arvude summa: "+str(summa))


#14
#from random import *
#N=randint (1,100)
#arvude_korrutis=1
#for arv in range(1,N+1):
#    arvude_korrutis*=arv
#print("Arvude 1 kuni N korrutis on võrdne: "+str(arvude_korrutis))

#14.1
#from random import *
#N=randint (1,100)
#arvude_korrutis=1
#arv=1
#while True:
#    arvude_korrutis*=arv
#    arv+=1
#    if arv>N:break
#print("Arvude 1 kuni N korrutis on võrdne: "+str(arvude_korrutis))

#14.2
#from random import *
#N=randint (1,100)
#arvude_korrutis=1
#arv=1
#while arv<=N:
#    arvude_korrutis*=arv
#    arv+=1
#print("Arvude 1 kuni N korrutis on võrdne: "+str(arvude_korrutis))


#15

#16

#17
#arv=int(input("Sisestage arv vahemikus 1 kuni 9: "))
#for i in range(1,11):
#    tulemus=arv*i
#    print(arv, "*", i, "=", tulemus)

#17.1
#i=0
#for i in range(1,11):
#    i+=1
#    print("2 *", i, "=", 2*i)

#17.1.1
#i=0
#while i<10:
#    i+=1
#    print("2 *", i, "=", 2*i)

#17.1.2
#arv=int(input("Sisestage arv vahemikus 1 kuni 9: "))
#i=0
#while i<10:
#    i+=1
#    tulemus=arv*i
#    print(arv, "*", i, "=", tulemus)

#17.2.1
#arv=int(input("Sisestage arv vahemikus 1 kuni 9: "))
#i=1
#while True:
#    i+=1
#    tulemus=arv*i
#    if i>10: break
#    print(arv, "*", i, "=", tulemus)

#17.2.2
#i=1
#while True:
#    i+=1
#    if i>10: break
#    print("2*", i, "=", 2*i)


#18
#for arv in range(20,51):
#    if arv%3==0 and arv%5!=0:
#        print("Arvud jaguvad 3-ga, kuid mitte 5-ga:  "+str(arv))
#%-используется для операции взятие остатка от деления. Я делила числа на 3 поэтому написала arv%3, чтобы проверить делится "arv" на 3 
#без остатка. Если остаток равен 0, значит число делится на 3.
# Знак ! используется для обозначение отрицание.
# Знак ! использовала, чтобы показать, что на 5 не должно число делится (не равно).

#18.1
#arv=20
#while arv <=50:
#    if arv%3==0 and arv%5!=0:
#        print("Arvud jaguvad 3-ga, kuid mitte 5-ga:  "+str(arv))
#    arv+=1

#18.2
#arv=20
#while True:
#    if arv%3==0 and arv%5!=0:
#        print("Arvud jaguvad 3-ga, kuid mitte 5-ga:  "+str(arv))
#    arv+=1
#    if arv>50:break


#19
#for arv in range(35,88):
#    if arv%7 in {1,2,5}:
#        print("Arvud, mis on jagatud 7-ga, jätavad 1,2 ja 5:  " +str(arv))
#arv%7==1 or arv%7==2 or arv%7==5 
# or- можно использовать для того, чтобы объединить условий. Оr показывает, если одно из условий истинно.

#19.1
#arv=35
#while arv <=87:
#    if arv%7 in {1,2,5}:
#        print("Arvud, mis on jagatud 7-ga, jätavad 1,2 ja 5:  " +str(arv))  
#    arv+=1  

#19.2
#arv=35
#while True:
#    if arv%7 in {1,2,5}:
#        print("Arvud, mis on jagatud 7-ga, jätavad 1,2 ja 5:  " +str(arv)) 
#    arv+=1 
#    if arv>87: break


#20
#summa=0
#for arv in range(1,51):
#    if arv%7 and arv%7:
#        summa+=arv
#print("Arvude summa: " +str(summa))

#20.1
#summa=0
#arv=1
#while arv <=50:
#    if arv%7 and arv%7:
#        summa+=arv
#    arv+=1
#print("Arvude summa: " +str(summa))

#20.2
#summa=0
#arv=1
#while True:
#    if arv%7 and arv%7:
#        summa+=arv
#    arv+=1
#    if arv>50: break
#print("Arvude summa: " +str(summa))


#21


#22
#summa=0
#for arv in range(100,201):
#    if arv%17==0:
#        summa+=arv
#print("Arvude summa vahemikus 100 kuni 200, mis on 17 kordsed:  "+str(summa))

#22.1
#summa=0
#arv=100
#while arv<=200:
#    if arv%17==0:
#        summa+=arv
#    arv+=1
#print("Arvude summa vahemikus 100 kuni 200, mis on 17 kordsed:  "+str(summa))

#22.2
#summa=0
#arv=100
#while True:
#    if arv%17==0:
#        summa+=arv
#    arv+=1
#    if arv>200: break
#print("Arvude summa vahemikus 100 kuni 200, mis on 17 kordsed:  "+str(summa))


#23


#24

#25

#26

#27

#28


#29

#30

#31
