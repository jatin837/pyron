import unittest
import neuNets
import numpy as np
neuron = neuNets.Neuron()
class TestNeuNets(unittest.TestCase):

    def test_get_weight(self):
        inpLayerShape = np.random.randint(low = 5, high = 100)
        outLayerShape = np.random.randint(low = 5, high = 100)
        weight = neuron.get_weight(inpLayerShape, outLayerShape)
        m = weight.shape[0]
        n = weight.shape[1]
        self.assertTrue(m == outLayerShape and n == inpLayerShape)


if __name__ == '__main__':
    for i in range(100):
        unittest.main()
