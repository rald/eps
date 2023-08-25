#!/usr/bin/env python3

import re



class debug:

  h="0123456789ABCDEF"

  def __init__(self):

    self.m=bytearray([0x00 for _ in range(0x10000)])

    self.org=0x0000

    self.ml=0x0000
    self.mh=0xFFFF

    self.ph=self.mh
    self.pl=self.ph-1

    self.ah=self.pl-1
    self.al=self.ah-1

    self.sh=self.al-1
    self.sl=self.sh-1

    self.sth=self.sl-1
    self.stl=self.sth-1024

    self.fbh=self.stl-1
    self.fbl=self.fbh-4095

    self.srsp(self.sth)
    self.srpc(self.org)

    print("mh =",self.itoa(self.mh,16,4))
    print("ml =",self.itoa(self.ml,16,4))

    print("ph =",self.itoa(self.ph,16,4))
    print("pl =",self.itoa(self.pl,16,4))

    print("ah =",self.itoa(self.ah,16,4))
    print("al =",self.itoa(self.al,16,4))
 
    print("sh =",self.itoa(self.sh,16,4))
    print("sl =",self.itoa(self.sl,16,4))

    print("sth =",self.itoa(self.sth,16,4))
    print("stl =",self.itoa(self.stl,16,4))

    print("fbh =",self.itoa(self.fbh,16,4))
    print("fbl =",self.itoa(self.fbl,16,4))



  @staticmethod
  def fnd(s,c):
    i=0
    j=-1
    while i<len(s):
      if s[i]==c:
        j=i
        break
      i+=1
    return j    



  @staticmethod
  def itoa(n,b,p=0):
    d=""
    q=False
    while not q:
      d=debug.h[n%b]+d
      n=int(n/b)
      if n<=0:
        q=True
    l=p-len(d)
    d=(l if l>0 else 0)*"0"+d
    return d



  @staticmethod
  def atoi(s,b):
    d=0
    q=False
    i=len(s)
    j=0
    while not q:
      if i<=0:
        q=True
      else:
        i-=1

        n=debug.fnd(debug.h,s[i])
        if n==-1:
          raise Exception("atoi: invalid digit")      
        d+=n*pow(b,j)
        j+=1

    return d



  def grpl(self):
    return self.m[self.pl]

  def grph(self):
    return self.m[self.ph]

  def grpc(self):
    return (self.grpl()+self.grph()*256)%65536



  def srpl(self,v):
    self.m[self.pl]=v

  def srph(self,v):
    self.m[self.ph]=v

  def srpc(self,v):
    self.m[self.pl]=v%256
    self.m[self.ph]=int(v/256)%256



  def gral(self):
    return self.m[self.al]

  def grah(self):
    return self.m[self.ah]

  def grax(self):
    return (self.gral()+self.grah()*256)%65536



  def sral(self,v):
    self.m[self.al]=v

  def srah(self,v):
    self.m[self.ah]=v

  def srax(self,v):
    self.m[self.al]=v%256
    self.m[self.ah]=int(v/256)%256


 
  def grsl(self):
    return self.m[self.sl]

  def grsh(self):
    return self.m[self.sh]

  def grsp(self):
    return (self.grsl()+self.grsh()*256)%65536



  def srsl(self,v):
    self.m[self.sl]=v

  def srsh(self,v):
    self.m[self.sh]=v

  def srsp(self,v):
    self.m[self.sl]=v%256
    self.m[self.sh]=int(v/256)%255



  def gb(self,a):
    return self.m[a]%256

  def gw(self,a):
    return (self.m[a+0]+self.m[a+1]*256)%65536
 
    

  def gins(self,a):
    s=""
    b0=self.m[a]
    h0=debug.itoa(b0,16,2)
    if b0==0x00:
      s+=h0+"      NO"
      a+=1
    elif b0==0x01:
      h0=debug.itoa(b0,16,2)
      s+=h0+"      AD"
      a+=1
    elif b0==0x02:
      h0=debug.itoa(b0,16,2)
      s+=h0+"      SU"
      a+=1
    elif b0==0x03:
      h0=debug.itoa(b0,16,2)
      s+=h0+"      PU"
      a+=1
    elif b0==0x04:
      h0=debug.itoa(b0,16,2)
      s+=h0+"      PO"
      a+=1
    elif b0==0x05:
      b1=self.gw(a+1)
      h1=debug.itoa(b1,16,4)
      s+=h0+" "+h1+" MA "+h1
      a+=3
    elif b0==0x06:
      b1=self.gw(a+1)
      h1=debug.itoa(b1,16,4)
      s+=h0+" "+h1+" AM "+h1
      a+=3
    elif b0==0x07:
      b1=self.gb(a+1)
      h1=debug.itoa(b1,16,2)
      s+=h0+" "+h1+"   IA "+h1
      a+=2
    elif b0==0x08:
      s+=h0+"      IN"
      a+=1
    elif b0==0x09:
      h0=debug.itoa(b0,16,2)
      s+=h0+"      DE"
      a+=1
    elif b0==0x0A:
      b1=self.gw(a+1)
      h1=debug.itoa(b1,16,4)
      s+=h0+" "+h1+" JU "+h1
      a+=3
    elif b0==0x0B:
      b1=self.gw(a+1)
      h1=debug.itoa(b1,16,4)
      s+=h0+" "+h1+" SO "+h1
      a+=3
    elif b0==0x0C:
      b1=self.gb(a+1)
      h1=debug.itoa(b1,16,2)
      s+=h0+" "+h1+"   CO "+h1
      a+=2
    elif b0==0x0D:
      b1=self.gb(a+1)
      h1=debug.itoa(b1,16,2)
      s+=h0+" "+h1+"   JE "+h1
      a+=2
    elif b0==0x0E:
      b1=self.gb(a+1)
      h1=debug.itoa(b1,16,2)
      s+=h0+" "+h1+"   JN "+h1
      a+=2
    elif b0==0x0F:
      b1=self.gb(a+1)
      h1=debug.itoa(b1,16,2)
      s+=h0+" "+h1+"   JG "+h1
      a+=2
    elif b0==0x10:
      b1=self.gb(a+1)
      h1=debug.itoa(b1,16,2)
      s+=h0+" "+h1+"   JL "+h1
      a+=2
    elif b0==0x11:
      s+=h0+"      BR"
      a+=1
    return {"a":a,"s":s}



  def nx(self,v=1):
    self.srpc(self.grpc()+v)

  def pv(self,v=1):
    self.srpc(self.grpc()-v)



  def una(self,a0,a1):
    i=a0
    while i<=a1:
      r=self.gins(i)
      print(debug.itoa(i,16,4)+":",r["s"])
      i=r["a"]



  def mw1(self,v0):
    self.m[self.grpc()+0]=v0
    self.nx()

  def mw2(self,v0,v1):
    self.m[self.grpc()+0]=v0
    self.m[self.grpc()+1]=v1
    self.nx(2)
    
  def mw3(self,v0,v1,v2):
    self.m[self.grpc()+0]=v0
    self.m[self.grpc()+1]=v1
    self.m[self.grpc()+2]=v2
    self.nx(3)



  def mr1(self):
    v=self.m[self.grpc()+0]
    self.nx()
    return v

  def mr2(self):
    v=self.m[self.grpc()+0]+self.m[self.grpc()+1]*256
    self.nx(2)
    return v



  def save(self,fn):
    f=open(fn,"wb")
    f.write(self.m)
    f.close()



  def load(self,fn):
    f=open(fn,"rb")
    self.m=bytearray(f.read(65536))
    f.close()






  def dmp(self,s,e):
    for i in range(s,e+1):
      print(debug.itoa(i,16,4),debug.itoa(self.m[i],16,2))



  def regs(self):
    print("REGS:")
    print(
      "AX =",debug.itoa(self.grax(),16,4),
      "AL =",debug.itoa(self.gral(),16,2),
      "AH =",debug.itoa(self.grah(),16,2)
    )
    
    print(
      "SP =",debug.itoa(self.grsp(),16,4),
      "SL =",debug.itoa(self.grsl(),16,2),
      "SH =",debug.itoa(self.grsh(),16,2)
    )



  def stk(self):
    print("STACK:")
    s=""
    j=0
    for i in range(self.stl,self.sth+1):
      if j!=0 and j%16==0: 
        print(f"'{s}'")
        s=""
      if j%16==0: print(debug.itoa(i,16,2),end=": ")
      if self.grsp()==i:
        print("<",debug.itoa(self.m[i],16,2),">",sep="",end="")
      else:
        if j%8==0: print(" ",end="") 
        print(debug.itoa(self.m[i],16,2),end="")
        if self.grsp()-1!=i: print(" ",end="")
      c=chr(self.m[i])
      if c.isspace() or not c.isprintable(): c='.'
      s+=c
      j+=1
    print(f"'{s}'")
        


  def start(self):

    q=False
    
    while not q:

      pc=debug.itoa(self.grpc(),16,4)

      c=input(f"{pc} > ")

      t=c.upper().split()
      t=[x.strip() for x in t if x.strip()]

      if len(t)==1:
        if t[0]=="Q":
          q=True
        elif t[0]=="R":
          self.regs()
        elif t[0]=="S":
          self.stk()
        elif t[0]=="RAX":
          print(debug.itoa(self.grax(),16,4))
        elif t[0]=="RSP":
          print(debug.itoa(self.grsp(),16,4))
        elif t[0]=="NO":
          self.mw1(0x00)
        elif t[0]=="AD":
          self.mw1(0x01)
        elif t[0]=="SU":
          self.mw1(0x02)
        elif t[0]=="PU":
          self.mw1(0x03)
        elif t[0]=="PO":
          self.mw1(0x04)
        elif t[0]=="IN":
          self.mw1(0x08)
        elif t[0]=="DE":
          self.mw1(0x09)
        elif t[0]=="BR":
          self.mw1(0x11)
      elif len(t)==2:
        if len(t[1])==2:
          if t[0]=="IA":
            self.mw2(0x07,debug.atoi(t[1],16)%256)
          elif t[0]=="CO":
            self.mw2(0x0C,debug.atoi(t[1],16)%256)
          elif t[0]=="JE":
            self.mw2(0x0D,debug.atoi(t[1],16)%256)
          elif t[0]=="JN":
            self.mw2(0x0E,debug.atoi(t[1],16)%256)
          elif t[0]=="JG":
            self.mw2(0x0F,debug.atoi(t[1],16)%256)
          elif t[0]=="JL":
            self.mw2(0x10,debug.atoi(t[1],16)%256)
        elif len(t[1])==4:
          if t[0]=="RAX":
            self.srax(debug.atoi(t[1],16))
          elif t[0]=="RSP":
            self.srsp(debug.atoi(t[1],16))
          elif t[0]=="ORG":
            self.srpc(debug.atoi(t[1],16))
          elif t[0]=="SAVE":
            self.save(t[1])
          elif t[0]=="LOAD":
            self.load(t[1])
          elif t[0]=="MA":
            self.mw3(0x05,
              debug.atoi(t[1],16)%256,
              int(debug.atoi(t[1],16)/256)%256,
            )
          elif t[0]=="AM":
            self.mw3(0x06,
              debug.atoi(t[1],16)%256,
              int(debug.atoi(t[1],16)/256)%256,
            )
          elif t[0]=="JU":
            self.mw3(0x0A,
              debug.atoi(t[1],16)%256,
              int(debug.atoi(t[1],16)/256)%256,
            )
          elif t[0]=="SO":
            self.mw3(0x0B,
              debug.atoi(t[1],16)%256,
              int(debug.atoi(t[1],16)/256)%256,
            )
      elif len(t)==3:
        if t[0]=="D":
          a0=debug.atoi(t[1],16)
          a1=debug.atoi(t[2],16)
          self.dmp(a0,a1)
        if t[0]=="U":
          a0=debug.atoi(t[1],16)
          a1=debug.atoi(t[2],16)
          self.una(a0,a1)
      elif len(t)>=3:
        if t[0]=="E":
          i=debug.atoi(t[1],16)
          for j in range(2,len(t)):
            self.m[i+j-2]=debug.atoi(t[j],16)%256                    
        


      

debug=debug()

debug.start()

