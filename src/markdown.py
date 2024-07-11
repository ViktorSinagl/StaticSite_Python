import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, from_text_to_texnode, text_node_to_html_node, textnodelist_to_htmlnodelist, peacock
from enum import Enum


class Block(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


BTYPES = {
    r"#{1,6}\s+\w+": Block.HEADING,
    r"'{3} *.*\n(.*\n)*.*'{3}": Block.CODE,
    r">(.)+": Block.QUOTE,
    r"(\*|-)([^\S\r\n]+\w+)+": Block.UNORDERED_LIST,
    r"(\d.)([^\S\r\n]+\w+)+": Block.ORDERED_LIST,
}


def count_character_beg(string: str, character: str):
    count = 0
    if len(character) > 1:
        raise ValueError("Count_character_beg need as second parametr a character (string of size 1!)")
    i = 0
    while string[i] == string[0]:
        count += 1
        i += 1
    return count


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block: str):
    block_type = Block.PARAGRAPH
    for regex in BTYPES.keys():
        if re.match(regex, block):
            block_type = BTYPES[regex]
            return block_type
    return block_type


def get_tag(block_type: Block, block: str) -> str:
    if block_type == Block.HEADING:
        count = count_character_beg(block, '#')
        return f"h{count}"
    if block_type == Block.PARAGRAPH:
        return "p"
    if block_type == Block.QUOTE:
        return "blockquote"
    if block_type == Block.CODE:
        return "code"
    if block_type == Block.ORDERED_LIST:
        return "ol"
    if block_type == Block.UNORDERED_LIST:
        return "ul"


# Function that takes raw markdown string and return the list of html nodes (in tree-like structure)
#   - the root node is type of html. Under hmtl nodes, there are block type leaf nodes. Block type leaf nodes
# consists of standard text html nodes (text formating html nodes, as code, italic text etc.
"""
def markdown_to_html_node(markdown: str) -> list:
    html_child = []
    html_root = []
    root_node = HTMLNode('html', None, html_child)
    html_root.append(root_node)
    markdown_block = markdown_to_blocks(markdown)
    for block in markdown_block:
        block_type = block_to_block_type(block)
        tag = get_tag(block_type, block)
        block_node = HTMLNode(tag, None, [], None)
        textnodes = from_text_to_texnode(block)
        block_node.children.append(textnodelist_to_htmlnodelist(textnodes))
root_node.children.append(block_node)
return html_root

"""


def markdown_to_html_node(markdown: str) -> HTMLNode:
    root_node = ParentNode('html', [], None)
    markdown_block = markdown_to_blocks(markdown)
    for block in markdown_block:
        #i will allow only code blocks to have a parents
        block_type = block_to_block_type(block)
        tag = get_tag(block_type, block)
        block_node = ParentNode(tag, [], None)
        textnodes = from_text_to_texnode(block)
        block_node.children = peacock(textnodes)
        root_node.children.append(block_node)
    return root_node
