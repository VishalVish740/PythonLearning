# Day66 -->Instance variable and class variable
class Employee:
    companyName = "Acer"   #Class Variable - use for all class who share all instances
    def __init__(self,name):
        self.name = name
        self.raise_amount = 200  #Instance variable - used for particular object
    def showData(self):
        print(f"The Name of employee is {self.name} and the raise amout in {self.companyName} is {self.raise_amount}")

emp = Employee("Vishal")
emp.showData()
Employee.showData(emp)

# Day67 --> Library management system solution
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Kitab")
l1.addBook("Notebook")
l1.showInfo()
Library.showInfo(l1)

# Day69 -->Class Method in python is type of method that is bound to class not to the instance
class Employee1:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls,newComp):
        cls.company = newComp

ep1 = Employee1()
ep1.name = "Vishal"
ep1.show()

ep1.changeCompany("Vivo")
ep1.show()
print(Employee1.company)

# Day70 -->Class method as alternative constructor
