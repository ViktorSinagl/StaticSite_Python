import unittest

from markdown import markdown_to_blocks, Block, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_string1(self):
        markdown_text = """# This is first heading
- with one list element

# There is another heading

here is list
- **bold** text
- *italic* text """
        test_result = ['# This is first heading\n- with one list element', '# There is another heading',
                       'here is list\n- **bold** text\n- *italic* text']
        result = markdown_to_blocks(markdown_text)
        self.assertEqual(test_result, result)


class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        block = "this should be.\nJust an simle paragraph"
        self.assertEqual(block_to_block_type(block), Block.PARAGRAPH)

    def test_code(self):
        block = """''' Python Code
def test_paragraph(self):
    block = "this should be.\nJust an simple paragraph"
    self.assertEqual(block_to_block_type(block), Block.PARAGRAPH)
    '''
"""
        self.assertEqual(block_to_block_type(block), Block.CODE)

    def test_heading(self):
        block = "### Heading 1\nThis should be an heading\n"
        self.assertEqual(block_to_block_type(block), Block.HEADING)

    def test_quote(self):
        block = ">[!INFO] QUOTE\nQuote is important part of markdown files\n"
        self.assertEqual(block_to_block_type(block), Block.QUOTE)

    def test_list_unordered(self):
        block = "- this is list elem 1\n- this is list elem2"
        self.assertEqual(block_to_block_type(block), Block.UNORDERED_LIST)

    def test_list_ordered(self):
        block = "1. this is list elem 1\n2. this is list elem2\n    1. this is list elem4"
        self.assertEqual(block_to_block_type(block), Block.ORDERED_LIST)


if __name__ == '__main__':
    unittest.main()
