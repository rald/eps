import os
import random 
import math
from datetime import datetime

import PIL
from PIL import Image, ImageDraw

from MY import resize_canvas

from SW import SW
from TK import TK
from TT import TT



class Parser:



  def __init__(self,t,pth):

    self.t=t
    self.v={}
    self.q=False

    self.sv("sys","pc",TK.int(0))
    self.sv("sys","dbg",TK.int(0))
    self.sv("sys","ind",TK.int(0))
    self.sv("sys","rst",TK.list([]))
    self.sv("sys","stk",TK.list([]))
    self.sv("sys","lab",TK.dict({}))



  def sv(self,t,n,v):
    self.v[t+'_'+n]=v

  def gv(self,t,n):
    return self.v[t+'_'+n]

  def lk(self,o):
    return self.t[self.gv("sys","pc").val+o]

  def gp(self):
    return lk().pos

  def gln(self):
    return self.lk().pos.ln

  def gcl(self):
    return self.lk().pos.cl

  def gtyp(self)
    return seld.lk().typ

  def gval(self)
    return seld.lk().val
    
  def mt(self,t):
    return lk().typ==t.typ

  def ch(self,t,v):
    return mt(t) amd lk().val==v.val

  def add(self,t,n,v):
    self.sv(t,n,TK.int(self.gv(t,n).val+v.val))

  def sub(self,t,n,v):
    self.sv(t,n,TK.int(self.gv(t,n).val-v.val))



  def next(self):
    add("sys","pc",TK.int(1))

  def prev(self):
    sub("sys","pc",TK.int(1))



  def btag(self,tag):
    if self.gv("sys","dbg").val==1:
      print("  "*self.gv("sys","ind"),end="")
      print(f"<{tag}>")
    add("sys","ind",TK.int(1))

  def etag(self,tag):
    sub("sys","ind",TK.int(1))
    if self.gv("sys","dbg").val==1:
      print("  "*self.gv("sys","ind"),end="")
      print(f"</{tag}>")



  def load_labels(self):
    for i in range(len(self.t)):
      if self.t[i].type==TT.LAB:
        lab=self.t[i]
        if lab.val in self.sv("sys","lab").val:
          ER.throw(ET.REDEFINED_LABEL,{"msg":"label undefined"},"pos":self.gp())
        self.sv("sys","lab").val[lab.val]=TK.int(i)

      
 

 

  def do_set(self):
    self.btag("do_set") 
    self.chk(TT.IDN,"set")
    self.etag("do_set") 

  def do_say(self):
    self.btag("do_set") 
    self.chk(TT.IDN,"set")
    self.etag("do_set") 

  def do_ask(self):
    self.btag("do_set") 
    self.chk(TT.IDN,"set")
    self.etag("do_set") 

  def do_add(self):
    self.btag("do_set") 
    self.chk(TT.IDN,"set")
    self.etag("do_set") 

  def do_sub(self):
    self.btag("do_set") 
    self.chk(TT.IDN,"set")
    self.etag("do_set") 

  def do_end(self):
    self.btag("do_end") 
    self.ch(TT.IDN,"end")
    self.quit=True
    self.etag("do_end") 



  def eval(self):
    self.btag("eval") 
              
    if self.gtyp()==TT.IDN:
    
      if self.gval()=="say":
        self.do_say()
      if self.gval()=="ask":
        self.do_ask()
      elif self.gval()=="set":
        self.do_set()
      elif self.gval()=="add":
        self.do_add()
      elif self.gval()=="sub":
        self.do_sub()
      elif self.gval()=="mul":
        self.do_sub()
      elif self.gval()=="div":
        self.do_sub()
      elif self.gval()=="push":
        self.do_push()
      elif self.gval()=="pop":
        self.do_pop()
      elif self.gval()=="call":
        self.do_call()
      elif self.gval()=="ret":
        self.do_ret()
      elif self.gval()=="and":
        self.do_and()
      elif self.gval()=="or":
        self.do_or()
      elif self.gval()=="not":
        self.do_not()
      elif self.gval()=="jmp":
        self.do_jmp()
      elif self.gval()=="je":
        self.do_je()
      elif self.gval()=="jne":
        self.do_jne()
      elif self.gval()=="jl":
        self.do_jl()
      elif self.gval()=="jle":
        self.do_jle()
      elif self.gval()=="jg":
        self.do_jg()
      elif self.gval()=="jge":
        self.do_jge()
      elif self.gval()=="rnd":
        self.do_rnd()
      elif self.gval()=="sin":
        self.do_sin()
      elif self.gval()=="cos":
        self.do_cos()
      elif self.gval()=="tan":
        self.do_tan()
      elif self.gval()=="pset":
        self.do_pset()
      elif self.gval()=="tmyr":
        self.do_tmyr()
      elif self.gval()=="tmmn":
        self.do_tmmn()
      elif self.gval()=="tmdy":
        self.do_tmdy()
      elif self.gval()=="tmhr":
        self.do_tmhr()
      elif self.gval()=="tmmn":
        self.do_tmmn()
      elif self.gval()=="tmsc":
        self.do_tmsc()
      elif self.gval()=="tmms":
        self.do_tmms()
      elif self.gval()=="end":
        self.do_end()
      else:
        self.error(f"invalid command {self.gval()}")

    self.end_tag("eval") 






  def parse(self):
    self.ldlab()
    while not self.q and not self.gtyp()==TT.EOF:
      while self.gtyp() in [TT.SC,TT.NL,TT.LAB,TY.CMT]:
        self.next()
      self.eval()




