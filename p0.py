class p0:

  def __init__(self,t):
    self.t=t
    self.tp=0




    return {"adr":a,"ins":s}      


  def lk(self):
    self.t[self.tp]

  def gt(self):
    self.lk().typ

  def gv(self):
    self.lk().val
    
  def gp(self):
    self.lk().pos
      
  def gl(self):
    self.lk().pos.ln
      
  def gc(self):
    self.lk().pos.cl

  def gb(self,a):
    return self.m[a]

  def gw(self,a):
    return self.m[a]+self.m[a+1]*256

  def nx(self):
    self.tp+=1



  def asm(self,a):
    q=False
    c=None
    while not q:
  
      h=PS.itoa(a,16,4)
      r=self.gins(a)

      c=input(f"{h} {r['ins']}: ")

      if c.strip()=="":
        q=True
      else:
        lexer=Lexer(c)
        t=lexer.lex()
        p1=P1(t)
        p1.eval()

  def dmp(self,sa,ea):
    for i in range(sa,ea+1):
      h0=PS.itoa(i,16,4)
      r.self.gins(i)
      print(f"{h0} {r['ins']}")



  def do_q(self):
    self.q=True



  def do_a(self):
    self.nx()
    adr=self.mp
    if self.gt()==TT.HEX:
      adr=PS.atoi(self.gv(),16)
      self.nx()
    self.asm(adr)



  def do_d():
    self.nx()
    if self.gt()!=TT.HEX:
      print("start address expected")
    sadr=PS.atoi(self.gv(),16)
    self.nx()
    if self.gt()!=TT.HEX:
      print("end address expected")
    eadr=PS.atoi(self.gv(),16)
    self.nx()
    self.dmp(sadr,eadr)



  def eval0(self):

    q=False

    while not q: 

      while self.gt() in [TT.SC,TT.NL]:
        self.nx()
      
      if self.gt()==TT.IDN:

        if self.gv()=="q":
          self.do_q()
        elif self.gv()=="a":
          self.do_a()
        elif self.gv()=="d":
          self.do_d()



