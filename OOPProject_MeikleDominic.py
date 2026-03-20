class Author:
    def __init__(self, name, dob, pob):
        self.name = name
        self.dob = dob
        self.pob = pob
    
    def __str__(self):
        return f"Author: {self.name}\nBorn: {self.dob} | Place of Birth: {self.pob}"

class Book:
    def __init__(self, title, author, published, genre):
        self.title = title
        self.author = author
        self.published = published
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author.name}\nPublished: {self.published} | Genre: {self.genre}\n"


authors = [
    Author("George Orwell", "June 25, 1903", "Motihari, India"),
    Author("Toni Morrison"," Febuary 18, 1931", "Lorain, Ohio, USA"),
    Author("Gabriel Garcia Marquez"," March 6, 1927", "Aracataca, Colombia"),
    Author("Jane Austen", "December 16, 1775", "Steventon, Hampshire, England"),
    Author("F. Scott Fitzgerald", "September 24, 1896", "St. Paul, Minnesota, USA"),
]

books = [
    Book("Nineteen Eighty-Four", authors[0], "1949", "Dystopian Fiction"),
    Book("Animal Farm", authors[0], "1945", "Political Satire"),
    Book("Beloved", authors[1], "1987", "Historical Fiction"),
    Book("The Bluest Eye", authors[1], "1970", "Literary Fiction"),
    Book("One Hundred Years of Solitude", authors[2], "1967", "Magical Realism"),
    Book("Love in the Time of Cholera", authors[2], "1985", "Romantic Fiction"),
    Book("Pride and Prejudice", authors[3], "1813", "Romantic Fiction"),
    Book("Sense and Sensibility", authors[3], "1811", "Romantic Fiction"),
    Book("The Great Gatsby", authors[4], "1925", "Modernist Fiction"),
    Book("Tender is the Night", authors[4], "1934", "Literary Fiction"),
]


def searchBook(title):
    i = 0
    for book in books:
        i += 1

        if book.title.lower() == title.lower():
            print("\n--- Book found ---")
            print(book)
            print("--- author details ---")
            print(book.author)

            break
        elif i == len(books):
            print("--- Book not found ---")
        else:
            continue

def searchAuthor(name):
    i = 0
    for author in authors:
        i += 1

        if author.name.lower() == name.lower():
            print("\n--- Author found ---")
            print(f"Books by {author.name}:\n")

            for book in books:
                if book.author.name == author.name:
                    print(book)



def main():
    for i in books:
        print(i)

    title = input("enter book name: ")
    searchBook(title)

    print("\n")

    for i in authors:
        print(i)
    
    author = input("Enter an author's name: ")
    searchAuthor(author)


if __name__ == "__main__":
    main()