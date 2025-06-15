
"""

Huffman Coding
Huffman Coding
Huffman Coding is an algorithm used for lossless data compression.

Huffman Coding is also used as a component in many different compression algorithms. It is used as a component in lossless compressions such as zip, gzip, and png, and even as part of lossy compression algorithms like mp3 and jpeg.

Use the animation below to see how a text can be compressed using Huffman Coding.

Text:
lossless
Create Huffman Code
Huffman code:
UTF-8:
01101100
01101111
01110011
01110011
01101100
01100101
01110011
01110011
64 bits
Result

The animation shows how the letters in a text are normally stored using UTF-8, and how Huffman Coding makes it possible to store the same text with fewer bits.

How it works:

Count how often each piece of data occurs.
Build a binary tree, starting with the nodes with the lowest count. The new parent node has the combined count of its child nodes.
The edge from a parent gets '0' for the left child, and '1' for the edge to the right child.
In the finished binary tree, follow the edges from the root node, adding '0' or '1' for each branch, to find the new Huffman code for each piece of data.
Create the Huffman code by converting the data, piece-by-piece, into a binary code using the binary tree.
Huffman Coding uses a variable length of bits to represent each piece of data, with a shorter bit representation for the pieces of data that occurs more often.

Furthermore, Huffman Coding ensures that no code is the prefix of another code, which makes the compressed data easy to decode.

Data compression is when the original data size is reduced, but the information is mostly, or fully, kept. Sound or music files are for example usually stored in a compressed format, roughly just 10% of the original data size, but with most of the information kept.

Lossless means that even after the data is compressed, all the information is still there. This means that for example a compressed text still has all the same letters and characters as the original.

Lossy is the other variant of data compression, where some of the original information is lost, or sacrificed, so that the data can be compressed even more. Music, images, and video is normally stored and streamed with lossy compression like mp3, jpeg, and mp4.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Introduction

Unmute
Duration
2:49
/
Current Time
0:00

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Brand logo

Creating A Huffman Code Manually
To get a better understanding of how Huffman Coding works, let's create a Huffman code manually, using the same text as in the animation: 'lossless'.

A text is normally stored in the computer using UTF-8, which means that each letter is stored using 8 bits for normal latin letters, like we have in 'lossless'. Other letters or symbols such as '€' or '🦄' are stored using more bits.

To compress the text 'lossless' using Huffman Coding, we start by counting each letter.

l
o
s
e
2
1
4
1
As you can see in the nodes above, 's' occurs 4 times, 'l' occurs 2 times, and 'o' and 'e' occurs just 1 time each.

We start building the tree with the least occurring letters 'o' and 'e', and their parent node gets count '2', because the counts for letter 'o' and 'e' are summarized.

0
1
l
o
s
e
2
1
4
1
2
The next nodes that get a new parent node, are the nodes with the lowest count: 'l', and the parent node of 'o' and 'e'.

0
1
0
1
l
o
s
e
2
1
4
1
2
4
Now, the last node 's' must be added to the binary tree. Letter node 's' and the parent node with count '4' get a new parent node with count '8'.

0
1
0
1
0
1
l
o
s
e
2
1
4
1
2
4
8
Following the edges from the root node, we can now determine the Huffman code for each letter in the word 'lossless'.

0
1
0
1
0
1
l
o
s
e
2
1
4
1
2
4
8
10
110
0
111
The Huffman code for each letter can now be found under each letter node in the image above. A good thing about Huffman coding is that the most used data pieces get the shortest code, so just '0' is the code for the letter 's'.

As mentioned earlier, such normal latin letters are usually stored with UTF-8, which means they take up 8 bits each. So for example the letter 'o' is stored as '01101111' with UTF-8, but it is stored as '110' with our Huffman code for the word 'lossless'.

Note: With UTF-8, a letter has always the same binary code, but with Huffman code, the binary code for each letter (piece of data) changes with text (data set) we are compressing.

To summarize, we have now compressed the word 'lossless' from its UTF-8 code

01101100 01101111 01110011 01110011 01101100 01100101 01110011 01110011

to just

10 110 0 0 10 111 0 0

using Huffman Coding, which is a huge improvement.

But if data is stored with Huffman Coding as 10 110 0 0 10 111 0 0, or the code is sent to us, how can it be decoded so that we see what information the Huffman code contains?

Furthermore, the binary code is really 10110001011100, without the spaces, and with variable bit lengths for each piece of data, so how can the computer understand where the binary code for each piece of data starts and ends?

ADVERTISEMENT

Decoding Huffman Code
Just like with code stored as UTF-8, which our computers can already decode to the correct letters, the computer needs to know which bits represent which piece of data in the Huffman code.

So along with a Huffman code, there must also be a conversion table with information about what the Huffman binary code is for each piece of data, so that it can be decoded.

So, for this Huffman code:

100110110

With this conversion table:

Letter	Huffman Code
a	0
b	10
n	11
Are you able to decode the Huffman code?

How it works:

Start from the left in the Huffman code, and look up each bit sequence in the table.
Match each code to the corresponding letter.
Continue until the entire Huffman code is decoded.
We start with the first bit:

1
0
0
1
1
0
1
1
0
There is no letter in the table with just 1 as the Huffman code, so we continue and include the next bit as well.

1
0
0
1
1
0
1
1
0
We can see from the table that 10 is 'b', so now we have the first letter. We check the next bit:

1
0
0
1
1
0
1
1
0
We find that 0 is 'a', so now we have the two first letters 'ba' stored in the Huffman code.

We continue looking up Huffman codes in the table:

1
0
0
1
1
0
1
1
0
Code 11 is 'n'.

1
0
0
1
1
0
1
1
0
Code 0 is 'a'.

1
0
0
1
1
0
1
1
0
Code 11 is 'n'.

1
0
0
1
1
0
1
1
0
Code 0 is 'a'.

The Huffman code is now decoded, and the word is 'banana'!

ADVERTISEMENT

Huffman Code Prefixes
An interesting and very useful part of the Huffman coding algorithm is that it ensures that there is no code that is the prefix of another code.

Just image if the conversion table we just used, looked like this:

Letter	Huffman Code
a	1
b	10
n	11
If this was the case, we would get confused right from the start of the decoding, right?

1
0
0
1
1
0
1
1
0
Because how would we know if the first bit 1 represents the letter 'a' or if it is the first bit for the letter 'b' or 'c'?

This property, that no code is the prefix of another code, makes it possible to decode. And it is especially important in Huffman Coding because of the variable bit lengths.

ADVERTISEMENT

Huffman Coding Implementation
The correct word for creating Huffman code based on data or text is "encoding", and the opposite would be "decoding", when the original data or text is recreated based on the code.

The code example below takes a word, or any text really, and compress it using Huffman Coding.

Example
Huffman Coding.

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

nodes = []

def calculate_frequencies(word):
    frequencies = {}
    for char in word:
        if char not in frequencies:
            freq = word.count(char)
            frequencies[char] = freq
            nodes.append(Node(char, freq))

def build_huffman_tree():
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)

    return nodes[0]

def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_huffman_codes(node.left, current_code + '0', codes)
    generate_huffman_codes(node.right, current_code + '1', codes)

def huffman_encoding(word):
    global nodes
    nodes = []
    calculate_frequencies(word)
    root = build_huffman_tree()
    codes = {}
    generate_huffman_codes(root, '', codes)
    return codes

word = "lossless"
codes = huffman_encoding(word)
encoded_word = ''.join(codes[char] for char in word)

print("Word:", word)
print("Huffman code:", encoded_word)
print("Conversion table:", codes)
ADVERTISEMENT

Huffman Decoding Implementation
In addition to encode data using Huffman coding, we should also have a way to decode it, to recreate the original information.

The implementation below is basically the same as the previous code example, but with an additional function for decoding the Huffman code.

The huffman_decoding function takes the Huffman code, and the codes Python dictionary (a hashmap) with the characters and their corresponding binary codes. The Function then reverse the mapping, and checks the Huffman code bit-by-bit to recreate the original text.

Example
Huffman Decoding.

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

nodes = []

def calculate_frequencies(word):
    frequencies = {}
    for char in word:
        if char not in frequencies:
            freq = word.count(char)
            frequencies[char] = freq
            nodes.append(Node(char, freq))

def build_huffman_tree():
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)

    return nodes[0]

def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_huffman_codes(node.left, current_code + '0', codes)
    generate_huffman_codes(node.right, current_code + '1', codes)

def huffman_encoding(word):
    global nodes
    nodes = []
    calculate_frequencies(word)
    root = build_huffman_tree()
    codes = {}
    generate_huffman_codes(root, '', codes)
    return codes

def huffman_decoding(encoded_word, codes):
    current_code = ''
    decoded_chars = []

    # Invert the codes dictionary to get the reverse mapping
    code_to_char = {v: k for k, v in codes.items()}

    for bit in encoded_word:
        current_code += bit
        if current_code in code_to_char:
            decoded_chars.append(code_to_char[current_code])
            current_code = ''

    return ''.join(decoded_chars)

word = "lossless"
codes = huffman_encoding(word)
encoded_word = ''.join(codes[char] for char in word)
decoded_word = huffman_decoding(encoded_word, codes)

print("Initial word:", word)
print("Huffman code:", encoded_word)
print("Conversion table:", codes)
print("Decoded word:", decoded_word)














You have now seen how a text can be compressed using Huffman coding, and how a Huffman code can be decoded to recreate the original text.

Note: Huffman Coding can be used for lossless compression of any kind of data, not just text. Huffman Coding is also used as a component in other compression algorithms like zip, and even in lossy compressions like jpeg and mp3.

"""



















