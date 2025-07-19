
class BinaryHeap:
    def __init__(self , size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size+1

def peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize 

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1 , rootNode.heapSize+1):
            print(i)

def heapifyTreeInsert(rootNode , index , heapType):
    if not rootNode or index <= 1 or index > rootNode.heapSize:
        return

    parentIndex = index // 2

    if heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
            heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(nodeValue , rootNode , heapType):
    if not rootNode or rootNode.heapSize + 1 >= rootNode.maxSize:
        return

    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)

