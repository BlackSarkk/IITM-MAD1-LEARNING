
# Efficiency?
- Most common language on WEB?
    - English, as of now
- Should all characters be represented with same number of Bits?
    - Not necessarily.

- Example:
    - Text document with 1000 words, approximately 5000 characters (including spaces)
        - UCS-4 encoding: 32b x 5000 = 160,000 bits
        - ASCII encoding: 8b x 5000 = 40,000 bits
        - Orignal 7-bit ASCII sufficient for English: 7b x 5000 = 35,000 bits
        - Minimum needed to encode just 'a' - 'z', numbers and some special chars: could filt in 6bits: 30,000 bits
        - Optimal coding based on frequency of occurance;
            - "e" is most common letter, 't', 'a', 'o', ...
            - Huffman or similar encoding: ~ 10-20,000 bits, possibly less
        - If a document contains hundreds of repeated characters like “aaaaaa…”, run-length encoding (RLE) can store it as a*100, which can be less than 100 bits.
        - The optimal encoding depends on the specific content of the document.


# Solvable in general?
- Impossible to encode by actual character frequency: depends on text
    - Just use compression methods like "zip" instead!

- But can endocing be a good halfway point?

- Example:
    - Use 1 byte for most common aphabets
    - Group otehrs according to frequency, have "prefix" codes to indicate

- So they came up with a solution:
    - If the very first bit starts with 0 (0xxxxxx), treat the remaining 7 free bits as orignal ASCII --> 127 possibilities

- PREFIX ENCODING:
__1st byte__|__2nd byte__|__3rd byte__|__4th byte__|__Free Bits______|  Maximum  Expressible unicode value
            |            |            |            |                 |
  0xxxxxxx  |            |            |            |  7              |  007F hex(127)
  110xxxxx  |  10xxxxxx  |            |            |  (5+6) = 11     |  07FF hex(2047)
  1110xxxx  |  10xxxxxx  |  10xxxxxx  |            |  (4+6+6) = 16   |  FFFF hex(65535)
  11110xxx  |  10xxxxxx  |  10xxxxxx  |  10xxxxxx  |  (3+6+6+6) = 21 |  10FFFF hex (1,114,111)


# UTF-8 (unicode tranformation format)
- Use 8 bits for most common characters: ASCII subset
    - All ASCII documents are automatically UTF-8 compitable
- ALl other characters can be encoded based on prefix string
- More difficult for text processor:
    - First check prefix
    - Linked list through chain of prefixes possible
    - Still more efficient for majority of documents
- Most common encoding in use today


# Why UTF-8?
- We can use ASCII encoding for most tasks as long as we’re dealing only with English text (basic letters, digits, and common punctuation).
- The problem arises when we start handling non-English characters, such as letters with accents (é, ñ), emoji, or special symbols — because ASCII can’t represent them.
- To handle such diverse characters, we need to use Unicode encodings like UTF-8, which can represent virtually every character in every language.




- There are meta tags we can use in our documents to specify the encoding 
- It is a good practice to mention it there
