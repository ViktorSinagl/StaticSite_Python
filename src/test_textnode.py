import unittest

from textnode import TextNode, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text NODE\n", "italic", "www.seznam.cz")
        node2 = TextNode("This is a text NODE\n", "italic", "www.seznam.cz")
        self.assertEqual(node1, node2)
        node3 = TextNode(None, None, "www.seznam.cz")
        node4 = TextNode(None, None, "www.seznam.cz")
        self.assertEqual(node3, node4)
        node5 = TextNode(25, "smash!", None)
        node6 = TextNode(25, "smash!", None)
        self.assertEqual(node5, node6)
        node7 = TextNode("ahoj", "italic")
        node8 = TextNode("ahoj", "italic")
        self.assertEqual(node7, node8)
        node9 = TextNode("ahoj")
        node10 = TextNode("ahoj")
        self.assertEqual(node9, node10)

    def test_noteq(self):
        node1 = TextNode("This is not a text NODE\n",
                         "italic", "www.seznam.cz")
        node2 = TextNode("This is a text NODE\n", "italic", "www.seznam.cz")
        self.assertNotEqual(node1, node2)
        node3 = TextNode("This is not a text NODE\n",
                         "italic", "www.seznam.cz")
        node4 = TextNode("This is not a text NODE\n", "italic", "")
        self.assertNotEqual(node3, node4)
        node5 = TextNode("This is not a text NODE\n",
                         "italic", "www.seznam.cz")
        node6 = TextNode("This is not a text NODE\n", "italic", "")
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This is not a text NODE\n",
                         "italic", "www.seznam.cz")
        node8 = TextNode("This is not a text NODE\n",
                         "italic")
        self.assertNotEqual(node7, node8)


class Test_split_nodes_delimiter(unittest.TestCase):
    def test_eq(self):
        italic_nodes = [
                        TextNode("ahoj *jak* se mas.", "text"),
                        TextNode("mam se *dobre*", "text"),
                       ]
        code_node = [
                        TextNode("`e=mc^2` Einstein says!", "text")
                    ]
        result_italic = [
                        TextNode("ahoj ", "text"),
                        TextNode("jak", "italic"),
                        TextNode(" se mas.", "text"),
                        TextNode("mam se ", "text"),
                        TextNode("dobre", "italic")
                ]
        result_code = [
                        TextNode("e=mc^2", "code"),
                        TextNode(" Einstein says!", "text")
                    ]
        test_italic = split_nodes_delimiter(italic_nodes, "*", "italic")
        test_code = split_nodes_delimiter(code_node, "`", "code")
        self.assertEqual(result_italic, test_italic)
        self.assertEqual(result_code, test_code)


if __name__ == "__main()__":
    unittest.main()
