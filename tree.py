class TreeNode:
    def __init__(self , data , children=[]):
        self.data = data
        self.children = children

    def addChild(self , TreeNode):
        self.children.append(TreeNode)


    def __str__(self , level=0):
        res = ' ' + level + str(self.data) + '\n'
        for child in self.children:
            res += child.__str__(level + 1)
        return res

