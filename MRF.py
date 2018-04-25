import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu

def addNoise(image):
    output=np.copy(image)
    flags=np.random.binomial(n=1,p=0.05,size=image.shape)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if flags[i,j]:
                output[i,j]=not(output[i,j])

    return output

class MRF:
    def __init__(self):
        self.nodes=[] #Nodes on MRF
        self.id={} #Nodes on ID

    #add node at MRF
    def addNode(self,id,node):
        return self.id[id]=node

    #return node at node
    def getNode(self,id):
        return self.id[id]

    #return all nodes
    def getNodes(self):
        return self.nodes

    #start at the Belief Propagation
    def beliefPropagation(self,iter=20):

        #Initialize message from the neighborhood node
        for node in self.nodes:
            node.InitializeMessage()

        #repeat
        for t in range(iter):
            print(t)

            #send a message to the node adjacent to that node
            for node in self.nodes:
                for neighbor in node.getNeighbor():
                    neighbor.message[node]=node.sendMessage(neighbor)

        #Calculate the marginal distribution for each node
        for node in self.nodes:
            node.marginal()

class Node(object):
    
