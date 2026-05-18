import unittest
from proj3 import *

class TestHuffmanEncoding(unittest.TestCase):
    def test_heapify_up(self):
        heap = MinHeap()
        heap = insert(heap, Node(5, "a"))
        heap = insert(heap, Node(2, "b"))
        heap = insert(heap, Node(8, "c"))

        self.assertEqual(len(heap.data), 3)
        self.assertEqual(heap.data[0].freq, 2)

    def test_insert(self):
        heap = MinHeap([Node(3, 'b'), Node(5, 'a')])
        new_heap = insert(heap, Node(4, 'c'))
        self.assertEqual(len(new_heap.data), 3)
        self.assertEqual(new_heap.data[2].char, 'c')

    def test_extract_min(self):
        heap = MinHeap([Node(3, 'b'), Node(5, 'a'), Node(4, 'c')])
        new_heap, min_node = extract_min(heap)
        self.assertEqual(min_node.char, 'b')
        self.assertEqual(len(new_heap.data), 2)

    def test_huffman_encoding_single(self):
        encoded, decoded, codes = huffman_encoding("a")
        self.assertEqual(encoded, "0")
        self.assertEqual(decoded, "a")
        self.assertEqual(codes, {'a': '0'})

    def test_huffman_encoding_repeated(self):
        encoded, decoded, codes = huffman_encoding("aaaa")
        self.assertEqual(encoded, "0000")
        self.assertEqual(decoded, "aaaa")
        self.assertEqual(codes, {'a': '0'})

    def test_empty_string(self):
        frequency = count_frequency("")
        self.assertEqual(frequency, {})

if __name__ == "__main__":
    unittest.main()

#Test heapify_up, insert, and extract_min independently.
# Test trees and encoding/decoding with edge cases (e.g., empty strings, single characters, repeated characters).
# Use assertions to check both return values and structural properties (e.g., length of heap, code lengths, tree shape).