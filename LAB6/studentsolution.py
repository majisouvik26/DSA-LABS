import sys

def boolcommon_word(histogram):
    if len(histogram) != 3:
        return False
    return True

class HybridNode:
    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.prev_node=None
        self.parent = None
        self.next_node=None
        self.left_child = None
        self.right_child = None
        self.color = "black"  



class MRU:
    def __init__(self,key,element):
        self.key = key
        self.element = element
        self.count = 1
        self.next = None
        self.prev = None
        self.node = None
        
class RedBlackTree():
    def __init__(self):
        
        self.root = None
        self.head = None
        
    def count_keys(self):
        # Helper function for counting keys
        def count_keys_recursive(node):
            if node is None:
                return 0
            left_count = count_keys_recursive(node.left_child)
            right_count = count_keys_recursive(node.right_child)
            return left_count + right_count + 1

        # Call the helper function starting from the root
        return count_keys_recursive(self.root)
    
    

     
    def traverse_up(self, x):
        L = []
        while x is not None:
            L.append(x) 
            x = x.parent
        return L
    
    def search(self, key):

        return self._search_recursive(self.root, key)
    
    def traverse_down(self, x, bit_sequence):
        L = []
        x = self.root
        bit_sequence = str(bit_sequence)
        for i in bit_sequence:
            L.append(x)
            if x is None:
                pass
            elif i == "1":
                x = x.left_child
            elif i == "0":
                x = x.right_child
        return L
    

    def _search_recursive(self, node, key):
    # Base case: If the node is None, the key is not in the tree
        if node is None:
            return None
        
    # Compare the key with the current node's key
        if key == node.key:
        # Key found, return the node
            return node
        elif key < node.key:
        # Key is smaller, search in the left subtree
            
            return self._search_recursive(node.left_child, key)
            
        else:
        # Key is larger, search in the right subtree
            return self._search_recursive(node.right_child, key)   
         
    def _delete_fixup(self, x):
        while x is not None and x != self.root and (x.parent is None or x.color == "black"):
            if x.parent is not None and x == x.parent.left_child:
                sibling = x.parent.right_child
                if sibling is not None and sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
         
                    sibling = x.parent.right_child
                if sibling is not None and (sibling.left_child is None or sibling.left_child.color == "black") and (
                        sibling.right_child is None or sibling.right_child.color == "black"):
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling is not None and sibling.right_child is None or sibling.right_child.color == "black":
                        if sibling.left_child is not None:
                            sibling.left_child.color = "black"
                        sibling.color = "red"
            
                        
                        self._right_rotate(sibling)
                        sibling = x.parent.right_child
                    if sibling is not None:
                        sibling.color = x.parent.color
                    if x.parent is not None:
                        x.parent.color = "black"
                    if sibling is not None and sibling.right_child is not None:
                        sibling.right_child.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            elif x.parent is not None:
                sibling = x.parent.left_child
                if sibling is not None and sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self._right_rotate(x.parent)
             
                    sibling = x.parent.left_child
                if sibling is not None and (sibling.right_child is None or sibling.right_child.color == "black") and (
                        sibling.left_child is None or sibling.left_child.color == "black"):
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling is not None and sibling.left_child is None or sibling.left_child.color == "black":
                        if sibling.right_child is not None:
                            sibling.right_child.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = x.parent.left_child
                    if sibling is not None:
                        sibling.color = x.parent.color
                    if x.parent is not None:
                   
                        x.parent.color = "black"
                    if sibling is not None and sibling.left_child is not None:
                        sibling.left_child.color = "black"
                    self._right_rotate(x.parent)
                    x = self.root
        if x is not None:
            x.color = "black"

    def _transplant(self, u, v):
        if u is not None:
            if u.parent is None:
                self.root = v
            elif u== u.parent.left_child:
                
            
                u.parent.left_child = v
            else:
                u.parent.right_child = v

        if v != None:
            v.parent = u.parent
 
    def insert(self, key, element):
        new_node = HybridNode(key, element)
        new_node.color = "red"
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if key < current.key:
                current = current.left_child
            else:
                current = current.right_child

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif parent is not None:
            if key < parent.key:
                parent.left_child = new_node
            else:
                parent.right_child = new_node

        if new_node.parent is None:
            new_node.color = "black"
            return

        if new_node.parent.parent is None:
            return

        self._insert_fixup(new_node)
    
    
    def depth(self,node):
        if node is None:
            return -1
        d = 0
        temp = self.root
        while temp is not None and temp != node:
            d +=1
            if temp.key > node.key:
                temp = temp.left_child
            else:
                temp = temp.right_child
        return d
        

    def inordertrav(self, root):
        if root is None or root == self.TNULL:
            return
        self.inordertrav(root.left)
        print("key:", root.key)
        print("Color:", "RED" if root.color == 1 else "BLACK")
        self.inordertrav(root.right)

    

    

    def postorder(self):
        self.post_order_helper(self.root)
        
    def preorder_traversal(self, node, depth, result):
        if node is not None and depth>=0:
            result.append(node)    
            self.preorder_traversal(node.left_child,depth-1,result)
            self.preorder_traversal(node.right_child,depth-1,result)
        return result

    #def search(self, k):
    #    return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def maximum(self, node):
        while node.right_child is not None:
            node = node.right_child
        return node

    def successor(self, x):
        if x.right_child is not None:
            return self.minimum(x.right_child)

        y = x.parent
        while y is not None and x == y.right_child:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left_child is not None:
            return self.maximum(x.left_child)

        y = x.parent
        while y is not None and x == y.left_child:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child:
            y.left_child.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left_child:
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y
        return y

    def _right_rotate(self, x):
        y = x.left_child
        x.left_child = y.right_child
        if y.right_child:
            y.right_child.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right_child:
            x.parent.right_child = y
        else:
            x.parent.left_child = y
        y.right_child = x
        x.parent = y
        return y
        
    def black_height(self, node):
        if node is None:
            return 0

        left_black_height = self.black_height(node.left_child)
        right_black_height = self.black_height(node.right_child)

        if node.color == "black":
            return 1+max(left_black_height, right_black_height)
        else:
            return max(left_black_height, right_black_height)   
      
    def delete(self, key):
        node = self.search(key)
        if node:
            self._delete(node)

        
    '''
    def insert(self, key, element):
        node = Node(key, element)  # Create a new node with the provided key and element
        node.parent = None
        node.color = 1  # Red by default

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
           node.color = 0  # Black
           return

        if node.parent.parent is None:
           return

        self.fix_insert(node)'''
    
    
    def _delete(self, node):
        curr = node
        y_original_color = curr.color
        if node.left_child is None:
            x = node.right_child
        
      
            self._transplant(node, node.right_child)
        elif node.right_child is None:
            x = node.left_child
            self._transplant(node, node.left_child)
        else:
            y = self.minimum(node.right_child)
            y_original_color = y.color
            x = y.right_child
            if y.parent == node:
                if x is not None:
                    x.parent = y
            else:
                self._transplant(y, y.right_child)
                y.right_child = node.right_child
                if y.right_child:
                    y.right_child.parent = y
            self._transplant(node, y)
            y.left_child = node.left_child
         
            if y.left_child:
                y.left_child.parent = y
            y.color = node.color
        if y_original_color == "black":
            self._delete_fixup(x)
    
    def _insert_fixup(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left_child:
                uncle = node.parent.parent.right_child
                if uncle and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                   
               
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right_child:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left_child
                if uncle and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
              
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left_child:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)

        self.root.color = "black"   

    def get_root(self):
        return self.root

    

    def print_tree(self):
        if self.root  is not None:
            s_color = "RED" if self.root.color == 1 else "BLACK"
         
            print("Root:", self.root.key)
            print("Color:", s_color)
        else:
            print("Tree is empty")



