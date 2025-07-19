
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
            print(rootNode.customList[i])

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

def heapifyExtractTree(rootNode , index , heapType):
    leftIndex = index*2
    rightIndex = index*2 + 1
    swapChild = 0

    if index > rootNode.heapSize :
        return

    elif rootNode.heapSize == leftIndex :
        if heapType == "min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
        elif heapType == "max":
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]

    else:
        if heapType == "min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
                heapifyExtractTree(rootNode, swapChild, heapType)

        elif heapType == "max":
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
                heapifyExtractTree(rootNode, swapChild, heapType)

def extractNode(rootNode , heapType):
    if rootNode.heapize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtractTree(rootNode, 1, heapType)
        return extractedNode

def deleteHeap(rootNode):
    if not rootNode:
        return
    else:
        rootNode.customList = None
        rootNode.heapSize = 0
        rootNode.maxSize = 0
        return True