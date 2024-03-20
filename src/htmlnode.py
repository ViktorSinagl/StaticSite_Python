
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if (self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
                self.props == other.props):
            return True
        return False

    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if (self.props is None):
            return ""
        else:
            return f"href=\"{self.props['href']}\" target=\"{self.props['target']}\""


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self, indent=0):
        #ret_string = ""
        if self.value is None:
            raise ValueError("value = None error")
        if self.tag is None:
            ret_string = (indent * " ") + self.value
            return ret_string
        elif self.tag == "a":
            if self.props == {} or self.props is None:
                raise ValueError("link tag (a) with property emtpy or null!")
            elif 'target' in self.props and self.props['target'] is not None:
                ret_string = f"<{self.tag} href=\"{self.props['href']}\" target=\"{self.props['target']}\">{self.value}</{self.tag}>"
                ret_string = (indent * " ") + ret_string
                return ret_string
            else:
                ret_string =  f"<{self.tag} href=\"{self.props['href']}\">{self.value}</{self.tag}>"
                ret_string = (indent * " ") + ret_string
                return ret_string
        ret_string =  f"<{self.tag}>{self.value}</{self.tag}>"
        ret_string = (indent * " ") + ret_string
        return ret_string

#html.append("\t" + ("\n\t".join(html_inner)))

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self, indent=0):
        if self.tag is None:
            raise ValueError("error in to_html() -> tag not provided!")
        if self.children is None:
            raise ValueError("error ParrentNode class -> self.children is None")
        html = []
        ret_string = indent * " "
        html.append(f"{ret_string}<{self.tag}>")
        for child in self.children:
            if child is None:
                raise ValueError("None value of parrent node children!")
            html.append(child.to_html(indent + 3))
        html.append(f"{ret_string}</{self.tag}>")
        return "\n".join(html)
