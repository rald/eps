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



  def __init__(self,t,p):

    self.q=False
    self.t=t
    self.tp=0
    self.m=bytearray([0 for _ in range(0xffff)])
    self mp=0



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
      


  def lk(self,o=0):
    return self.t[self.tp+o] 

  def gv(self):
    return self.lk().val

  def gt(self):
    return self.lk().typ

  def chk(self,t,v):
    if self.gt()!=t.typ or self.gv()!=v:
      raise Exception("chk")

  def nx(self):
    if self.tp>=len(self.t):
      raise Exception("nx")
    self.tp+=1



  def do_no(self):
    self.btag("do_no") 
    self.chk(TT.IDN,"no")
    self.m[self.mp]=0x00
    self.mp+=1
    self.nx()
    self.etag("do_no") 

  def do_ad(self):
    self.btag("do_ad") 
    self.chk(TT.IDN,"ad")
    self.m[self.mp]=0x01
    self.mp+=1
    self.nx()
    self.etag("do_ad") 

  def do_sb(self):
    self.btag("do_sb") 
    self.chk(TT.IDN,"sb")
    self.m[self.mp]=0x02
    self.mp+=1
    self.nx()
    self.etag("do_sb")

  def do_ph(self):
    self.btag("do_ph") 
    self.chk(TT.IDN,"ph")
    self.m[self.mp]=0x03
    self.mp+=1
    self.nx()
    self.etag("do_ph")
 
  def do_pp(self):
    self.btag("do_pp") 
    self.chk(TT.IDN,"pp")
    self.m[self.mp]=0x04
    self.mp+=1
    self.nx()
    self.etag("do_pp")

  def do_ma(self):
    self.btag("do_ma") 
    self.chk(TT.IDN,"ma")
    self.m[self.mp]=0x05
    self.mp+=1
    self.nx()
    self.etag("do_ma")

  def do_am(self):
    self.btag("do_am") 
    self.chk(TT.IDN,"am")
    self.m[self.mp]=0x06
    self.mp+=1
    self.nx()
    self.etag("do_am")

  def do_ia(self):
    self.btag("do_ia") 
    self.chk(TT.IDN,"ia")
    self.m[self.mp]=0x07
    self.mp+=1
    self.nx()
    self.etag("do_ia")

  def do_in(self):
    self.btag("do_in") 
    self.chk(TT.IDN,"in")
    self.m[self.mp]=0x08
    self.mp+=1
    self.nx()
    self.etag("do_in")

  def do_de(self):
    self.btag("do_de") 
    self.chk(TT.IDN,"de")
    self.m[self.mp]=0x09
    self.mp+=1
    self.nx()
    self.etag("do_de")

  def do_jp(self):
    self.btag("do_jp") 
    self.chk(TT.IDN,"jp")
    self.m[self.mp]=0x0A
    self.mp+=1
    self.nx()
    self.etag("do_jp")

  def do_so(self):
    self.btag("do_so") 
    self.chk(TT.IDN,"so")
    self.m[self.mp]=0x0B
    self.mp+=1
    self.nx()
    self.etag("do_so")

  def do_cp(self):
    self.btag("do_cp") 
    self.chk(TT.IDN,"cp")
    self.m[self.mp]=0x0C
    self.mp+=1
    self.nx()
    self.etag("do_cp")

  def do_je(self):
    self.btag("do_je") 
    self.chk(TT.IDN,"je")
    self.m[self.mp]=0x0D
    self.mp+=1
    self.nx()
    self.etag("do_je")

  def do_jn(self):
    self.btag("do_jn") 
    self.chk(TT.IDN,"jn")
    self.m[self.mp]=0x0E
    self.mp+=1
    self.nx()
    self.etag("do_jn")

  def do_jg(self):
    self.btag("do_jg") 
    self.chk(TT.IDN,"jg")
    self.m[self.mp]=0x0F
    self.mp+=1
    self.nx()
    self.etag("do_jg")

  def do_jl(self):
    self.btag("do_jl") 
    self.chk(TT.IDN,"jl")
    self.m[self.mp]=0x10
    self.mp+=1
    self.nx()
    self.etag("do_jl")

  def do_br(self):
    self.btag("do_br") 
    self.chk(TT.IDN,"br")
    self.m[self.mp]=0x11
    self.mp+=1
    self.nx()
    self.etag("do_br")




  def eval(self):
    self.btag("eval") 
              
    if self.gtyp()==TT.IDN:
    
      if self.gv()=="no":
        self.do_no()
      if self.gv()=="ad":
        self.do_ad()
      elif self.gv()=="sb":
        self.do_sb()
      elif self.gv()=="ph":
        self.do_ph()
      elif self.gv()=="pp":
        self.do_pp()
      elif self.gv()=="ma":
        self.do_ma()
      elif self.gv()=="am":
        self.do_am()
      elif self.gv()=="ia":
        self.do_ia()
      elif self.gv()=="in":
        self.do_in()
      elif self.gv()=="de":
        self.do_de()
      elif self.gv()=="jp":
        self.do_jp()
      elif self.gv()=="so":
        self.do_so()
      elif self.gv()=="cp":
        self.do_cp()
      elif self.gv()=="je":
        self.do_je()
      elif self.gv()=="jn":
        self.do_jn()
      elif self.gv()=="jg":
        self.do_jg()
      elif self.gv()=="jl":
        self.do_jl()
      elif self.gv()=="br":
        self.do_br()
      else:
        self.error(f"invalid command {self.gv()}")

    self.end_tag("eval") 






  def parse(self):
    self.ldlab()
    while not self.q and not self.gtyp()==TT.EOF:
      while self.gtyp() in [TT.SC,TT.NL,TT.LAB,TY.CMT]:
        self.next()
      self.eval()




