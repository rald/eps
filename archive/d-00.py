#!/usr/bin/env python3

class PS:



  h="0123456789ABCDEF"



  def __init__(self):

    self.m=bytearray([0 for _ in range(0xFFFF)])
    self.mp=0
    self.dp=0

    self.i=0
    self.c=0

  

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
      d=PS.h[n%b]+d
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

        n=PS.fnd(PS.h,s[i])
        if n==-1:
          raise Exception("atoi: invalid digit")      
        d+=n*pow(b,j)
        j+=1

    return d
      


  def gb(self,a):
    return self.m[a]



  def gw(self,a):
    return self.m[a]+self.m[a+1]*256



  def gins(self,a):
    s=""
    if self.gb(a)==0x00:
      s+="NO"
      a+=1 
    elif self.gb(a)==0x01:
      s+="AD"
      a+=1
    elif self.gb(a)==0x02:
      s+="SU"
      a+=1
    elif self.gb(a)==0x03:
      s+="PH"
      a+=1
    elif self.gb(a)==0x04:
      s+="PP"
      a+=1
    elif self.gb(a)==0x05:
      s+="MA"
      a+=1
      s+=" $"+PS.itoa(gw(a),16,4)
      self.a+=2
    elif self.gb(a)==0x06:
      s+="AM"
      a+=1
    elif self.gb(a)==0x07:
      s+="IA"
      a+=1
      s+=" $"+PS.itoa(gb(a),16,2)
      a+=1
    elif self.gb(a)==0x08:
      s+="IN"
      a+=1
    elif self.gb(a)==0x09:
      s+="DE"
      a+=1
    elif self.gb(a)==0x0A:
      s+="JP"
      a+=1
      s+=" $"+PS.itoa(gw(a),16,4)
      a+=2
    elif self.gb(a)==0x0B:
      s+="SO"
      a+=1
      s+=" $"+PS.itoa(gw(a),16,4)
      a+=2
    elif self.gb(a)==0x0C:
      s+="CP"
      a+=1
      s+=" $"+PS.itoa(gb(a),16,2)
      a+=1
    elif self.gb(a)==0x0D:
      s+="JP"
      a+=1
      s+=" $"+PS.itoa(gw(a),16,4)
      a+=2
    elif self.gb(a)==0x0E:
      s+="JE"
      a+=1
      s+=" $"+PS.itoa(gb(a),16,2)
      a+=1
    elif self.gb(a)==0x0F:
      s+="JN"
      a+=1
      s+=" $"+PS.itoa(gb(a),16,2)
      a+=1
    elif self.gb(a)==0x10:
      s+="JG"
      a+=1
      s+=" $"+PS.itoa(gb(a),16,2)
      a+=1
    elif self.gb(a)==0x11:
      s+="JL"
      a+=1
      s+=" $"+PS.itoa(gb(a),16,2)
      a+=1
    elif self.gb(a)==0x12:
      s+="BR"
      a+=1

    return {"addr":a,"ins":s}      



  def asm(self,a):
    q=False
    c=None
    while not q:
  
      ha=PS.itoa(a,16,4)
      rs=self.gins(a)

      c=input(f"{ha} {rs['ins']} : ")

      c=c.strip()

      if c=="":
        q=True

      return rs



  def gidn(self):
    q=False
    ch=None
    t=""

    while self.i<len(self.c) and self.c[self.i] in [' ',';']:
      self.i+=1

    while not q:

      if self.i<len(self.c):
        ch=self.c[self.i]
      else:
        q=True
        continue

      if self.i<len(self.c) and ch.isalpha():
        t+=ch
      else:  
        q=True
        continue

      if self.i<len(self.c):
        self.i+=1

    return t



  def ghex(self):
    q=False
    ch=None
    t=None

    while self.i<len(self.c) and self.c[self.i].isspace():
      self.i+=1

    while not q:

      if self.i<len(self.c):
        ch=self.c[self.i].upper()
      else:
        q=True
        continue

      if self.i<len(self.c) and (ch>='0' and ch<='9') or (ch>='A' and ch<='F'):
        t=ch if t==None else t+ch
      else:  
        q=True
        continue

    if self.i<len(self.c):
        self.i+=1

    return t



  def gcmd(self):

    q=False
    
    while not q:

      self.i=0
      self.c=input("> ")
      
      idn=self.gidn()
      print(f"idn: '{idn}'")

      if idn=="q":
        q=True
      elif idn=="a":
        self.asm(self.mp)
      elif idn=="d":
        hx0=self.ghex()
        hx1=self.ghex()
        dc0=PS.atoi(hx0,16)        
        dc1=PS.atoi(hx1,16)        
        for i in range(dc0,dc1+1):
          hx=PS.itoa(i,16,4)
          rs=self.gins(i)
          print(f"{hx} {rs['ins']}")
        self.dp=dc1+1
      elif idn=="o":
        hx=self.ghex()
        dc=PS.atoi(hx,16)
        print(f"hex: '{hx}'")
        print(f"dec: '{dc}'")
        self.mp=dc



ps=PS()

ps.gcmd()


