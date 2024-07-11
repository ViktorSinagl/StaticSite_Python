import markdown

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


def main():
    markdown_text = """
 # Est praecorrumpere mitia

## Est lenis Aeneae ut atria vero

Lorem markdownum Plura radice demptos, vultusque putatur, parvoque; diemque
vertice, nec. Promissi conversa vitta. Geminas honore animae **tenus
progenies**. Erit apium, aeternum cruore priore illis perterrita cursu, nam sed
hanc feror flecti: cuius his labaret. Pugnat alta unda patrem pelagi, a augusta
infelix vaga; herbas inmensum cultumque tollens eodem haec quod rosave o?

1. Incubat duxit protinus color iamiam
2. Verti est
3. Densi latronis candens terra
4. Et iungi tamen gurgite
5. Nox grates crescere
    """
    print("give Markdown file: ")
    print(markdown_text, "\n\n+++++++======++++++")
    node = markdown.markdown_to_html_node(markdown_text)
    print("\n====================\nNode:")
    print(type(node))
    print(node)
    print(node.to_html())
    #print_html_nodes(nodes)


main()
