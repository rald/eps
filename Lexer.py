from LS import LS
from TK import TK
from TT import TT
from P import P
from ER import ER
from ET import ET

class Lexer:

  def __init__(self,s):
    self.s=s
    self.ind=0
    self.dbg=1
    self.ln=0
    self.cl=0
    
  def btag(self,tag):
    if self.dbg==1:
      print("  "*self.ind,end="")   
      print(f"<{tag}>")
    self.ind+=1

  def etag(self,tag):
    self.ind-=1
    if self.dbg==1:
      print("  "*self.ind,end="")   
      print(f"</{tag}>")



  def lex(self):

    q=False
    i=0
    st=LS.DEF
    t=[]
    v=""
    scl=0
    sln=0
    p=False
    d=0
    c=None



    while not q:



      if i<len(self.s): 
        c=self.s[i]
      else:
        st=LS.EXT



      if st==LS.DEF:
   


        if c.isalpha():
          self.btag("IDN")

          sln=self.ln
          scl=self.cl
          i-=1
          self.cl-=1
          st=LS.IDN

        elif c=='$':
          self.btag("HEX")
  
          sln=self.ln
          scl=self.cl
          st=LS.HEX
          
        elif c==';':

          t.append(TK(P(self.ln,self.cl),TT.SC,c))

        elif c=='\n':

          t.append(TK(P(self.ln,self.cl),TT.NL,c))  
          self.ln+=1
          self.cl=0  

        elif c.isspace():

          pass

        else:

          ER.throw(ET.INVALID_CHARACTER)



      elif st==LS.IDN:



        if i<len(self.s) and c.isalpha():
          v+=c
          
        else:

          t.append(TK(P(sln,scl),TT.IDN,v))

          v=""
          i-=1
          self.cl-=1
          st=LS.DEF       

          self.etag("IDN")



      elif st==LS.HEX:

        if i<len(self.s) and ((c>='0' and c<='9') or (c.upper()>='A' and c.upper()<='F')):
        
          v+=c.upper()
          
        else:

          t.append(TK(P(sln,scl),TT.HEX,v.upper() if len(v)%2==0 else '0'+v.upper()))

          v=""
          i-=1
          self.cl-=1
          st=LS.DEF       

          self.etag("HEX")



      elif st==LS.EXT:

        q=True



      if i<len(self.s): 
        i+=1 
        self.cl+=1



    t.append(TK(P(self.ln,self.cl),TT.EOF,None))

    return t


