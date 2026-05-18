from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    new_heap = heap.data[:]

    if index == 0:
        return MinHeap(new_heap)
    
    parent = (index - 1) // 2

    if new_heap[index] < new_heap[parent]:
        temp = new_heap[index]
        new_heap[index] = new_heap[parent]
        new_heap[parent] = temp
        return heapify_up(MinHeap(new_heap), parent)
    
    return MinHeap(new_heap)

def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_heap = heap.data + [element]
    new_heap = heapify_up(MinHeap(new_heap), len(new_heap) - 1)
    return new_heap

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    new_heap = heap.data[:]
    left = 2 * index + 1
    right = 2 * index + 2
    size = len(new_heap)

    smallest = left 

    if right < size and new_heap[right] < new_heap[left]:
        smallest = right
    
    if new_heap[smallest] < new_heap[index]:
        temp = new_heap[index]
        new_heap[index] = new_heap[smallest]
        new_heap[smallest] = temp
        return heapify_down(MinHeap(new_heap), smallest)
    
    return MinHeap(new_heap)


def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    last_value = heap.data[-1]
    new_heap = [last_value] + heap.data[1:-1]

    min_element = heap.data[0]

    new_heap = heapify_down(MinHeap(new_heap), 0)
    return MinHeap(new_heap), min_element
        
def count_frequency(s: str)-> dict[str,int]:
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    heap = MinHeap()
    for char, freq in frequency.items():
        node = Node(freq,char)
        heap = insert(heap, node)
    return heap


def build_tree(priority_queue: MinHeap) -> Node:
    while len(priority_queue.data) > 1:

        priority_queue, left = extract_min(priority_queue)
        priority_queue, right = extract_min(priority_queue)

        merged_freq = left.freq + right.freq
        merged_node = Node(merged_freq, '', left, right)
        priority_queue = insert(priority_queue, merged_node)

    priority_queue, root = extract_min(priority_queue)
    return root


def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}  
    


def encode(s: str, codes: dict)-> str:
    pass


def decode(encoded_string: str, root: Node):
    pass

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes

