from tkinter import * 
win=Tk()
win.config(bg="light cyan")
count=0 
def addrec(): 
    f=open("pranav.txt","a") 
    TrainID=s1.get() 
    Station=s2.get() 
    Destination=s3.get() 
    Arrival=s4.get() 
    Departure=s5.get() 
    f.writelines(TrainID.ljust(40)+Station.ljust(20)+Destination.ljust(20)+Arrival.ljust(20)+Departure.ljust(5)+"\n") 
    f.close() 
def last():
    f=open("pranav.txt","r")
    l=f.readlines()  #readlast line
    try:
        l2=l[len(l)-1]
        l1=l2.split()
        s1.set(l1[0]) 
        s2.set(l1[1]) 
        s3.set(l1[2]) 
        s4.set(l1[3]) 
        s5.set(l1[4])
    except IndexError:
        s6.set("No records")
    f.close

def first():
    f=open("pranav.txt","r")
    l=f.readline()  #readlast line
    try:
        l1=l.split()
        s1.set(l1[0]) 
        s2.set(l1[1]) 
        s3.set(l1[2]) 
        s4.set(l1[3]) 
        s5.set(l1[4])
    except IndexError:
        s6.set("No records")
    f.close    
def nextrec(): 
    global count 
    i=0 
    f=open("pranav.txt","r") 
    try: 
         
        while(i<=count): 
            l=f.readline() 
            i=i+1 
 
        m=l.split() 
        s1.set(m[0]) 
        s2.set(m[1]) 
        s3.set(m[2]) 
        s4.set(m[3]) 
        s5.set(m[4]) 
        print(m) 
    except: 
        clear() 
        s6.set("No More Record Found") 
    count=count+1 
    f.close()

def prevrec(): 
    global count 
    i=0 
    f=open("pranav.txt","r")
    if(count<=0):
        s6.set("No previous record")
    else:
        while(i<=count): 
            l=f.readline() 
            i=i+1 
 
        m=l.split() 
        s1.set(m[0]) 
        s2.set(m[1]) 
        s3.set(m[2]) 
        s4.set(m[3]) 
        s5.set(m[4])
        c=c-1 
    f.close()


    
def delrec(): 
    k=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()] 
    f=open("pranav.txt","r") 
    lines=f.readlines() 
    print(lines) 
    print(k) 
    f.close() 
    f=open("pranav.txt","w") 
    for i in lines: 
        m=i.split() 
        print(m) 
        if(m!=k): 
             f.writelines(m[0].ljust(10)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(5)+"\n") 
    f.close() 
def search(): 
    k=s1.get() 
   
    f=open("pranav.txt","r") 
    h=f.readlines() 
    for i in h: 
        j=i.split() 
        if(j[0]==k): 
            print("customer found")  
            print(j) 
            s1.set(j[0]) 
            s2.set(j[1]) 
            s3.set(j[2]) 
            s4.set(j[3]) 
            s5.set(j[4]) 
             
    f.close()         
def update(): 
    a1=s1.get() 
    a2=s2.get() 
    a3=s3.get() 
    a4=s4.get() 
    a5=s5.get() 
    f=open("pranav.txt","r") 
    h=f.readlines() 
    f.close() 
    f=open("pranav.txt","w") 
    for i in h: 
        j=i.split() 
        if(j[0]!=a1): 
            f.writelines(j[0].ljust(3)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n") 
     
        else: 
            f.writelines(j[0].ljust(3)+a2.ljust(20)+a3.ljust(20)+a4.ljust(20)+a5.ljust(5)+"\n") 
     
     
     
     
def clear(): 
    m="" 
    s1.set(m) 
    s2.set(m) 
    s3.set(m) 
    s4.set(m) 
    s5.set(m) 
s1=StringVar() 
s2=StringVar() 
s3=StringVar() 
s4=StringVar() 
s5=StringVar() 
s6=StringVar()
s7=StringVar()
l1=Label(win,text="TrainID",bg="light cyan") 
l2=Label(win,text="Station",bg="light cyan") 
l3=Label(win,text="Destination",bg="light cyan") 
l4=Label(win,text="Arrival",bg="light cyan") 
l5=Label(win,text="Departure",bg="light cyan")
l6=Label(win,text="->",fg="red",bg="light cyan")
l7=Label(win,text=" ",fg="red",bg="light cyan")
l8=Label(win,text=" ",fg="red",bg="light cyan")
l9=Label(win,text=" ",fg="red",bg="light cyan")
l10=Label(win,text="Pranav Sharma ",fg="blue4",bg="light cyan")
l11=Label(win,text="16CSU259",fg="blue4",bg="light cyan")
l12=Label(win,text="INDIAN RAILWAY DATABASE",fg="blue4",bg="light cyan")
l13=Label(win,text=" ",fg="red",bg="light cyan")
t1=Entry(win,textvariable=s1) 
t2=Entry(win,textvariable=s2) 
t3=Entry(win,textvariable=s3) 
t4=Entry(win,textvariable=s4) 
t5=Entry(win,textvariable=s5) 
t6=Entry(win,textvariable=s6) 
b1=Button(win,text="add",command=addrec,fg="blue4",bg="SkyBlue1") 
b2=Button(win,text=">",command=nextrec,fg="dark green",bg="olive drab1") 
b3=Button(win,text="del",command=delrec,fg="blue4",bg="SkyBlue1") 
b4=Button(win,text="search",command=search,fg="blue4",bg="SkyBlue1") 
b5=Button(win,text="update",command=update,fg="blue4",bg="SkyBlue1") 
b6=Button(win,text="clear",command=clear,fg="white",bg="red2")
b7=Button(win,text=">|",command=last,fg="dark green",bg="olive drab1")
b8=Button(win,text="|<",command=first,fg="dark green",bg="olive drab1")
b9=Button(win,text="<",command=prevrec,fg="dark green",bg="olive drab1")
l1.grid(row=3,column=2)
l13.grid(row=2,column=4)
l12.grid(row=1,column=4)
l2.grid(row=4,column=2) 
l3.grid(row=6,column=2) 
l4.grid(row=7,column=2) 
l5.grid(row=5,column=2)
l6.grid(row=8,column=2)
l7.grid(row=9)
l8.grid(row=11,column=2)
l9.grid(row=13,column=2)
l10.grid(row=15,column=6)
l11.grid(row=16,column=6)
t1.grid(row=3,column=4) 
t2.grid(row=4,column=4) 
t3.grid(row=5,column=4) 
t4.grid(row=7,column=4) 
t5.grid(row=6,column=4) 
t6.grid(row=8,column=4)
b1.grid(row=12,column=1) 
b2.grid(row=10,column=5) 
b3.grid(row=12,column=3) 
b4.grid(row=12,column=5) 
b5.grid(row=12,column=6) 
b6.grid(row=14,column=4)
b7.grid(row=10,column=6)
b8.grid(row=10,column=1)
b9.grid(row=10,column=3)
win.mainloop()
