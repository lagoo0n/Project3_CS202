import unittest
from proj3 import *

class TestHuffmanEncoding(unittest.TestCase):
    def test_heapify_up(self):
        heap = MinHeap([Node(5, 'a'), Node(3, 'b'), Node(1, 'c')])
        new_heap = heapify_up(heap, 2)
        self.assertEqual(new_heap.data[0].char, 'c')
        self.assertEqual(new_heap.data[0].freq, 1)
        self.assertEqual(len(new_heap.data), 3)

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

    def test_encode_empty_string(self):
        encoded = encode("", {'a': '0'})
        self.assertEqual(encoded, "")
    
    def test_decode_empty_string(self):
        root = Node(1, 'a')
        decoded = decode("", root)
        self.assertEqual(decoded, "")
    
    def test_tree_shape(self):
        frequency = {'a': 5, 'b': 3, 'c': 1}
        priority_queue = create_priority_queue(frequency)
        tree = build_tree_from_queue(priority_queue)
        self.assertEqual(tree.freq, 9)
        self.assertEqual(tree.left.freq, 4)
        self.assertEqual(tree.right.freq, 5)

if __name__ == "__main__":
    unittest.main()
