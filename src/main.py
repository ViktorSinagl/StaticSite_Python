from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    print("main started")
    textnode = TextNode("This is the text node", "bold", "https.boot.dev.com")
    print(textnode)


# main program body:
main()
