# Matrix[Zeile][Spalte]


# Class for Artifical Neural Network

class NeuralNetwork():
    values = []
    weights = []
    # matrix with connections between Neurons. Saves neuronIndex of next layer
    connections = []
    def __init__(self, layers):
        self.layers = layers

        #initialzie values with None for layers
        tempRow = []
        for i in range(layers):
            tempRow.append(0)  # TODO: Change zeros to None
        self.values.append(tempRow)
        self.weights.append(tempRow)
        self.connections.append(tempRow)



    # Add neuron
    def addNeuron(self, layerIndex, neuronIndex, value):
        # if neuronIndex > rows of ANN: add new Row
        if neuronIndex > len(self.values)-1:
            self.addRow()
            self.addNeuron(layerIndex,neuronIndex,value)
        else:
            self.values[neuronIndex][layerIndex] = value

    def addConnection(self,layerIndex,neuronIndex, nextNeuronIndex):
        self.connections[layerIndex][neuronIndex] = nextNeuronIndex


    # Add Row to every matrix
    def addRow(self):
        self.values.append([0,0,0])
        self.weights.append([0,0,0])
        self.connections.append([0,0,0])

    # Print Methods
    # Useful Methods for information retrival and debugging

    def printValues(self):
        print("Values:")
        for i in range(len(self.values)):
            print(self.values[i])
        print("------------")

    def printConnections(self):
        print("Connections:")
        for i in range(len(self.connections)):
            print(self.connections[i])
        print("------------")

    def printNeuron(self,layerIndex, neuronIndex):
        print("Coordinate:",neuronIndex, layerIndex)
        print("Value:",self.values[neuronIndex][layerIndex])
        print("Connections to:",self.connections[neuronIndex][layerIndex])
        # //TODO: add print functions for weight, connections etc.



def main():
    # create new NeuralNetwork
    ANN = NeuralNetwork(3)
    ANN.printValues()
    ANN.addNeuron(0,3,1)
    ANN.addNeuron(1,2,2)
    ANN.addNeuron(0,0,3)
    ANN.printValues()
    ANN.printConnections()  # TODO: investigate why there is entry in connection matrix
    ANN.printNeuron(0,0)




if __name__ == "__main__":
    main()

