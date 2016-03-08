from pandas import read_csv
import scipy.stats
from numpy import loadtxt

import numpy as np

#data = read_csv('resources/raop.csv')
data = read_csv('resources/raop.csv', header=None, skiprows=[0], nrows=3)

#print(data) # pandas data-frame
#print(data.values) # numpy-array containing values

class TreeGrowth():
    """Algorithm 4.1 from page 164 in Introduction to Datamining"""

    def __init__(self, trainingRecords, attributeSet):
       
        self.trainingRecords = trainingRecords
        self.attributeSet = attributeSet
        self.bestSplit = float("-inf")
        self.maxDepth = 20

        self.rightChild
        self.leftChild
       
        return None
   
    def getTreeGrowth(self):
       
        return self._process(self.trainingRecords, self.attributeSet)
       
       
    def _process(self, trainingRecords, attributeSet):
       
        if self.stoppingCond(trainingRecords, attributeSet) == True:
            leaf = TreeGrowth() #a node that either has a testCond(a list) or a class label, and a descendant list(two legs?)
            leaf.setLabel(self.classify(trainingRecords))
            return leaf

        self.bestSplit= self.findBestSplit(trainingRecords, attributeSet)

        """let V = {v|v is a possible outcome of root.testCond } """
       
        Evl = []
        Evr = []
        #for v in self.getTestCond(): #for each v in V. V should just be two grouped lists [[], []] with attributes
        for e in trainingRecords:
                if (self.bestSplit < v): #sort the records for the child
                    a = e[0:]
                    Evl.append(e)
                else:
                    Evr.append(e)

        self.leftChild = TreeGrowth(Evl, attributeSet)
        self.rightChild = TreeGrowth(Evr, attributeSet)


            #self.addChild(child, v) #label the edge root -> child as v and add the child to root
           
        return self

    def stoppingCond(self, trainingRecords, attributeSet):
       
        self.maxDepth += 1
        if(self.maxDepth >= 20):
            return True
       
        return False
   
    def classify(self, trainingRecords):
        return None
   
    def findBestSplit(self, trainingRecords, attributeSet):
        return None
   
    def gini(records):
        """gini selects the first column in the numpy array, sorts it
        and selects the best value for partitioning the records with the
        lowest value for the class"""

        gini_value = 0

        arr2 = records[np.lexsort(np.fliplr(records).T)] #sort on first column

        sorted_column = np.array(arr2[:,0]) #select first column

        last_column = np.array(arr2[:,-1])

        work_arr = np.concatenate(sorted_column, last_column)

        split_value = (sorted_column[0] + sorted_column[1]) / 2
       
        for value in sorted_column:
           
            if value < split_value:
                left_value +=1
               
            if value >= split_value:
                right_value += 1
               
            count_values += 1



    def count_classes(self, records):
        return 0

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

"""
arr = np.core.records.array(data.values)

print arr

arr.sort(axis=0)

print arr
"""

arr = data.values #np.genfromtxt('resources/raop.csv', skip_header=1, delimiter=',', skip_footer=4037, dtype=None)

print arr

#arr.sort(arr.view('f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8'), order=['f1'], axis=1).view(np.float)

array = np.array([[5,4,3,6,7,14,12,25],[1,2,3,5,6,27,24,45],[5,6,3,8,3,1,2,43], [2,4,3,5,3,15,2,2], [2,9,12,20,1,17,27,1]])

array2=np.delete(array, np.s_[:1],1) #used to deletet the first column

#arr2 = array[np.lexsort(np.fliplr(array).T)] #anvands for att sortera pa forsta kolumnen
#arr2 = arr[np.lexsort(np.fliplr(arr).T) ]

print array2

a = np.array([[1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]])

b = np.array(a[:,0])

print b

c = np.array(a[:,-1])

print c

#d = np.concatenate(b,c)

#print d
