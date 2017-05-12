from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class BookHandler(ContentHandler):
    inAuthor = False
    inTitle = False

    def startElement(self, name, attrs):
        if name == "book":
            print("*****Book*****")
        if name == "title":
            self.inTitle = True
            print("Title : ", )
        if name == "author":
            self.inAuthor = True
            print("Author : ", )

    def endElement(self, name):
        if name == "title":
            self.inTitle = False
        if name == "author":
            self.inAuthor = False

    def characters(self, content):
        if self.inTitle or self.inAuthor:
            print(content)


parser = make_parser()
parser.setContentHandler(BookHandler())
parser.parse("library.xml")
