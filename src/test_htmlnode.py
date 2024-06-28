import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        htmln1 = HTMLNode()
        htmln2 = HTMLNode()
        self.assertEqual(htmln1, htmln2)
        htmln3 = HTMLNode("p", "Hello ! I'm the new paragraph",
                          None, {"href": "https://www.google.com"})
        htmln4 = HTMLNode("p", "Hello ! I'm the new paragraph",
                          None, {"href": "https://www.google.com"})
        self.assertEqual(htmln3, htmln4)

    def test_props_to_html(self):
        result_string = "href=\"https://www.google.com\" target=\"_blank\""
        htmln1 = HTMLNode("a", None, None,
                          {"href": "https://www.google.com", "target": "_blank"})
        test_string = htmln1.props_to_html()
        self.assertEqual(result_string, test_string)

class TestLeafNode(unittest.TestCase):

    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html_string = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), html_string)

    def test_eq_target_isNone(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html_string = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(), html_string)

    def test_eq_target_notNone(self):
        node = LeafNode("a", "LinkText", {"href": "https://example.com", "target": "_blank"})
        html_string = "<a href=\"https://example.com\" target=\"_blank\">LinkText</a>"
        self.assertEqual(node.to_html(), html_string)

    def test_valueError(self):
        node = LeafNode("p")
        with self.assertRaises(ValueError):
            node.to_html()

class TestParentNode(unittest.TestCase):

    def test_eq1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        html = node.to_html()
        result = "<p>\n   <b>Bold text</b>\n   Normal text\n   <i>italic text</i>\n   Normal text\n</p>"
        self.assertEqual(html, result)

    def test_eq2(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("p",
                            [
                                LeafNode(None, "Nested normal text"),
                                LeafNode("i", "Nested italic text"),
                            ],
                        ),
                LeafNode(None, "Normal text"),
            ],
        )
        html = node.to_html()
        result = "<p>\n   <b>Bold text</b>\n   <p>\n      Nested normal text\n      <i>Nested italic text</i>\n   </p>\n   Normal text\n</p>"
        self.assertEqual(html, result)

    def test_valueError(self):
        node = ParentNode(
                 "p",
                 [
                     LeafNode("b", "Bold text"),
                     None,
                 ],
         )
        with self.assertRaises(ValueError):
            node.to_html()
        node2 = ParentNode(None,
                 [
                     LeafNode("b", "Bold text"),
                 ],
         )
        with self.assertRaises(ValueError):
            node2.to_html()

    def test_valueError_2(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
