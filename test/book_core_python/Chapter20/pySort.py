# -*- coding:utf-8 -*-
# file: pySort.py
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
def inorder(node):								# 中序遍历
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def rinorder(node):								# 中序遍历,先遍历右子树
	if node.data:
		if node.right:
			rinorder(node.right)
		node.show()
		if node.left:
			rinorder(node.left)
def insert(node, value):
	if value > node.data:
		if node.right:
			insert(node.right, value)
		else:
			node.insertRight(value)
	else:
		if node.left:
			insert(node.left, value)
		else:
			node.insertLeft(value)
if __name__ == '__main__':
	l = [3, 5 , 7, 20, 43, 2, 15, 30]
	Root = BTree(l[0])							# 根节点
	node = Root
	for i in range(1, len(l)):
		insert(Root, l[i])
	print '*****************************'
	print '        从小到大'
	print '*****************************'
	inorder(Root)
	print '*****************************'
	print '        从大到小'
	print '*****************************'
	rinorder(Root)
