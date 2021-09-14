# Ion Flux Relabeling
# New challenge "Ion Flux Relabeling" added to your home folder.
# Time to solve: 168 hours.
# ===================

# Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired spectacularly. 
# The Commander had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. 
# Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. 
# Commander Lambda is having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!

# Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. 
# To label them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with 
# the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

#    7
#  3   6
# 1 2 4 5

# Write a function solution(h, q) - where h is the height of the perfect tree of converters 
# and q is a list of positive integers representing different flux converters - which returns a list 
# of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, 
# or -1 if there is no such converter.  
# For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 
# in a perfect binary tree of height 3, which is [3, 6, -1].

# The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, 
# h = 2 represents a perfect binary tree with the root and two leaf nodes, 
# h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  
# The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution(5, {19, 14, 28})
# Output:
#     21,15,29

# Input:
# Solution.solution(3, {7, 3, 5, 1})
# Output:
#     -1,7,6,3

# -- Python cases --
# Input:
# solution.solution(3, [7, 3, 5, 1])
# Output:
#     -1,7,6,3

# Input:
# solution.solution(5, [19, 14, 28])
# Output:
#     21,15,29

#########
#########
#########

#design a PERFECT tree -> generate tree and nodes based on height 


class Node: 
    def __init__ (self, val=None):
        self.value = val
        self.left = None
        self.right = None
    
    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def get_left_child(self):
        return self.left

    def set_right_child(self, right):
        self.right = right

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

class Tree:
    def __init__(self, node):
        self.root = Node(node)

    def get_root(self):
        return self.root

def solution(h, q):
    node = Node()
    tree = Tree(node)
    height = h
    converters = q
    ans = []

    def generate_node(height):
        num_of_nodes = 0
        nodes = list()
        if height >= 1 and height <= 30:
            height = height - 1
            nums_of_nodes = 2**(height + 1) - 1
            for i in range(1, nums_of_nodes+1):
                nodes.append(i)
            return nodes 
    
    label = generate_node(height)

    #post order traversal
    def post_order(tree, label):
        count = 1
        i = 0
        node = tree.get_root()

        def traverse(count, node, i):
            node_val = label[i]
            if height == count:
                node.set_value(node_val) #set last left node to 1
                i += 1
                return i #go back up 1 level, if reached the end of the tree
            node.set_left_child(Node())
            if node.has_left_child(): #if node has left child, go to next layer on the left
                i =  traverse(count+1, node.left, i)
            node.set_right_child(Node())
            if node.has_right_child(): #if node has right child, go to the next level on the right
                i = traverse(count+1, node.right, i)
            node.set_value(label[i])
            i += 1
            return i
        traverse(count, node, i)

    post_order(tree, label)

    def result():
        dic = {}
        node = tree.get_root()
        dic[node.get_value()] = -1

        def dfs(node):
            if node.has_left_child() != True and node.has_right_child() != True:
                dic[node.get_value()] = -1
                return node.get_value()
            if node.has_left_child(): 
                key = dfs(node.get_left_child())
                dic[key] = node.get_value()
            if node.has_right_child(): #if node has right child, go to the next level on the right
                key = dfs(node.get_right_child())
                dic[key] = node.get_value()
            dic[node.get_value()] = -1
            return node.get_value()
        
        dfs(node)
        
        for i in converters:
            if i in dic.keys():
                ans.append(dic.get(i))

    result()
    return ans
        

# print(solution(5, [19, 14, 28]))
