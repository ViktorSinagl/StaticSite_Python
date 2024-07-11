import sys
import re
from htmlnode import LeafNode, ParentNode


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


SEPARATORS = {
    r'\*\*(?=\w)': "bold",
    r'__(?=\w)(?!_)': "bold",
    r'\*(?=\w)': "italic",
    r'_(?=\w)(?!_)': "italic",
    r"`(?=\w)": "code",
    r"``(?=\w)": "code",
    #r"```(?!\s)": "code_block",
    r'\[(.*?)\]\((.*?)\)': "link",
    r'\!\[(.*?)\]\((.*?)\)': "img",
}


#shoud be private function
def check_separator(text):
    min = sys.maxsize
    separator_find = None
    for separator in SEPARATORS:
        match = re.search(separator, text)
        if match:
            if match.start() < min:
                min = match.start()
                separator_find = separator
    return separator_find


#rewrite this accordting to extract mardowns and rewrite the separators, neni nutne hledat match pro obraceny string ale napsat regex tak je je psany pro link
def split_nodes_delimiter(text, separator_find, code_block):
    match1 = re.search(separator_find, text)
    match2 = re.search(separator_find, text[::-1])
    split_list = []
    if match2 is None:
        if len(text[0:match1.start()]) > 0:
            split_list += (from_text_to_texnode(text[0:match1.start()], code_block))
        split_list.append(from_text_to_texnode(
            text[(match1.start() + len(match1.group()))::],
            SEPARATORS[separator_find]))
    else:
        if len(text[0:match1.start()]) > 0:
            split_list += (from_text_to_texnode(text[0:match1.start()], code_block))
        split_list.append(from_text_to_texnode(
            text[
            (match1.start() + len(match1.group())):
            -(match2.start() + len(match2.group()))
            ],
            SEPARATORS[separator_find]))
        if match2.start() > 0:
            split_list += (from_text_to_texnode(text[-match2.start():], code_block))
    return split_list


#text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
# [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
def extract_markdown_links(text, separator_find, code_block):
    node_list = []
    match = re.search(separator_find, text)
    group = re.findall(separator_find, text)
    if len(text[0:match.start()]) > 0:
        node_list.append(TextNode(text[0:match.start()], "text", None))
    node_list.append(TextNode(group[0][0], code_block, group[0][1]))
    if len(text[match.end():]) > 0:
        node_list += (from_text_to_texnode(text[match.end():]))
    return (node_list)


def from_text_to_texnode(text, code_block="text"):
    separator_find = None
    textnodes = []
    if type(text) is not str:
        raise ValueError(f"__split name__ input parameter error,expected text type of object, given {type(text)}")
    if len(text) == 0:
        return None
    separator_find = check_separator(text)
    if separator_find is None:
        return [TextNode(text, code_block)]
    if SEPARATORS[separator_find] in ["bold", "italic", "code"]:
        textnodes += (split_nodes_delimiter(text, separator_find, code_block))
    elif SEPARATORS[separator_find] in ["link", "img"]:
        textnodes += (extract_markdown_links(text, separator_find, SEPARATORS[separator_find]))
    else:
        raise NotImplementedError(f"for type: {SEPARATORS[separator_find]}")
    return textnodes


#need a better function, this work with list, i want to work with tree like structure
def textnodelist_to_htmlnodelist(text_node: list):
    html_nodes = []
    for node in text_node:
        if isinstance(node, list):
            textnodelist_to_htmlnodelist(node)
        else:
            html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def peacock(text_node: list):
    html_nodes = []
    for node in text_node:
        if isinstance(node, list):
            html_nodes.append(ParentNode(None, peacock(node), None))
        else:
            html_nodes.append(text_node_to_html_node(node))
    return html_nodes



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
