import os
import random 
import PIL
import math
from PIL import Image, ImageDraw
from datetime import datetime

from palette import pal
from Token import Token
from TokenType import TokenType
from my_lib import resize_canvas



class Parser:



  def __init__(self,toks,image_path):
  
    self.id=id

    self.t=toks
    self.v={}
    self.q=False

    self.sv("sys","pc",Token.int(0))
    self.sv("sys","dbg",Token.int(0))
    self.sv("sys","ind",Token.int(0))
    self.sv("sys","rst",Token.list([]))
    self.sv("sys","stk",Token.list([]))

    self.image_path=image_path
    if os.path.isfile(self.image_path):
      self.img=Image.open(self.image_path).convert('RGB')
    else:
      self.img=PIL.Image.new(mode="RGB", size=(640,480), color=pal[12])
    self.draw=ImageDraw.Draw(self.img)



  def er(self,msg):
    print(f"\n{self.get_line()}:{self.get_column()}: {msg}")
    quit()




  def sv(self,t,n,v):
    self.var[t+'_'+n]=v

  def gv(self,t,n):
    return self.var[t+'_'+n]






  def next(self):
    if self.get_type()==TokenType.EOF:
      self.error("end of file")
    else:
      self.gv("sys","pc").val+=1
      if self.gv("sys","dbg").val==1: print("pc",self.pc)



  def begin_tag(self,tag):
    if self.gv("sys","dbg").val==1:
      print("  "*self.indent,end="")   
      print(f"<{tag}>")
    self.indent+=1

  def end_tag(self,tag):
    self.indent-=1
    if self.gv("sys","dbg").val==1:
      print("  "*self.indent,end="")   
      print(f"</{tag}>")


  
  def load_labels(self):
    for i in range(len(self.toks)):
      if self.toks[i].type==TokenType.LABEL:
        label=self.toks[i]
        if "LAB_"+label.value in self.glo:
          print(f"{self.toks[i].line}:{self.toks[i].column}:label redefined: {label.value}")
          quit()
        self.glo["LAB_"+label.value]=Token(0,0,TokenType.INTEGER,i);



  def get_line(self):
    return self.look().line



  def get_column(self):
    return self.look().column
    


  def look(self):
    return self.toks[self.pc]



  def peek(self,offset):
    pos=self.pc+offset
    if pos<0 or pos>=len(self.toks):
      self.print(f"offset out of bounds {pos}")
      quit()
    return self.toks[self.pc+offset]



  def match(self,type):
    if self.look().type!=type:
      self.error(f"found {self.look().type} expected {type}")      


 
  def check(self,type,value):
    self.begin_tag("check") 
    self.match(TokenType.IDENT)
    if self.get_value()!=value:
      self.error(f"found '{self.get_value()}' expected {value}")  
    self.next()
    self.end_tag("check") 



  def get_token(self):
    return self.look()



  def get_type(self):
    return self.look().type



  def get_value(self):
    return self.look().value



  def eat(self,type,count=1):
    for _ in range(count):
      self.match(type)
      self.next()


      
 

 

  def do_set(self):
    self.begin_tag("do_set") 
    self.check(TokenType.IDENT,"set")
    self.end_tag("do_set") 



  def do_say(self):
    self.begin_tag("do_say") 
    self.check(TokenType.IDENT,"say")
    self.end_tag("do_say") 



  def do_add(self):
    self.begin_tag("do_add")
    self.check(TokenType.IDENT,"add")   
    self.end_tag("do_add") 



  def do_sub(self):
    self.begin_tag("do_sub")
    self.check(TokenType.IDENT,"sub")
    self.end_tag("do_sub") 



  def do_call(self):
    self.begin_tag("do_call")
    self.check(TokenType.IDENT,"call")
    self.end_tag("do_call") 



  def do_ret(self):
    self.begin_tag("do_ret")
    self.check(TokenType.IDENT,"ret")
    self.end_tag("do_ret") 



  def do_jmp(self):
    self.begin_tag("do_jmp")
    self.check(TokenType.IDENT,"jmp")
    self.end_tag("do_jmp") 



  def do_je(self):
    self.begin_tag("do_je")
    self.check(TokenType.IDENT,"je")
    self.end_tag("do_je") 



  def do_jne(self):
    self.begin_tag("do_jne")
    self.check(TokenType.IDENT,"jne")
    self.end_tag("do_je") 



  def do_jl(self):
    self.begin_tag("do_jl")
    self.check(TokenType.IDENT,"jl")
    self.end_tag("do_je") 



  def do_jle(self):
    self.begin_tag("do_jle")
    self.check(TokenType.IDENT,"jle")
    self.end_tag("do_jle") 



  def do_jg(self):
    self.begin_tag("do_jg")
    self.check(TokenType.IDENT,"jg")
    self.end_tag("do_jg") 



  def do_jge(self):
    self.begin_tag("do_jge")
    self.check(TokenType.IDENT,"jge")
    self.end_tag("do_jge") 



  def do_push(self):
    self.begin_tag("do_push")
    self.check(TokenType.IDENT,"push")
    self.end_tag("do_push") 



  def do_pop(self):
    self.begin_tag("do_pop")
    self.check(TokenType.IDENT,"pop") 
    self.end_tag("do_pop") 



  def do_int(self):
    self.begin_tag("do_int")
    self.check(TokenType.IDENT,"int")
    self.end_tag("do_int") 



  def do_flt(self):
    self.begin_tag("do_flt")
    self.check(TokenType.IDENT,"flt")
    self.end_tag("do_flt") 



  def do_str(self):
    self.begin_tag("do_str")
    self.check(TokenType.IDENT,"str")
    self.end_tag("do_str") 



  def do_rnd(self):
    self.begin_tag("do_rnd")
    self.check(TokenType.IDENT,"rnd")
    self.end_tag("do_rnd") 



  def do_sin(self):
    self.begin_tag("do_sin")
    self.check(TokenType.IDENT,"sin")
    self.end_tag("do_sin") 



  def do_cos(self):
    self.begin_tag("do_cos")
    self.check(TokenType.IDENT,"cos")
    self.end_tag("do_cos") 



  def do_tan(self):
    self.begin_tag("do_tan")
    self.check(TokenType.IDENT,"tan")
    self.end_tag("do_tan") 



  def do_pset(self):
    self.begin_tag("do_pset")
    self.check(TokenType.IDENT,"pset")
    self.end_tag("do_pset") 



  def do_debug(self):
    self.check(TokenType.IDENT,"debug")
    self.glo["DBG"]=self.get_any()



  def do_globals(self):
    self.begin_tag("do_globals") 
    self.check(TokenType.IDENT,"globals")
    for key in self.glo:
      print(key,"=",self.glo[key])
    self.end_tag("do_globals") 



  def do_toks(self):
    self.begin_tag("do_toks") 
    self.check(TokenType.IDENT,"toks")
    for i in range(len(self.toks)):
      print(i,self.toks[i])
    self.end_tag("do_toks") 



  def do_tmyr(self):
    self.begin_tag("do_tmyr")
    self.check(TokenType.IDENT,"tmyr")
    self.glo["VAR_"+self.get_ident().value



    datetime.now().year
    self.end_tag("do_tmyr") 

  def do_tmyr(self):
    self.begin_tag("do_tmmh")
    self.check(TokenType.IDENT,"tmmh")
    self.end_tag("do_tmmh") 

  def do_tmyr(self):
    self.begin_tag("do_tmdy")
    self.check(TokenType.IDENT,"tmdy")
    self.end_tag("do_tmdy") 

  def do_tmyr(self):
    self.begin_tag("do_tmhr")
    self.check(TokenType.IDENT,"tmhr")
    self.end_tag("do_tmhr") 

  def do_tmyr(self):
    self.begin_tag("do_tmmn")
    self.check(TokenType.IDENT,"tmmn")
    self.end_tag("do_tmmn") 

  def do_tmyr(self):
    self.begin_tag("do_tmsc")
    self.check(TokenType.IDENT,"tmsc")
    self.end_tag("do_tmsc") 

  def do_tmyr(self):
    self.begin_tag("do_tmms")
    self.check(TokenType.IDENT,"tmms")
    self.end_tag("do_tmms") 




  def do_end(self):
    self.begin_tag("do_end") 
    self.check(TokenType.IDENT,"end")
    self.quit=True
    self.end_tag("do_end") 






  def eval(self):
    self.begin_tag("eval") 
              
    if self.get_type()==TokenType.IDENT:
    
      if self.get_value()=="say":
        self.do_say()
      elif self.get_value()=="set":
        self.do_set()
       elif self.get_value()=="add":
        self.do_add()
      elif self.get_value()=="sub":
        self.do_sub()
      elif self.get_value()=="push":
        self.do_push()
      elif self.get_value()=="pop":
        self.do_pop()
      elif self.get_value()=="call":
        self.do_call()
      elif self.get_value()=="ret":
        self.do_ret()
      elif self.get_value()=="jmp":
        self.do_jmp()
      elif self.get_value()=="je":
        self.do_je()
      elif self.get_value()=="jne":
        self.do_jne()
      elif self.get_value()=="jl":
        self.do_jl()
      elif self.get_value()=="jle":
        self.do_jle()
      elif self.get_value()=="jg":
        self.do_jg()
      elif self.get_value()=="jge":
        self.do_jge()
      elif self.get_value()=="rnd":
        self.do_rnd()
      elif self.get_value()=="sin":
        self.do_sin()
      elif self.get_value()=="cos":
        self.do_cos()
      elif self.get_value()=="tan":
        self.do_tan()
      elif self.get_value()=="pset":
        self.do_pset()
      elif self.get_value()=="tmyr":
        self.do_tmyr()
      elif self.get_value()=="tmmn":
        self.do_tmmn()
      elif self.get_value()=="tmdy":
        self.do_tmdy()
      elif self.get_value()=="tmhr":
        self.do_tmhr()
      elif self.get_value()=="tmmn":
        self.do_tmmn()
      elif self.get_value()=="tmsc":
        self.do_tmsc()
      elif self.get_value()=="tmms":
        self.do_tmms()
      elif self.get_value()=="end":
        self.do_end()
      else:
        self.error(f"invalid command {self.get_value()}")

    self.end_tag("eval") 






  def parse(self):

    self.load_labels()

    while not self.quit and not self.get_type()==TokenType.EOF:

      while self.get_type() in [TokenType.SEMI_COLON,TokenType.NEW_LINE,TokenType.LABEL,TokenType.COMMENT]:
        self.next()

      self.eval()

    self.img.save(self.image_path)






