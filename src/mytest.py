from main import markdown_to_blocks
from textnode import TextNode, LeafNode, from_text_to_texnode
import re


def inline_to_textnode(split_list):
    textnode_list = []
    for textnode in split_list:
        if len(textnode.text) > 0:
            textnode_list.append(textnode)
    return textnode_list




def main():
    """
    old_nodes = [
                    TextNode("ahoj *jak* se mas", "text"),
                    TextNode("mam se *dobre*", "text")
                ]
    ne2w_nodes = split_nodes_delimiter(old_nodes, "*", "italic")
    """
    test_list = [
            "this is *italic __bold text__*",
            "this is __bold text__",
            "__bold text",
            "thisis__bold text__",
            "thisis**bold text**yup",
            "*italic text*",
            "this is *italic text*",
            "this is _italic text_",
            "this is not ** bold text ** ",
            "this is not __ bold text __ ",
            "this is not ___ bold text ___ ",
            "this is not * italic text * ",
            "this is not _ italic text _ ",
            "this is none",
            "this is  a code ``!!",
            "this is  a code ` neco `  ",
            "this is a code `print(abc)`",
            "``print(abc)``",
            "``(x^2_this is a code_)$&``",
            "``(x^2_this is a code_)$&``",
            " this is a __shit",
            "**italic with one *please",
        ]
    #result = "bold, bold, bold, bold, bold, italic, italic, italic, None, None, None, None, None, None, code, code, code, code, code, code_block, None"
    #print("test correct results:")
    #print(result)
    print("\n\nTEST OF THE STRING SPLIT")
    for test in test_list:
        result = from_text_to_texnode(test)
        print(result)
    print("\n\nTEST OF LINK SEPARATOR")
    testlink = [
            "clik here [link](www.google.com) and here [link](www.seznam.cz)",
            "here is picture of ![your mom](yourmomnaked.png)",
    ]
    for text in testlink:
        print(from_text_to_texnode(text))
    print("\n\nBOOTDEV")
    bootdev = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    listik = from_text_to_texnode(bootdev)
    for node in listik:
        print(node)

    print("=====MARKDOWN BLOCK SPLIT\n\n")
    markdown_text = """# This is a heading

  This is a paragraph of text. It has some **bold** and *italic* words inside of it.

  * This is a list item
  * This is another list item"""
    blocks = markdown_to_blocks(markdown_text)
    print(blocks)



#main function run
main()
