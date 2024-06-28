import unittest

from main import markdown_to_blocks
class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_string1(self):
        markdown_origin = """# This is first heading
- with one list element

# There is another heading

here is list
- **bold** text
- *italic* text"""
        test_result = ['# This is first heading\n- with one list element', '# There is another heading', 'here is list\n- **bold** text\n- *italic* text']
        result = markdown_to_blocks(markdown_origin)
        print(result)
        #self.assertEqual(test_result, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
