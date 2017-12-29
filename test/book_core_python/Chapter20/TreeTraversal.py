# -*- coding:utf-8 -*-
# file: TreeTraversal.py
#
class BTree:									# 二叉树节点
	def __init__(self, value):						# 初始化函数
		self.left = None						# 左儿子
		self.data = value						# 节点值
		self.right = None						# 右儿子
	def insertLeft(self, value):						# 向左子树插入节点
		self.left = BTree(value)
		return self.left
	def insertRight(self, value):						# 向右子树插入节点
		self.right = BTree(value)
		return self.right
	def show(self):								# 输出节点数据
		print self.data
def preorder(node):								# 先序遍历
	if node.data:
		node.show()
		if node.left:
			preorder(node.left)
		if node.right:
			preorder(node.right)
def inorder(node):								# 中序遍历
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def postorder(node):								# 后序遍历
	if node.data:
		if node.left:
			postorder(node.left)
		if node.right:
			postorder(node.right)
		node.show()
if __name__ == '__main__':
	Root = BTree('Root')							# 构建树
	A = Root.insertLeft('A')
	C = A.insertLeft('C')
	D = A.insertRight('D')
	F = D.insertLeft('F')
	G = D.insertRight('G')
	B = Root.insertRight('B')
	E = B.insertRight('E')
	print '*************************'
	print 'Binary Tree Pre-Traversal'
	print '*************************'
	preorder(Root)								# 对树进行先序遍历
	print '*************************'
	print 'Binary Tree In-Traversal'
	print '*************************'
	inorder(Root)								# 对树进行中序遍历
	print '*************************'
	print 'Binary Tree Post-Traversal'
	print '*************************'
	postorder(Root)								# 对树进行后序遍历
