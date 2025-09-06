# Matrix[Zeile][Spalte]


# Class for Artifical Neural Network

class NeuralNetwork():

    def __init__(self, layers):
        self.layers = layers
        self.values = []
        # matrix with connections between Neurons. Saves neuronIndex of next layer
        self.weights = []



        #initialzie values with None for layers
        tempRow = [0] * self.layers # TODO: Change zeros to None
        self.values.append(tempRow.copy())

        weightTemp = []
        [weightTemp.append([]) for _ in range(self.layers)]
        self.weights.append(weightTemp)





    # Add neuron
    def addNeuron(self, layerIndex, neuronIndex, value):
        # if neuronIndex > rows of ANN: add new Row
        if neuronIndex > len(self.values)-1:
            self.addRow()
            self.addNeuron(layerIndex,neuronIndex,value)
        else:
            self.values[neuronIndex][layerIndex] = value


    def addWeight(self,layerIndex,neuronIndex, nextNeuronIndex, weight):
        # Data structure: [nextNeuronIndex,weight]
        self.weights[layerIndex][neuronIndex].append([nextNeuronIndex,weight])


    # Add Row to every matrix
    def addRow(self):
        self.values.append([0]* self.layers)

        weightTemp = []
        [weightTemp.append([]) for _ in range(self.layers)]
        self.weights.append(weightTemp)

    # Print Methods
    # Useful Methods for information retrival and debugging

    def printValues(self):
        print("Values:")
        for i in range(len(self.values)):
            print(self.values[i])
        print("------------")

    def printConnections(self):
        # TODO: Extract only connections from weights
        print("Connections:")

    def printWeights(self):
        print("Weights:")
        for i in range(len(self.weights)):
            print(self.weights[i])
        print("------------")

    def printNeuron(self,layerIndex, neuronIndex):
        print("Coordinate:",neuronIndex, layerIndex)
        print("Value:",self.values[neuronIndex][layerIndex])
        weightEntry = self.weights[neuronIndex][layerIndex];
        [print("Connections to:",weightEntry[i][0],"with weight:",self.weights[neuronIndex][layerIndex][i][1]) for i in range(len(weightEntry))]
        # //TODO: add print functions for weight, connections etc.

    # Setter

    def setWeight(self,layerIndex, neuronIndex,nextNeuronIndex, newWeight):

        cell = self.weights[neuronIndex][layerIndex]

        # Search in cell [layerIndex, neuronIndex] for nextNeuron Index
        match = [sub for sub in cell if sub[0] == nextNeuronIndex]
        match[0][1] = newWeight




def main():
    # create new NeuralNetwork
    ANN = NeuralNetwork(3)
    ANN.addNeuron(0,3,1)
    ANN.addNeuron(1,2,2)
    ANN.addNeuron(0,0,3)
    ANN.addWeight(0,0,1,1.5)
    ANN.addWeight(0,0,2,2.5)
    ANN.setWeight(0,0,1,3.5)
    ANN.printNeuron(0,0)


if __name__ == "__main__":
    main()

