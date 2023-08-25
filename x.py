class Product:
  def __init__(self,id,name,price,quantity):
    self.id = id
    self.name = name
    self.price = price
    self.quantity = quantity

  def info(self):
    print("id: ",self.id," name: ",self.name," price: ",self.price," quantity: ",self.quantity)


class Products:
  def __init__(self):
    self.products = []

  def info(self):
    for product in self.products:
      product.info()

  def add(self,product):
    self.products.append(product)

  def remove(self,id):
    found = False

    for i in range(len(self.products)):
      if self.products[i].id == id:
        del self.products[i]
        found = True
        break
    if found:
      print("product ",id," has been removed")
    else :
      print("product ",id,"not found")


  def clear(self):
    print("product clear")
    self.products.clear()

  def search(self,id):
    x=-1
    for i in range(len(self.products)):
      if self.products[i].id == id:
        x = i
        break

    if x!=-1:
      print("product: ")
      print("id: ",self.products[x].id,", name: ",self.products[x].name,", price: ",self.products[x].price,", quantity: ",self.products[x].quantity)
    else:
      print("product not exist")

    return x

  def update(self,idx,id,name,price,quantity):
    self.products[idx].id = id
    self.products[idx].name = name
    self.products[idx].price = price
    self.products[idx].quantity = quantity




class Menu:
#       products=Products();
  def __init__(self):
    self.products = Products()

  def menu(self):

    exit = False

    while not exit:

      print(
        "\tMenu\n"
        "0: Exit\n"
        "1: Add\n"
        "2: Remove\n"
        "3: Update\n"
        "4: List\n"
        "5: Search\n\n"
      )

      choice = int(input("Enter choice: "))

      if choice == 0:
        exit = True
      elif choice == 1:
        self.add()
      elif choice == 2:
        self.remove(id)
      elif choice == 3:
        self.update(id)
      elif choice == 4:
        self.list()
      elif choice == 5:
        self.search(id)

  def add(self):
    print("add\n\n")

    id = int(input("Enter id: "))
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    self.products.add(Product(id,name,price,quantity))

    print("product successfully added\n")

  
  def remove(self,id):
    print("remove\n")
    id = int(input("Enter id: "))
    self.products.remove(id)
  

  def update(self,id):
    print("update\n")
    id = int(input("Enter id: "))
    idx = self.products.search(id)

    id = int(input("new id: "))
    name = input("new name: ")
    price = float(input("new price: "))
    quantity = int(input("new quantity: "))

    self.products.update(idx,id,name,price,quantity)


 
  """
          def update(self,id):
                  print("update")
                  id = int(input("Enter id: "))
                  idx = self.products.search(id)

                  id = int(input("new id: "))
                  name = input("new name: ")
                  price = float(input("new price: "))
                  quantity = int(input("new quantity: "))

                  self.products[idx].id = id
                  self.products[idx].name = name
                  self.products[idx].price = price
                  self.products[idx].quantity = quantity
          """

  def list(self):
    print("list\n");
    self.products.info()
  
  def search(self,id):
    print("search\n")
    id = int(input("Enter id: "))
    self.products.search(id)
  


menu = Menu()
menu.menu()


