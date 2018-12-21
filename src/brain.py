# -*- coding: utf-8 -*-
import math

"""Neurosearch brain
"""
class Brain:

    def __init__(self, premise_types, weights):
        """
        Initialize a Brain with an list of weights.
    

        Args:
             premises: a list of a names of premises, inputs of a network
             weights : a list of lists containing neuron weights.
                       Example: [[level1 weights...], [level2 weights], ...]

        """
        self.premise_types = premise_types
        self.weights = weights

    def propagate(self, inputs, weight_values):
        """

        Args:
             inputs: input values as list of floats, e.g. [input1, input2,...]
             weight_values: weight values as a list of floats.
                            [[input1-node1w, input2-node1w, ...], [input1-nodexw,...]]

        Example:
             inputs: [1.0, 1.5, 1.3]
             weights_values: [[x,x,x],[x,x,x],[x,x,x],...] 
        
        """
        nodes = []
        for weights in weight_values:
            if len(weights) != len(inputs):
                raise ValueError("Must have a single weight for a input when propagating a node, weights:{0} inputs:{1}".format(len(weights), len(inputs)))
            weighted_sum = 0.0
            for v in inputs:
                weighted_sum += weights[inputs.index(v)]*v

            # Activation function
            total = math.tanh(weighted_sum)

            nodes.append(total)

        return nodes

    def think(self, premise_values):
        """
        Process through neural network.
        
        Args:
        premise_values: a list of decimal input values. Each value must
                        be between 0..1. Must have equal amount as
                        initialized inputs. 
        """

        if not type(premise_values) is list:
            raise TypeError("Premise values must be given as a list")
        for value in premise_values:
            if not type(value) is float:
                raise TypeError("Premise values must be decimal numbers")
        if len(self.premise_types) != len(premise_values):
            raise ValueError("You must give equal amount of premise types and values")

        inputs = premise_values
        for weights in self.weights:
            inputs = self.propagate(inputs, weights)

        if len(inputs) != 1:
            raise ValueError("Weights are not given correctly, result has multiple values")

        return inputs[0]


    
