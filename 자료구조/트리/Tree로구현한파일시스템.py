import copy


def addPath(Node, params):
    addedPath = params[0]
    Node.entirePath = addedPath + Node.entirePath

class Node():

    def __str__(self):
        return self.getNodePath()

    def __init__(self, entirePath=None):
        self.entirePath = entirePath
        self.name = self.getNameFromEntirePath(entirePath=entirePath)
        self.childNodeList = []
        self.parentNode = None

    def getNameFromEntirePath(self, entirePath):
        dirList = entirePath.split("\\")

        if len(dirList) == 2 and dirList[-1] == '':
            return "\\"

        return dirList[-1]

    def haveNoChild(self):
        if len(self.getChildNodeList()) == 0:
            return True
        else:
            return False

    def iterNodes(self, startNode, nodeList = []):
        # 딸린 노드들 포함해서 반복하는 함수
        if startNode.haveNoChild:
            return [startNode]
        else:
            for child in startNode.getChildNodeList():
                nodeList.extend(self.iterNodes(child))
            nodeList.extend([child])

        return nodeList



    def iterNodes(self, startNode, func, params):
        # 딸린 노드들 포함해서 반복하고 노드마다 함수를 적용한다.

        func(startNode, params)
        for child in startNode.getChildNodeList():
            self.iterNodes(child, func, params)


    def getNodeName(self):
        return self.name

    def setParentNode(self, parentNode):
        self.parentNode = parentNode

    def addChild(self, childNode):
        added = False
        if self.childNodeList == []:
            self.childNodeList.append(childNode)
            added = True
        else:
            for i in range(len(self.childNodeList)):
                if self.childNodeList[i].getNodeName() < childNode.getNodeName():
                    added = True
                    self.childNodeList.insert(i, childNode)
        if added == False:
            self.childNodeList.append(childNode)


    def getChildNodeList(self):
        return self.childNodeList

    def getChildNode(self, name):
        for node in self.childNodeList:
            if node.getNodeName() == name:
                return node

    def getNodePath(self):
        return self.entirePath

    def getParentNode(self):
        return self.parentNode

class dirTree():

    def __init__(self):
        self.rootNode = Node(entirePath="\\")
        self.nodeCount = 1

    def getRootNode(self):
        return self.rootNode

    def getParentNodePath(self, entirePath):
        return "\\" + "\\".join(entirePath.split("\\")[1:-1])

    def addNode(self, entirePath):
        if entirePath == "\\":
            return

        newNode = Node(entirePath=entirePath)
        parentNode = self.findNode(self.getParentNodePath(entirePath=entirePath))
        parentNode.addChild(newNode)
        newNode.setParentNode(parentNode)

        self.nodeCount += 1

    def findNode(self, entirePath):
        dirListFromRoot = entirePath.split("\\")[1:]
        searchStartNode = self.rootNode

        # root node 인 경우 바로 반환

        if entirePath == "\\":
            return self.rootNode

        for dirName in dirListFromRoot:
            for childNode in searchStartNode.getChildNodeList():
                if childNode.getNodeName() == dirName:
                    searchStartNode = searchStartNode.getChildNode(dirName)
                    break

        return searchStartNode

    def printAllNode(self, startNode):

        print(startNode.getNodePath())
        for i in startNode.getChildNodeList():
            self.printAllNode(i)

    def rm(self, entirePath):
        # 전체 패스를 통해서 노드를 찾는다.
        # 해당 노드에 딸린 자식 노드들을 삭제한다.
        findNode = self.findNode(entirePath)

        if len(findNode.getChildNodeList()) == 0:
            # 자식이 없으면 del하고 빠져나온다.
            parentNode = findNode.getParentNode()
            # 부모 노드에서 자식 노드를 담아서 노드를 지운다.
            parentNode.getChildNodeList().remove(findNode)

            # 객체도 삭제한다.
            del findNode
        else:
            # 자식이 있으면 다시 rm을 실행해서 leaf 노드를 찾아간다.
            for i in findNode.getChildNodeList():
                self.rm(i.getNodePath())

            # 지우고 나면 이제 부모도 지워준다.
            self.rm(findNode.getNodePath())




    def copy(self, fromPath, toPath):
        # fromPath의 Node를 떼서 toPath로 붙인다. 이때 둘은 경로가 겹쳐도 무관
        copiedNode = self.findNode(fromPath)
        copiedNode = copy.deepcopy(copiedNode)

        # 이제 copiedNode를 돌면서 패스를 수정해줘야 한다.
        copiedNode.iterNodes(startNode=copiedNode, func=addPath, params=[toPath])

        # copyToNode
        copyToNode = self.findNode(toPath)
        copyToNode.addChild(copiedNode)



if __name__ =="__main__":
    dirs = [
        "\\",
        "\\root",
        "\\jk",
        "\\root\\jk1",
        "\\jk\\jk2"
    ]

    dirSystem = dirTree()

    ## dir 추가 끝
    for dir in dirs:
        n = Node(entirePath=dir)
        dirSystem.addNode(dir)


    dirSystem.printAllNode(startNode=dirSystem.getRootNode())

    ## dir 명령어
    # 1. rm
    # jk 폴더 삭제
    print("--rm--")
    dirSystem.rm("\\jk",)
    dirSystem.printAllNode(startNode=dirSystem.getRootNode())
    print("------")

    # 2. copy
    # 디렉토리들을 카피해서 경로에 붙이기
    dirSystem.copy("\\root", "\\root\\jk1")
    print("--copy--")
    dirSystem.printAllNode(startNode=dirSystem.getRootNode())





