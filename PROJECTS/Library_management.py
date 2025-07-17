class Library:
  def __init__(self):
    self.noBooks=0
    self.books=[]

  def addBook(self,book):
    self.books.append(book)
    self.noBooks=len(self.books)
  def showInfo(self):
    print(f"the library has {self.noBooks} books.the books are ")
    for book in self.books:
      print(book)
      
l1=Library()
l1.addBook("ashish ranjan1")
l1.addBook('ashish ranjan2')
l1.showInfo()