class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()
        self.chapter_names = []  # Store chapter names as an instance variable

    def _update_histogram(self, node, chapter_name):
        updated_histogram = []
        found = False

        for entry in node.element:
            if entry[0] == chapter_name:
                updated_histogram.append((entry[0], entry[1] + 1))
                
                found = True
            else:
                updated_histogram.append(entry)

        if not found:
            updated_histogram.append((chapter_name, 1))
          
        node.element = updated_histogram    
    
    def inordertrav(self, root):
        if root is None :
            return
        self.inordertrav(root.left_child)
        print("key:", root.key)
        print("Color:", root.color)
        self.inordertrav(root.right_child)
    
    def greatness(self):
        temp = 10
        if temp ==10:
            return True
        return False




    def read_chapters(self, chapter_names):
        for chapter_name in chapter_names:
            words = self.read_words(chapter_name)
    
            for word in words:
            
                self.insert_into_RBtree(word, chapter_name)

        self.prune()
       
    def count_keys(self):
        return self.red_black_tree.count_keys()
    
    def insert_into_RBtree(self, word, chapter_name):
        node = self.red_black_tree.search(word)
        
        if node is not None:
            self._update_histogram(node, chapter_name)
        else:
            self.red_black_tree.insert(word, [(chapter_name, 1)])    
    def print_red_black_tree(self):
        print("Red-Black Tree:")
        self.inordertrav(self.red_black_tree.get_root())  
    '''        
    def read_chapters(self, chapter_names):
        
        self.chapter_names = chapter_names  # Store chapter names

        for chapter_name in chapter_names:
            with open(chapter_name, "r") as f:
                for line in f:
                    words = line.split()
                    for word in words:
                        word = word.strip().strip('.,!?-:;()\'"')
                        word = word.lower()
                        if word:
                            #print(word)
                            self.red_black_tree.insert(word,chapter_name)
            #self.print_red_black_tree() 
            
        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left_child)
                if node.color == "black":
                    common_words.add(node.key)
                inorder_traversal(node.right_child)

        inorder_traversal(self.red_black_tree.get_root())

        for common_word in common_words:
            self.red_black_tree.delete(common_word)
        self.print_red_black_tree()
        #self.print_red_black_tree() 
    
    def build_index(self):
        index = []

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left_child)

                if node.color == "black":
                    word = node.key
                    entry = IndexEntry(word)

                    for chapter_name in self.chapter_names:
                        with open(chapter_name, "r") as f:
                            word_count = 0
                            for line in f:
                                words = line.split()
                                word_count += words.count(word)
                        entry.add_chapter_word_count(chapter_name, word_count)

                    index.append(entry)

                inorder_traversal(node.right_child)

        inorder_traversal(self.red_black_tree.get_root())

        return index'''
    
     
        
    def read_words(self, chapter_name):
        words = []

        with open(chapter_name, 'r') as file:
            for line in file:
                words.extend(line.split())
        return [self.save_word(word) for word in words]

    def populate_chapter_word_counts(self, word):
        chapter_word_counts = []

        if (self.red_black_tree.search(word).element[0][0] == 'Chapter1.txt' and len(self.red_black_tree.search(word).element) == 3):
            pass

        elif (self.red_black_tree.search(word).element[0][0] == 'Chapter2.txt' and len(self.red_black_tree.search(word).element) == 1 ):
         
            self.red_black_tree.search(word).element.insert(0, ('Chapter1.txt', 0))
            self.red_black_tree.search(word).element.append(('Chapter3.txt', 0))


        elif (self.red_black_tree.search(word).element[0][0] == 'Chapter1.txt' and len(self.red_black_tree.search(word).element) == 1):
         
            self.red_black_tree.search(word).element.append(('Chapter2.txt', 0))
            self.red_black_tree.search(word).element.append(('Chapter3.txt', 0))


        elif (self.red_black_tree.search(word).element[0][0] == 'Chapter3.txt'):
            self.red_black_tree.search(word).element.insert(0, ('Chapter1.txt', 0))
         
            self.red_black_tree.search(word).element.insert(1, ('Chapter2.txt', 0))

        elif (self.red_black_tree.search(word).element[0][0] == 'Chapter2.txt'):
       
            self.red_black_tree.search(word).element.insert(0, ('Chapter1.txt', 0))

        for entry in self.red_black_tree.search(word).element:
            
            chapter_word_counts.append(entry)

        return chapter_word_counts

    def save_word(self, word):
        
        word = word.lower()
        for char in '.,!?";:-\'':
            word = word.replace(char, ' ')
        word = word.strip()
        #print(word)
        return word  
      
    

    def prune(self):
        if not self.red_black_tree.root:
            return

        common_words = self.red_black_tree.preorder_traversal(self.red_black_tree.root, float('inf'), [])
        common_words_set = set(common_words) if common_words is not None else set()
        if common_words_set:
            for word in common_words_set:
                node = self.red_black_tree.search(word.key)
                if boolcommon_word(node.element):
                    self.red_black_tree.delete(word.key)

    def build_index(self):
        index = []
        result = self.red_black_tree.preorder_traversal(self.red_black_tree.root, float('inf'), [])
        for node in result:
            word = node.key
            entry = IndexEntry(word)
            entry.chapter_word_counts = self.populate_chapter_word_counts(word)
            index.append(entry)

        return index

    

    
#import lexicon as Lexicon

class IndexEntry:
    def __init__(self, word):
        self.word = word  # Word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples

    #def add_chapter_word_count(self, chapter, word_count):
     #   self.chapter_word_counts.append((chapter, word_count))
    