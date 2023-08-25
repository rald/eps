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
    p=False
    d=0
    c=None



    while not q:



      if i<len(s): 
        c=s[i] 
      else: 
        st=LS.QUIT

        

      if st==LS.DEFAULT:



        if c=='\"':

          scl=cl
          st=LS.STR

        elif c=='@':

          t.append(Tok(Pos(ln,cl),TT.AT,c))
        elif c==';':

          t.append(Tok(Pos(ln,cl),TT.SEMICOLON,c))

        elif c==':':

          st=LS.LAB

        elif c=='\n':

          t.append(Tok(Pos(ln,cl),TT.NEWLINE,c))  
          ln+=1
          cl=0  

        elif c=='+' or c=='-' or c.isdigit() or c=='.':

          scl=cl
          v=c
          st=LS.NUM

        elif c.isalpha():

          scl=cl
          i-=1
          cl-=1
          st=LS.IDN

        elif c=='#':

          scl=cl
          i-=1
          cl-=1
          st=LS.COMMENT

        elif i<len(s)-1 and s[i]=="/" and s[i+1]=="/":
        
          scl=cl
          i-=1
          cl-=1
          st=LS.COMMENT

        elif i<len(s)-1 and s[i]=="/" and s[i+1]=="*":
        
          scl=cl
          i-=1
          cl-=1
          d=1
          st=LS.MULTILINE_COMMENT 

        elif c.isspace():

          pass

        else:

          Err.throw(ET.INVALID_CHARACTER)



      elif st==LS.STR:



        if i<len(s) and  c!='\"':
          v+=c
        else:
          t.append(Tok(ln,scl,TT.STR,v))
          v=""
          st=LS.DEFAULT



      elif st==LS.NUM:



        if i<len(s) and c.isdigit() or (not p and c=='.'):
          if c=='.': p=True
          v+=c
        else:
          if p:
            t.append(Tok(Pos(ln,scl),TT.FLT,float(v)))
          else:
            t.append(Tok(Pos(ln,scl),TT.INT,int(v)))          
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
            t.append(Tok(Pos(ln,scl),TT.NONE,None))
          elif v=='false':
            t.append(Tok(Pos(ln,scl),TT.F,False))
          elif v=='true':
            t.append(Tok(Pos(ln,scl),TT.T,True))
          else:
            t.append(Tok(Pos(ln,scl),TT.IDN,v))

          v=""
          i-=1
          cl-=1
          st=LS.DEFAULT       



      elif st==LS.LAB:



        if i<len(s) and c.isalnum() or c=='_':
          v+=c
        else:
          t.append(Tok(Pos(ln,scl),TT.LAB,v))
          v=""
          i-=1
          cl-=1
          st=LS.DEFAULT       



      elif st==LS.COMMENT:



        if i<len(s) and c!="\n":
          v+=c
        else:
          t.append(Tok(Pos(ln,scl),TT.COMMENT,v))
          v=""
          st=LS.DEFAULT       



      elif st==LS.MULTILINE_COMMENT:


        if d==0:
          t.append(Tok(Pos(ln,scl),TT.COMMENT,v))
          v=""
          st=LS.DEFAULT
        elif i<len(s)-1 and (s[i]!="/" or s[i+1]!="*"):
          d+=1
        elif i<len(s)-1 and (s[i]!="*" or s[i+1]!="/"):
          d-=1
        else:
          v+=c




      elif st==LS.QUIT:

        q=True



      if i<len(s): 
        i+=1 
        cl+=1
      else:
        q=True


    t.append(Tok(Pos(ln,cl),TT.EOF,None))

    return t


