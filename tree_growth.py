class TreeGrowth():
    """Algorithm 4.1 from page 164 in Introduction to Datamining"""

    def __init__(self, trainingRecords, attributeSet):
        
        self.trainingRecords = trainingRecords
        self.attributeSet = attributeSet
        self.label = ""
        self.leftNode = TreeGrowth
        self.rightNode = TreeGrowth
        self.testCond = [[],[]]

        
        self.maxDepth = 20
        

    
    def getTreeGrowth(self):
        
        return self._process(self.trainingRecords, self.attributeSet)
        
        
    def _process(self, trainingRecords, attributeSet):
        #this row is prolly not riht, regarding the params. Check this out, this is cause of the change to delete the class node, the tree should contain trainingrecords? And a attribute set?
        if self.stoppingCond(trainingRecords, attributeSet) == True:
            leaf = TreeGrowth([],[]) #a node that either has a testCond(a list) or a class label, and a descendant list(two legs?)
            leaf.setLabel(self.classify(trainingRecords))
            return leaf

        #This is the same as before the root should prolly contain trainingRecords and a attribute set?
        root = TreeGrowth([],[])
        root.setTestCond(self.findBestSplit(trainingRecords, attributeSet))
        
        """let V = {v|v is a possible outcome of root.testCond } """
        
        Ev = []
        
        for v in root.getTestCond(): #for each v in V. V should just be two grouped lists [[], []] with attributes
            for e in trainingRecords:
                if (root.testCond(e) == v): #sort the records for the child
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

    
    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label
    
    def setTestCond(self, testCond):
        self.testCond = testCond
    
    def getTestCond(self):
        return self.testCond
    
    def testCond(self, trainingRecord):
        ###What's this functions use?
        return True
    
    def addChild(self, child, edgeLabel):
        if(edgeLabel == "rightNode"):
            self.rightNode = child
        elif(edgeLabel == "leftNode"):
            self.leftNode = child

        
        
"""trainrec = [1,2,3,4,5]
attrset = ['good', 'bad', 'better', 'pizza']

myTree = TreeGrowth(trainrec, attrset)

myTree.getTreeGrowth()"""
