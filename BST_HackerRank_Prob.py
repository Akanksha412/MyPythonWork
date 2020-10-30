{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "4 2 3 1 7 6\n",
      "4 2 1 3 7 6 "
     ]
    }
   ],
   "source": [
    "\n",
    "class Node:\n",
    "    def __init__(self, info):\n",
    "        self.info = info  \n",
    "        self.left = None  \n",
    "        self.right = None \n",
    "        self.level = None \n",
    "\n",
    "    def __str__(self):\n",
    "        return str(self.info) \n",
    "\n",
    "def preOrder(root):\n",
    "    if root == None:\n",
    "        return\n",
    "    print (root.info, end=\" \")\n",
    "    preOrder(root.left)\n",
    "    preOrder(root.right)\n",
    "    \n",
    "class BinarySearchTree:\n",
    "    def __init__(self): \n",
    "        self.root = None\n",
    "    def insert(self, val):\n",
    "        data = Node(val)\n",
    "        #If the root is Null\n",
    "        if self.root is None:\n",
    "            self.root = data\n",
    "            return\n",
    "        current = self.root\n",
    "        #If the root is greater than value\n",
    "        while current:\n",
    "            if val < current.info:\n",
    "                if current.left is None:\n",
    "                    current.left = data\n",
    "                    return\n",
    "                current = current.left\n",
    "            #if the root is less than value\n",
    "            elif val > current.info:\n",
    "                if current.right is None:\n",
    "                    current.right = data\n",
    "                    return\n",
    "                current = current.right\n",
    "\n",
    "tree = BinarySearchTree()\n",
    "t = int(input())\n",
    "\n",
    "arr = list(map(int, input().split()))\n",
    "\n",
    "for i in range(t):\n",
    "    tree.insert(arr[i])\n",
    "\n",
    "preOrder(tree.root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
