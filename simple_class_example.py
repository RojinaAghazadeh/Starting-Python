class Book():
	book_type = 'classic'
	def __init__(self, page):
		self.pages = page
		
	def open(self):
		print(f'opened the book.({self.pages})')

b1 = Book(304)
print(b1.book_type)
b2 = Book(505)
b2.book_type = 'fun'
print(b2.book_type)
