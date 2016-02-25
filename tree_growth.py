class TreeGrowth():
    """Algorithm 4.1 from page 164 in Introduction to Datamining"""

    def __init__(self, trainingRecords, attributeSet):
        
        self.trainingRecords = trainingRecords
        self.attributeSet = attributeSet
        
        self.maxDepth = 20
        
        return None
    
    def getTreeGrowth(self):
        
        return self._process(self.trainingRecords, self.attributeSet)
        
        
    def _process(self, trainingRecords, attributeSet):
        
        if self.stoppingCond(trainingRecords, attributeSet) == True:
            leaf = CreateNode() #a node that either has a testCond(a list) or a class label, and a descendant list(two legs?)
            leaf.setLabel(self.classify(trainingRecords))
            return leaf
        
        root = CreateNode()
        root.setTestCond(self.findBestSplit(trainingRecords, attributeSet))
        
        """let V = {v|v is a possible outcome of root.testCond } """
        
        Ev = []
        
        for v in root.getTestCond(): #for each v in V. V should just be two grouped lists [[], []] with attributes
            for e in trainingRecords:
                if root.testCond(e) == v: #sort the records for the child
                    Ev.append(e)
                    
            child = self._process(Ev, attributeSet) #grow tree further
            root.addChild(child, v) #label the edge root -> child as v and add the child to root
            
        return root

    def stoppingCond(self, trainingRecords, attributeSet):
        
        self.maxDepth += 1
        if(self.maxDepth >= 20):
            return True
        
        return False
    
    def classify(self, trainingRecords):
        return None
    
    def findBestSplit(self, trainingRecords, attributeSet):
        return None

class CreateNode():
    
    def setLabel(self, label):
        return None
    
    def setTestCond(self, testCond):
        return None
    
    def getTestCond(self):
        return [None, None]
    
    def testCond(self, trainingRecord):
        return None
    
    def addChild(self, child, edgeLabel):
        return None
        
        
"""trainrec = [1,2,3,4,5]
attrset = ['good', 'bad', 'better', 'pizza']

myTree = TreeGrowth(trainrec, attrset)

myTree.getTreeGrowth()"""
