import numpy as np
class Neuron :
    def __init__(self):
        self.layers = []
        self.weights = []
        self.bias = []
    def get_weight(self, inpLayerShape, outLayerShape):
        """
        PARAMETERS :
            1-->shape of input layer(must be an integer)
            2-->shape of output layer
        Return : weight numpy matrix
            shape(weight) = (m, n)
            where 
                m = shape of output row vector
                n = shape of input row vector
        """
        n = inpLayerShape
        m = outLayerShape
        W = np.random.uniform(10, size = (m, n))
        return W
    def get_bias(self, outLayerShape):
        """
        PARAMETERS :
            1-->shape of output layer
        Return : bias numpy matrix
        """
        bias = np.random.uniform(10, shape = (1, outLayerShape))
        return bias
    def init_layer(self, input_shape, output_shape):
        """
        PARAMETERS :
            1-->shape of input layer
            2-->shape of output layer
        RETURN : nothing 
            -->initialize self.layer, self.bias and self.weights
            -->shape(layer) = (1, n)
            -->shape(weight) = (m, n)
            -->shape(bias) = (1, m)
            where n = shape of input row vector
                m = shape of output row vector
        """
        weight = self.get_weights(input_shape, output_shape)
        layer = np.ones((1, output_shape))
        bias = self.get_bias(output_shape)
        self.weights.append(weight)
        self.bias.append(bias)
        self.layers.append(layer)
