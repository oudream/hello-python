# -*- coding:utf-8 -*-
# file: pybtree.py
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
if __name__ == '__main__':
	Root = BTree('Root')							# 根节点
	A = Root.insertLeft('A')						# 向根节点中插入A节点
	C = A.insertLeft('C')							# 向A节点中插入C节点
	D = A.insertRight('D')							# 向A节点中插入D节点
	F = D.insertLeft('F')							# 向D节点中插入F节点
	G = D.insertRight('G')							# 向D节点中插入G节点
	B = Root.insertRight('B')						# 向根节点中插入B节点
	E = B.insertRight('E')							# 向B节点中插入E节点
	Root.show()								# 输出节点数据
	Root.left.show()
	Root.right.show()
	A = Root.left
	A.left.show()
	Root.left.right.show()

