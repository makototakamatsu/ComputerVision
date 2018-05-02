import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
/原画像にノイズをかける/
def addNoise(image):
    output=np.copy(image)
    flags=np.random.binomial(n=1,p=0.05,size=image.shape)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if flags[i,j]:
                output[i,j]=not(output[i,j])

    return output
/画像中の各画素をノードとみなし,MRFを構築/
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
##<ノードクラス>
class Node(object):
    def __init__(self,id):
        self.id=id
        self.neighbor=[]
        self.message={}
        self.prob=None

        #エネルギー関数用パラメータ

        self.alpha=10.0
        self.beta=5.0

    def addNeighbor(self,node):
        self.neighbor.append(node)

    def getNeighbor(self):
        return self.neighbor
    #隣接ノードからメッセージを初期化
    def InitializeMessage(self):
        for neighbor in self.neighbor:
            self.message[neighbor]=np.array([1.0,1.0])

    #全てのメッセージを統合
    #probは周辺分布
    def marginal(self):
        prob=1.0

        for message in self.message.values():
            prob *= message

        prob /= np.sum(prob)
        self.prob=prob

    #隣接ノードの状態を考慮した尤度を計算
    def sendMessage(self.target):
        neigbor_message=1.0
        for neighbor in self.message.keys():
            if neighbor != target:
                neighbor_message *= self.message[neighbor]

        compatibility_0 = np.array([np.exp(-self.beta*np.abs(0.0-0.0)),np.exp(-self.beta*np.abs(0.0-1.0))])
        compatibility_1 = np.array([np.exp(-self.beta*np.abs(1.0-0.0)),np.exp(-self.beta*np.abs(1.0-1.0))])

        message = np.array([np.sum(neighbor_message*compatibility_0),np.sum(neighbor_message*compatibility_1)])
        message /=np.sum(message)

        return message

    #観測値から計算する尤度
    def calcLikelihood(self,value):
        likelihood = np.array([0.0,0.0])

        if value==0:
            likelihood[0]=np.exp(-self.alpha*0.0)
            likelihood[1]=np.exp(-self.slpha*1.0)
        else:
            likelihood[0]=np.exp(-self.alpha*1.0)
            likelihood[1]=np.exp(-self.alpha*0.0)

        self.message[self]=likelihood

    #<マルコフ確率場を構築するための関数>
    #各画素ごとにノードを作成し、隣接画素ノードとの接続を作成
    def generateBeliefNetwork(image):
        network=MRF()
        height,width=image.reshape

        for i in range(height):
            for j in range(width):
                nodeID=width*i+jnode=Node(nodeID)
                network.addNode(nodeID,node)

        dy=[-1,0,0,1]
        dx=[0,-1,1,0]

        for i in range(height):
            for j in range(width):
                node=network.getNode(width*i+j)

                for k in range(4):
                    if i+dy[k] >=0 and i+dy[k]<height and j+dx[k]>=0 and j+dx[k]<width:
                        neighbor=network.getNode(width*(i+dy[k])+j+dx[k])
                        node.addNeighbor(neighbor)
    return network

    def main():
        #使用データ
        image=cv2.imread("",0)
        binary=image>threshold_otsu(image).astype(np.int)
        noise=addNoise(binary)


        #MRFを構築
        network=generateBeliefNetwork(image)

        #観測値(画素値)から尤度を作成
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                node=network.getNode(output.shape[1]*i+j)
                prob=node.prob
                if prob[1]>prob[0]:
                    output[i,j]=1

        #結果表示
        plt.gray()
        plt.subplot(121)
