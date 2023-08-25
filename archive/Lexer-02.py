from LS import LS
from Tok import Tok
from TT import TT
from Pos import Pos

class Lexer:

  @staticmethod
  def lex(s):

    q=False
    i=0
    st=LS.DEFAULT
    t=[]
    v=""
    ln=1
    cl=1
    scl=0
    sln=0
    p=False
    d=0
    c=None



    while not q:



      if i<len(s): 
        c=s[i] 
        

      if st==LS.DEFAULT:



        if c=='\"':

          sln=ln
          scl=cl

          st=LS.STR

        elif c=='+' or c=='-' or c=='.' or c.isdigit():
          if c=='.': p=True

          sln=ln
          scl=cl
          v=c
          st=LS.NUM

        elif c.isalpha():

          sln=ln
          scl=cl
          i-=1
          cl-=1
          st=LS.IDN

        elif c==':':

          sln=ln
          scl=cl
          st=LS.LAB

        elif c=='@':

          t.append(Tok(Pos(ln,cl),TT.AT,c))

        elif c=='#':

          sln=cl
          scl=cl
          i-=1
          cl-=1
          st=LS.COMMENT

        elif c==';':

          t.append(Tok(Pos(ln,cl),TT.SEMICOLON,c))

        elif c=='\n':

          t.append(Tok(Pos(ln,cl),TT.NEWLINE,c))  
          ln+=1
          cl=0  

        elif c.isspace():

          pass

        else:

          Err.throw(ET.INVALID_CHARACTER)



      elif st==LS.STR:



        if i<len(s) and  c!='\"':
          v+=c
        else:
          t.append(Tok(sln,scl,TT.STR,v))
          v=""
          st=LS.DEFAULT



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
            Err.throw(ET.INVALID_NUMBER,{msg:"invalid number","pos":Pos(sln,scl))      
          p=False
          v=""
          i-=1
          cl-=1
          st=LS.DEFAULT
          


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
          cl-=1
          st=LS.DEFAULT       



      elif st==LS.LAB:



        if i<len(s) and c.isalnum() or c=='_':
          v+=c
          
        else:
          t.append(Tok(Pos(sln,scl),TT.LAB,v))
          v=""
          i-=1
          cl-=1
          st=LS.DEFAULT       



      elif st==LS.COMMENT:



        if i<len(s) and c!="\n":
          v+=c
        else:
          t.append(Tok(Pos(sln,scl),TT.COMMENT,v))
          v=""
          st=LS.DEFAULT       



      elif st==LS.QUIT:

        q=True



      if i<len(s): 
        i+=1 
        cl+=1
      else:
        q=True

         

    t.append(Tok(Pos(ln,cl),TT.EOF,None))

    return t


