
#二叉树模板
class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.t=right=right

class Tree:
    def __init__(self,maxnode):
        self.root=None
        self.nodes=[TreeNode() for _ in range(maxnode)]
        self.treesize=maxnode

    def GetTreeNode(self,id):
        return self.nodes[id]
    
    def visit(self,node):
        print(node.val,end=' ')
    

    #这个函数最后得到了 nowNode ，我们读函数可以知道，这个nowNode其实就是root，于是我们还需要一个函数去给root赋值为这个nowNode
    def Create(self,a,size,nodeid):
        if nodeid>=size or a[nodeid]==None:
            return None
        nowNode=self.GetTreeNode(nodeid)
        nowNode.val=a[nodeid]
        nowNode.left=self.Create(a,size,nodeid*2)
        nowNode.right=self.Create(a,size,nodeid*2+1)
        return nowNode
    
    def CreateTree(self,a):
        self.root=self.Create(a,len(a),1)

    #前序遍历
    def preOrder(self,node):
        if node:
            self.visit(node)
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    #这个函数主要是不让成员变量在类外暴露出来，不需要传参
    def preOrderTree(self):
        self.preOrder(self.root)
        print(' ')
    
    #中序遍历
    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            self.visit(node)
            self.inOrder(node.right)
    
    def inOrderTree(self):
        self.inOrder(self.root)
        print(' ')

    #后序遍历
    def postOrder(self,node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.visit(node)
    
    def postOrderTree(self):
        self.postOrder(self.root)
        print(' ')



