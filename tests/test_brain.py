# -*- coding: utf-8 -*-
import unittest
import random

from src.brain import Brain

"""Neurosearch brain
"""

class TestBrain(unittest.TestCase):

  def think_should_have_correct_premise_values(self):
    brain = Brain(["a"], [[[0.1]],[[0.1]],[[0.1]]])
    with self.assertRaises(TypeError):
      brain.think(0.1)
    with self.assertRaises(TypeError):
      brain.think(["a"])
    with self.assertRaises(TypeError):
      brain.think([0.1,"a"])
    with self.assertRaises(ValueError):
      brain.think([0.1,0.2])

  def think_should_return_output(self):
    brain = Brain(["a"], [[[0.1]],[[0.1]],[[0.1]]])
    value = brain.think([0.1])
    self.assertTrue(type(value) is float)
    self.assertTrue(value < 1)
    self.assertTrue(value > 0)

    brain = Brain(["a"], [[[1.0]],[[0.5]],[[1.0]]])
    value = brain.think([1.0])
    self.assertTrue(round(value,2) == 0.35)
    
    brain = Brain(["a"], [[[0.5],[0.5]],[[0.5,0.5],[0.5,0.5]],[[0.5,0.5]]])
    value = brain.think([1.0])
    self.assertTrue(round(value,2) == 0.41)
    
    # Only one input but 2 weights for inputs
    brain = Brain(["a"], [[[0.5,0.5]]])
    with self.assertRaises(ValueError):
      value = brain.think([1.0])

    # One level network with 4 inputs
    values = [
      [list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4))],
      [list(float(random.uniform(0,1)) for x in range(4))]
    ]
    brain = Brain(["a","b","c","d"], values)
    value = brain.think(list(float(random.uniform(0,1)) for x in range(4)))
      
    # Two level network with 4 inputs
    values = [
      [list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4))],
      [list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4)), list(float(random.uniform(0,1)) for x in range(4))],
      [list(float(random.uniform(0,1)) for x in range(4))]
    ]
    brain = Brain(["a","b","c","d"], values)
    value = brain.think(list(float(random.uniform(0,1)) for x in range(4)))
    print(value)
      
