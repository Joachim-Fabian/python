
print("                   WELCOME TO GROUP E BOOK STORE PROGRAM         ")
print("                   By Joachim, Otafire, Nicole         ")
print("                   ======================================        ")
print("                   --------------------------------------         ")
name = input(f"Please Enter Your name: ") 
greeting = print(f"Hello {name.upper()}, Greetings from Group E.")



while True: 
  try: 
    age = int(input("How old are you?: ")) 
    break 
  except ValueError: 
    print("Value error: invalid entry, enter valid number")

from datetime import datetime 
current_year = datetime.now().year 
year_of_birth = current_year - age 

print(f"You were born in, {year_of_birth}\n") 



while True:
  try: 
    fav_number = int(input(f"What is your favorite number, {name.upper()}: "))
    print(f"{fav_number} is an amazing favorite number")
    if (fav_number % 2 == 0):
      print("and guess what, its an even number")
      if (fav_number > 10):
        print("its also greater than 10\n")
      elif (fav_number == 10):
        print("Did you know the number 10, is the base of the decimal system")
      elif (fav_number % 2 > 10):
        print("greater heights i see, result is greater than 10 when divided by 2 as well\n")
      else:
        print("but quite a low number\n")
    else:
      print("and guess what, its an odd number\n")
      break
    break
  except:
    print("Value error: invalid entry, enter valid number")


"""1. syntax error: used wrong syntax of using multiple else statements instead of using 
elif. 
Applied elif and defined parameters because using else multiple times displayed outputs of other else statements.
2. used a wrong variable name for fav_number which gave a TypeError: not all arguments converted during string formatting.
had to change the variable name used to fav_number to erase error"""

import time 
while True: 
  question1 = input("Do you like reading?(yes/no): ") 

  if question1.lower() == "yes": 
    print("\nThere are some books available, hope you like them\n")
    time.sleep(2) 
    
    class Book: 
      def __init__(self, title, author, year_published): 
        self.title = title
        self.author = author
        self.year_published = year_published
      def description(self): 
            return f"{self.title} by {self.author}, published in {self.year_published}"

    """book1 = Book(input("enter title: "),input("enter author: "),input("enter year: "))
    book2 = Book(input("enter title: "),input("enter author: "),input("enter year: "))
    book3 = Book(input("enter title: "),input("enter author: "),input("enter year: "))"""

    book1 = Book("Introduction to IT", "Goefrey", 1982)
    book2 = Book("Programing Techniques","Otafire",1995)
    book3 = Book("Oliva Twist","Charles Dickens",1997)
    book4 = Book("Chemical science", "Abort", 1960)
    book5 = Book("Multimedia systems", "JaneRose", 1913)
    book6 = Book("Art and Design", "Darlington", 1949)
    book7 = Book("The Great Wall of China", "WakaScott", 1925)
    book8 = Book("China Town", "Savage", 1851)
    book9 = Book("The Hyna", "Jkimz", 1951)
    book10 = Book("KingKong", "1111", 1937)

    """print(f"{book1.title} by {book1.author}, published in {book1.year_published}")
    print(f"{book2.title} by {book2.author}, published in {book2.year_published}")
    print(f"{book3.title} by {book3.author}, published in {book3.year_published}")"""
    for i, book in enumerate([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10], start=1):
      
      print(f"{i}. {book.description()}")

    print("\nPlease wait")
    print("Generating a list of available books sorted by year...")
    time.sleep(3) 

    def sort_books_by_year(books): 
        if not books: 
          print("the list is empty.")
        return sorted(books, key=lambda book:book.year_published) 

    books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10] 

    sorted_books = sort_books_by_year(books)




    while True:
        if books != []: 
            print("\nlist of sorted books".upper())
            for book in sorted_books:
              print(book.title, "by", book.author, "in", book.year_published)
        break
        
    


    def search_book_by_title(books, title):  
      for book in books:
        if book.title.lower() == title.lower(): 


          print("\nBook found:")
          print(book.description()) 
          return
      print("\nBook not found.")

    while True:
      title_to_search = input("\nSearch book by title to check library or exit to end search: ") 


      if title_to_search.lower()== "exit": 
        print("Exiting the search.")
        time.sleep(2)
        print("Exiting the program")
        break
      search_book_by_title(books, title_to_search) 

    break    
  elif question1 == "no": 
   print("Exiting the program")
   
   break
   
 
