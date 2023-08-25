from LS import LS
from Tok import Tok
from TT import TT
from Pos import Pos
from Err import Err
from ET import ET

class Lexer:

  def __init__(self,s):
    self.s=s
    self.ind=0
    self.dbg=1
    self.ln=1
    self.cl=1
    
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

    s=self.s
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



      if i<len(s): 
        c=s[i]
      else:
        q=True



      if st==LS.DEF:
   


        if c=='\"':
          self.btag("STR")

          sln=self.ln
          scl=self.cl

          st=LS.STR

        elif c=='+' or c=='-' or c=='.' or c.isdigit():
          self.btag("NUM")

          if c=='.': p=True

          sln=self.ln
          scl=self.cl
          v=c
          st=LS.NUM

        elif c.isalpha():
          self.btag("IDN")

          sln=self.ln
          scl=self.cl
          i-=1
          self.cl-=1
          st=LS.IDN

        elif c==':':
          self.btag("LAB")
  
          sln=self.ln
          scl=self.cl
          st=LS.LAB

        elif c=='@':

          t.append(Tok(Pos(self.ln,self.cl),TT.AT,c))

        elif c=='#':
          self.btag("SLC")

          sln=self.cl
          scl=self.cl
          i-=1
          self.cl-=1
          st=LS.SLC

        elif i<len(s)-1 and s[i]=='/' and s[i+1]=='/':
          self.btag("SLC")

          sln=self.cl
          scl=self.cl
          i-=1
          self.cl-=1
          st=LS.SLC

        elif i<len(s)-1 and s[i]=='/' and s[i+1]=='*':
          self.btag("MLC")

          sln=self.cl
          scl=self.cl
          i-=1
          self.cl-=1
          d=1
          st=LS.MLC

        elif c==';':

          t.append(Tok(Pos(self.ln,self.cl),TT.SC,c))

        elif c=='\n':

          t.append(Tok(Pos(self.ln,self.cl),TT.NL,c))  
          self.ln+=1
          self.cl=0  

        elif c.isspace():

          pass

        else:

          Err.throw(ET.INVALID_CHARACTER)



      elif st==LS.STR:



        if i<len(s) and  c!='\"':
          v+=c
        else:
          t.append(Tok(Pos(sln,scl),TT.STR,v))
          v=""
          st=LS.DEF

          self.etag("STR")



      elif st==LS.NUM:



        if i<len(s) and (c.isdigit() or (not p and c=='.')):
          if c=='.': p=True
          v+=c
        else:
          try:
            if p:
              t.append(Tok(Pos(sln,scl),TT.FLT,float(v)))
            else:
              t.append(Tok(Pos(sln,scl),TT.INT,int(v)))    
          except:
            Err.throw(ET.INVALID_NUMBER,{"msg":"invalid number","pos":Pos(sln,scl)})      

          p=False
          v=""
          i-=1
          self.cl-=1
          st=LS.DEF

          self.etag("NUM")
          


      elif st==LS.IDN:



        if i<len(s) and c.isalnum() or c=='_':
          v+=c
          
        else:
        
          if v=='none':
            t.append(Tok(Pos(sln,scl),TT.NONE,None))
          elif v=='false':
            t.append(Tok(Pos(sln,scl),TT.F,False))
          elif v=='true':
            t.append(Tok(Pos(sln,scl),TT.T,True))
          else:
            t.append(Tok(Pos(sln,scl),TT.IDN,v))

          v=""
          i-=1
          self.cl-=1
          st=LS.DEF       

          self.etag("IDN")



      elif st==LS.LAB:



        if i<len(s) and c.isalnum() or c=='_':
          v+=c
          
        else:
          t.append(Tok(Pos(sln,scl),TT.LAB,v))
          v=""
          i-=1
          self.cl-=1
          st=LS.DEF       

          self.etag("LAB")


        
      elif st==LS.SLC:



        if i<len(s) and c!="\n":
          v+=c
        else:
          t.append(Tok(Pos(sln,scl),TT.CMT,v))
          v=""
          st=LS.DEF       

          self.etag("SLC")



      elif st==LS.MLC:



        if i<len(s)-1 and s[i]=='*' and s[i+1]=='/':
          d-=1

        elif i<len(s)-1 and s[i]=='*' and s[i+1]=='/':
          d+=1

        elif d==0:
        
          v+="*/"
        
          t.append(Tok(Pos(sln,scl),TT.CMT,v))
          v=""
          
          i+=1
          self.cl+=1

          st=LS.DEF       

          self.etag("MLC")

        else:

          v+=c



      elif st==LS.QUIT:

        q=True



      if i<len(s): 
        i+=1 
        self.cl+=1



    t.append(Tok(Pos(self.ln,self.cl),TT.EOF,None))

    return t


