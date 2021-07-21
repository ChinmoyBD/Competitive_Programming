class Node:
    def getHeight(self, root):
        print(root)
        if root:
            leftDepth = self.getHeight(root.left)
            rightDepth = self.getHeight(root.right)

            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1
        else:
            return -1


class Solution(Node):
    def insert(self, root, node):
        pass


# T = int(input())
myTree = Solution()
root = [3, 5, 2, 1, 4, 6, 7]
'''for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)'''
height = myTree.getHeight(root)
print(height)