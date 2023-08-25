#!/usr/bin/env python3

from Lexer import Lexer



class PS:

  h="0123456789ABCDEF"

  def __init__(self):

    self.m=bytearray([0 for _ in range(0x10000)])

    self.mp=0



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


  @staticmethod
  def gins(a):
    s=""
    b0=self.gb(a)
    if b0==0x00:
      h0=PS.itoa(b0,16,2)
      s+=h0+" NO"
      a+=1
    elif b0==0x01:
      h0=PS.itoa(b0,16,2)
      s+=h0+" AD"
      a+=1
    elif b0==0x02:
      h0=PS.itoa(b0,16,2)
      s+=h0+" SB"
      a+=1
    elif b0==0x03:
      h0=PS.itoa(b0,16,2)
      s+=h0+" PH"
      a+=1
    elif b0==0x04:
      h0=PS.itoa(b0,16,2)
      s+=h0+" PP"
      a+=1
    elif b0==0x05:
      b1=self.gw(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,4)
      s+=h0+" "+h1+" MA"
      self.a+=3
    elif b0==0x06:
      b1=self.gw(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,4)
      s+=h0+" "+h1+" AM"
      self.a+=3
    elif b0==0x07:
      b1=self.gb(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,2)
      s+=h0+" "+h1+" IA"
      self.a+=3
    elif b0==0x08:
      h0=PS.itoa(b0,16,2)
      s+=h0+" IN"
      a+=1
    elif b0==0x09:
      h0=PS.itoa(b0,16,2)
      s+=h0+" DE"
      a+=1
    elif b0==0x0A:
      b1=self.gw(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,4)
      s+=h0+" "+h1+" JP"
      self.a+=3
    elif b0==0x0B:
      b1=self.gw(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,4)
      s+=h0+" "+h1+" SO"
      self.a+=3
    elif b0==0x0C:
      b1=self.gb(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,2)
      s+=h0+" "+h1+" CP"
      self.a+=3
    elif b0==0x0D:
      b1=self.gb(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,2)
      s+=h0+" "+h1+" JE"
      self.a+=3
    elif b0==0x0E:
      b1=self.gb(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,2)
      s+=h0+" "+h1+" JN"
      self.a+=3
    elif b0==0x0F:
      b1=self.gb(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,2)
      s+=h0+" "+h1+" JG"
      self.a+=3
    elif b0==0x10:
      b1=self.gb(a+1)
      h0=PS.itoa(b0,16,2)
      h1=PS.itoa(b1,16,2)
      s+=h0+" "+h1+" JL"
      self.a+=3
    elif b0==0x11:
      h0=PS.itoa(b0,16,2)
      s+=h0+" BR"
      a+=1











       

  def ginp(self):

    q=False
    
    while not q:

      c=input("> ")

      lexer=Lexer(c)
      t=lexer.lex()
      p0=P0(t)
      p0.eval()



ps=PS()

ps.ginp()


