from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    print("main started")
    textnode = TextNode("This is the text node", "bold", "https.boot.dev.com")
    print(textnode)

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        html_node = LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        html_node = LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        html_node = LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        html_node = LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        raise NotImplementedError()
    elif text_node.text_type == "image":
        raise NotImplementedError()
    else:
        raise Exception("text node with unsupported text type")
    return html_node

# main program body:
main()
