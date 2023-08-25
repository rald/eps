class paint:

  def __init__(self,m):

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
    return self.m[self.pc(]
    
  def gw(self):
    return self.m[self.pc()]+self.m[a+1]*256


  

  def eval(self,pc):
    b0=self.gb(pc)
    if  
      
