from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text and
            self.text_type == other.text_type and
                self.url == other.url):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


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
        html_node = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        html_node = LeafNode("img", "", {"src": text_node.url,
                                         "alt": text_node.text})
    else:
        raise Exception("text node with unsupported text type")
    return html_node
