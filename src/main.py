from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

def check_delimiter(delimiter, delimiters):
    pass
    

""" This is some old unused function probably
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    sub_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            return_nodes.append(node)
            continue
        elif delimiter not in node.text:
            raise Exception(f"Delimiter({delimiter}) was not found in node.text({node.text}) in split_nodes_delimiter function")
        else:
            pass
        sub_text = node.text.split(delimiter)
        print(sub_text)
        for i, text in enumerate(sub_text):
            if i == 0 or i == len(sub_text) :
                sub_node = TextNode(text, text_type)
            elif text == "":
                continue
            else:
                sub_node = TextNode(text, "text")
            sub_nodes.append(sub_node)
    return sub_nodes
    """


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def main():
    pass

