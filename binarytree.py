class BinaryTree:
    class Node:
        def __init__(self, val, height):
            self.val = val
            self.height = height
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
        self.height = 0

    def add(self, val):
        if self.root == None:
            self.root = self.Node(val, 0)
        else:
            self.addUtil(val, self.root, 1) 
    
    def addUtil(self, val, node, depth):
        if val == node.val:
            return

        if val > node.val and node.right == None:
            node.right = self.Node(val, depth)
            if depth > self.height:
                self.height = depth

        elif val > node.val:
            self.addUtil(val, node.right, depth+1)

        elif val < node.val and node.left == None:
            node.left = self.Node(val, depth)
            if depth > self.height:
                self.height = depth

        elif val < node.val:
            self.addUtil(val, node.left, depth+1)

    def search(self, val):
        if self.root == None:
            return False

        return self.searchUtil(val, self.root)      

    def searchUtil(self, val, node):
        if val == node.val:
            return True

        elif val < node.val and node.left != None:
            return self.searchUtil(val, node.left)

        elif val > node.val and node.right != None:
            return self.searchUtil(val, node.right)

        return False

    def toList(self):
        lst = []

        if self.root == None:
            return lst
        
        self.toListUtil(self.root, lst)

        return lst
        
    def toListUtil(self, node, lst):
        if node.left != None:
            self.toListUtil(node.left, lst)

        lst.append(node.val)

        if node.right != None:
            self.toListUtil(node.right, lst)

    def isBalanced(self):
        return self.isBalancedUtil(self.root)

    def isBalancedUtil(self, node):
        if node == None:
            return True

        self.assignHeight(node)

        if node.left == None and node.right == None:
            return True

        if node.left != None and node.right == None:
            return node.left.height == 0

        if node.left == None and node.right != None:
            return node.right.height == 0

        lh = node.left.height
        rh = node.right.height

        bl = self.isBalancedUtil(node.left)
        br = self.isBalancedUtil(node.right)

        return abs(lh - rh) <= 1 and bl and br

    def assignHeight(self, node):
        if node == None:
            return

        if node.left == None and node.right == None:
            node.height = 0

        elif node.left != None and node.right == None:
            self.assignHeight(node.left)
            node.height = node.left.height + 1
        
        elif node.left == None and node.right != None:
            self.assignHeight(node.right)
            node.height = node.right.height + 1

        elif node.left != None and node.right != None:
            self.assignHeight(node.left)
            self.assignHeight(node.right)
            node.height = 1 + max(node.left.height, node.right.height)

    def balance(self):
        nodes = self.toList()
        self.root = None
        self.balanceUtil(nodes)

    def balanceUtil(self, lst):
        medianIndex = len(lst)/2

        self.add(lst[medianIndex])

        if len(lst) == 2:
            self.add(lst[-1])               

        elif len(lst) > 2:
            left = lst[0:medianIndex]
            right = lst[medianIndex+1:]
            self.balanceUtil(left)
            self.balanceUtil(right)

bt = BinaryTree()
bt.add(100)
bt.add(80)
bt.add(120)
bt.add(90)
bt.add(70)
bt.add(130)
bt.add(110)

i = 50
while i <= 150:
    print("Contains {}: {}".format(str(i), "True" if bt.search(i) else "False"))
    i += 10

print(bt.toList())
print("Is balanced" if bt.isBalanced() else "Is not balanced")

bt.add(140)
bt.add(150)

print("Is balanced" if bt.isBalanced() else "Is not balanced")

print("Balancing...")
bt.balance()

print("Is balanced" if bt.isBalanced() else "Is not balanced")
