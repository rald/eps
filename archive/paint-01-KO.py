class paint:

  def __init__(self,m):

    self.q=False

    self.m=m

    self.org=0x0000

    self.mh=0xFFFF
    self.ml=0x0000

    self.ph=self.mh
    self.pl=self.ph-1

    self.ah=self.pl-1
    self.al=self.ah-1

    self.sh=self.al-1
    self.sl=self.sh-1

    self.sth=self.sl-1
    self.stl=self.sth-1024

    self.fbh=self.stl-1
    self.fbl=self.fbh-4095

    self.srsp(self.sth)
    self.srpc(self.org)



  def pinfo(self):
    print("mh =",self.itoa(self.mh,16,4))
    print("ml =",self.itoa(self.ml,16,4))

    print("ph =",self.itoa(self.ph,16,4))
    print("pl =",self.itoa(self.pl,16,4))

    print("ah =",self.itoa(self.ah,16,4))
    print("al =",self.itoa(self.al,16,4))
 
    print("sh =",self.itoa(self.sh,16,4))
    print("sl =",self.itoa(self.sl,16,4))

    print("sth =",self.itoa(self.sth,16,4))
    print("stl =",self.itoa(self.stl,16,4))

    print("fbh =",self.itoa(self.fbh,16,4))
    print("fbl =",self.itoa(self.fbl,16,4))


  def save(self,n):
    f=open(n,"wb")
    f.write(self.m)
    f.close()

  def load(self,n):
    f=open(n,"rb")
    self,m=f.read(65536)
    f.close()

  def gb(self):
    return self.m[self.grpc()]%256
    
  def gw(self):
    return (self.m[self.grpc()]+self.m[self.grpc()+1]*256)%65536

  def grpc(self):
    return (self.m[self.pl]+self.m[self.ph]*256)%65536

  def srpc(self,v):
    self.m[self.grpc()]=v%256
    self.m[self.grpc()+1]=int(v/256)%256

  def grsp(self):
    return (self.m[self.sl]+self.m[self.sh]*256)%65536

  def srsp(self,v):
    self.m[self.grsp()]=v%256
    self.m[self.grsp()+1]=int(v/256)%256

  def grax(self):
    return (self.m[self.al]+self.m[self.ah]*256)%65536

  def srax(self,v):
    self.m[self.grax()]=v%256
    self.m[self.grax()+1]=int(v/256)%256

  def nx(self):
    self.srpc(self.grpc()+1)
    
  def pv(self):
    self.srpc(self.grpc()-1)

  def pushb(self,v):
    self.srsp(self.grsp()-1)
    self.m[self.grsp()]=v%256
 
  def pushw(self,v):
    self.pub(v%256)
    self.pub(int(v/256)%256)
  
  def popb(self):
    r=self.m[self.grsp()]%256
    self.srsp(self.grsp()+1)
    return r 

  def popw(self):
    return (self.popb()*256+self.popb())%65536

  do_no(self):
    pass

  do_ad(self):
    self.srac(self.popb()+self.popb())  

  do_su(self):
    y=self.popb()
    x=self.popb()
    self.srac(x-y)  

  do_pu(self):
    self.pushb(self.grax()%256)  

  do_po(self):
    set.srax(self.popb()%256)  

  do_ma(self):
    set.srax(self.m[self.gw()])  

  do_am(self):
    self.m[self.gw()]=set.grax()  

  do_ia(self):
    self.srax(set.gb())  

  do_in(self):
    self.srax(self.grax()+1)  

  do_de(self):
    self.srax(self.grax()-1)  

  do_ju(self):
    self.srpc(set.gw())  

  do_so(self):
    self.srax(set.gw()+self.popb())  

  do_co(self):
    self.pushb(self.grax()-set.gb())  

  do_je(self):
    if self.popb()==0:
      self.srpc(byte(self.gb()-128)
 
  do_jn(self):
    if self.popb()!=0:
      self.srpc(self.gb()-128)
 
  do_jg(self):
    if self.popb()<0:
      self.srpc(self.gb()-128)
 
  do_jl(self):
    if self.popb()>0:
      self.srpc(self.gb()-128)

  do_br(self):
    self.q=True
 
  def eval(self,pc):
    while not self.q:
      b0=self.gb(pc)
      if b0==0x00:
        self.do_no()
      elif b0==0x01:
        self.do_ad()
      elif b0==0x02:
        self.do_su()
      elif b0==0x03:
        self.do_pu()
      elif b0==0x04:
        self.do_po()    
      elif b0==0x05:
        self.do_ma()
      elif b0==0x06:
        self.do_am()
      elif b0==0x07:
        self.do_ia()
      elif b0==0x08:
        self.do_in()
      elif b0==0x09:
        self.do_de()
      elif b0==0x0A:
        self.do_ju()
      elif b0==0x0B:
        self.do_so()
      elif b0==0x0C:
        self.do_co()
      elif b0==0x0D:
        self.do_je()
      elif b0==0x0E:
        self.do_jn()
      elif b0==0x0F:
        self.do_jg()
      elif b0==0x10:
        self.do_jl()
      elif b0==0x11:
        self.do_br()
      self.nx()
        
