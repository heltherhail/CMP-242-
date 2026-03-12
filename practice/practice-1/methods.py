class Author:
    def __init__(self, name, book_name, page):
        self.name = name
        self.book_name = book_name
        self.page = page
        
    def Helther(self):
        return f"{self.book_name} by {self.name}"
        
    def __len__(self):
        return self.page
        
A2 = Author("Oguzan Deniz", "Boolean Algebra", 200)
    
print(A2)
print(len(A2))