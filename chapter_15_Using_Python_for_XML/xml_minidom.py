from xml.dom.minidom import parse
import xml.dom.minidom


def printLibrary(library):
    books = myLibrary.getElementsByTagName("book")
    for book in books:
        print("*****Book*****")
        print("Title : %s" % book.getElementsByTagName("title")[0].childNodes[0].data)
        for author in book.getElementsByTagName("author"):
            print("Author : %s" % author.childNodes[0].data)


myDoc = parse("library.xml")
myLibrary = myDoc.getElementsByTagName("library")[0]
books = myLibrary.getElementsByTagName("book")
printLibrary(myLibrary)

newBook = myDoc.createElement("book")
newBookTitle = myDoc.createElement("title")
titleText = myDoc.createTextNode("Python")
newBookTitle.appendChild(titleText)
newBook.appendChild(newBookTitle)
newBookAuthor = myDoc.createElement("author")
authorName = myDoc.createTextNode("mahedi")
newBookAuthor.appendChild(authorName)
newBook.appendChild(newBookAuthor)
myLibrary.appendChild(newBook)

print("Added a new book")
printLibrary(myLibrary)

for book in myLibrary.getElementsByTagName("book"):
    for author in book.getElementsByTagName("author"):
        if author.childNodes[0].data.find("mahedi") != -1:
            removedBook = myLibrary.removeChild(book)
            removedBook.unlink()
print("Removed a Book")
printLibrary(myLibrary)

lib = open("library.xml", "w")
lib.write(myDoc.toprettyxml(" "))
lib.close()
