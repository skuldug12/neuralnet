eulersnum = 2.718281828459045 #constant
all_layers = {}

class inputNeuron(weight, active):
    def __init__(self, weight, active):
        self.weight = weight
        self.active = active
        self.output = 0

    def calculateoutput():
        self.output = self.weight * self.active

class sigmoidNeuron(weight, bias, previouslayer):
    def __init__(self, weight, bias, previouslayer):
        self.previouslayer = previouslayer
        self.bias = bias
        self.sum = 0
        self.output = 0

    def calculateoutput():
        for neuron in self.previouslayer:
            self.sum -= neuron.output
        self.sum -= self.bias

        self.output = 1/(1 + (eulersnum**self.sum))

class network():
    def __init__(self):
        self.layers = 0

    def setup():
        self.layers = int(input("how manys layer (1st is input): "))
        if self.layers >= 1:
            for layer in range(self.layers):
                all_layers["layer{}".format(layer)] = {}
                if layer == 1:
                    inputneuroncount = int(input("how many input neurons: "))
                    for inputneuron in range(inputneuroncount):
                        weight = int(input("weight for {}: ".format(inputneuron)))
                        active = int(input("is {} active: ".format(inputneuron)))
                        all_layers["layer{}".format(layer)]["inputneuron{}".format(inputneuron)] = inputNeuron(weight, active)
                else:
                    sigmoidneuroncount = int(input("how many input neurons: "))
