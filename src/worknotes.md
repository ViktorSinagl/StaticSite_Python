# Work-notes
- block_to_block_type function written.
  - need to be tested if work's correctly, then proceed to next assignment

# TO-DO
- [ ] printing the html --> allow tag.text to be printed without tags !!
- [ ] only paragraph can have child notes, all other block_types will be  leaf nodes --> change markdown_to_html_node function
- [ ] unitest ?


# Assignments
## Chapter 4: Blocks
### Block types

We will support 6 types of markdown blocks:

    "paragraph"
    "heading"
    "code"
    "quote"
    "unordered_list"
    "ordered_list"

We need a way to inspect a block of markdown text and determine what type of block it is.
Assignment

Create a block_to_block_type function that takes a single block of markdown text as input and returns the type of block it is. You can assume it's had any leading or trailing whitespace stripped (we did that in a previous lesson).

Here are some tips:

    I recommend creating variables that represent each block type and importing them wherever you need to use them, e.g. block_type_paragraph = "paragraph".
    Headings start with 1-6 # characters, followed by a space and then the heading text.
    Code blocks must start with 3 backticks and end with 3 backticks.
    Every line in a quote block must start with a > character.
    Every line in an unordered list block must start with a * or - character, followed by a space.
    Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    If none of the above conditions are met, the block is a normal paragraph.

### I'am the Peacock !
    - Split the markdown into blocks (you already have a function for this)
    - Loop over each block:
        Determine the type of block (you already have a function for this)
        Based on the type of block, create a new HTMLNode with the proper data
        Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
    - Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.

