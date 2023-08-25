from LS import LS
from Tok import Tok
from TT import TT
from Pos import Pos

class Lexer:

  @staticmethod
  def lex(s):

    quit=False
    state=LS.DEFAULT
    toks=[]
    text=""
    i=0
    ln=1
    cl=1
    scl=0
    dot=False
    d=0



    while not quit:



      if i<len(s): 
        c=s[i] 
      else: 
        state=LS.QUIT

        

      if state==LS.DEFAULT:



        if c=='\"':

          scl=cl
          state=LS.STR

        elif c=='@':

          toks.append(Tok(Pos(ln,cl),TT.AT,c))
        elif c==';':

          toks.append(Tok(Pos(ln,cl),TT.SEMICOLON,c))

        elif c==':':

          state=LS.LAB

        elif c=='#':

          scl=cl
          i-=1
          cl-=1
          state=LS.COMMENT

        elif i<len(s)-1 and s[i]=="/" and s[i+1]=="/":
        
          scl=cl
          i-=1
          cl-=1
          state=LS.COMMENT

        elif i<len(s)-1 and s[i]=="/" and s[i+1]=="*":
        
          scl=cl
          i-=1
          cl-=1
          d=1
          state=LS.MULTILINE_COMMENT 

        elif c=='\n':

          toks.append(Tok(Pos(ln,cl),TT.NEWLINE,c))  
          ln+=1
          cl=0  

        elif c=='+' or c=='-' or c.isdigit() or c=='.':

          scl=cl
          text=c
          state=LS.NUM

        elif c.isalpha():

          scl=cl
          i-=1
          cl-=1
          state=LS.IDN

        elif c.isspace():

          pass

        else:

          Err.throw(ET.INVALID_CHARACTER)



      elif state==LS.STR:



        if c!='\"':
          text+=c
        else:
          toks.append(Tok(ln,scl,TT.STR,text))
          text=""
          state=LS.DEFAULT



      elif state==LS.NUM:



        if c.isdigit() or (not dot and c=='.'):
          if c=='.': dot=True
          text+=c
        else:
          if dot:
            toks.append(Tok(Pos(ln,scl),TT.FLT,float(text)))
          else:
            toks.append(Tok(Pos(ln,scl),TT.INT,int(text)))          
          dot=False
          text=""
          i-=1
          cl-=1
          state=LS.DEFAULT
          


      elif state==LS.IDN:



        if c.isalnum() or c=='_':
          text+=c
        else:
          if text=='none':
            toks.append(Tok(Pos(ln,scl),TT.NONE,None))
          elif text=='false':
            toks.append(Tok(Pos(ln,scl),TT.F,False))
          elif text=='true':
            toks.append(Tok(Pos(ln,scl),TT.T,True))
          else:
            toks.append(Tok(Pos(ln,scl),TT.IDN,text))

          text=""
          i-=1
          cl-=1
          state=LS.DEFAULT       



      elif state==LS.LAB:



        if c.isalnum() or c=='_':
          text+=c
        else:
          toks.append(Tok(Pos(ln,scl),TT.LAB,text))
          text=""
          i-=1
          cl-=1
          state=LS.DEFAULT       



      elif state==LS.COMMENT:



        if c!="\n":
          text+=c
        else:
          toks.append(Tok(Pos(ln,scl),TT.COMMENT,text))
          text=""
          state=LS.DEFAULT       



      elif state==LS.MULTILINE_COMMENT:


        if d==0:
          toks.append(Tok(Pos(ln,scl),TT.COMMENT,text))
          text=""
          state=LS.DEFAULT
        elif i<len(s)-1 and (s[i]!="/" or s[i+1]!="*"):
          d+=1
        elif i<len(s)-1 and (s[i]!="*" or s[i+1]!="/"):
          d-=1
        else:
          text+=c




      elif state==LS.QUIT:



        quit=True



      if i<len(s): 
        i+=1 
        cl+=1
      else: 
        state=LS.QUIT



    toks.append(Tok(Pos(ln,cl),TT.EOF,None))

    return toks


