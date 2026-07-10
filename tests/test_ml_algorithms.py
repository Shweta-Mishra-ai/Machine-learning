import unittest
import numpy as np
import pandas as pd
from classification.gaussian_nb_scratch import gaussian_naive_bayes
from math_foundations.softmax_scratch import softmax, cost_function, class_labels
from model_tuning.min_max_scaling import min_max_scale

class TestMLAlgorithms(unittest.TestCase):
    def test_gaussian_nb_std_guard(self):
        # Mean = 5, Std = 0 (constant column)
        mean = pd.Series([5.0])
        std = pd.Series([0.0])
        new_data = np.array([5.0])
        
        # Should not crash with division by zero. Should compute successfully.
        prob = gaussian_naive_bayes(new_data, mean, std)
        self.assertTrue(prob > 0)

    def test_softmax_properties(self):
        z = np.array([[1.0, 2.0, 3.0], [5.0, 5.0, 5.0]])
        probs = softmax(z)
        
        # Shape should be preserved
        self.assertEqual(probs.shape, z.shape)
        
        # Sum across columns should equal 1.0 (probabilities)
        np.testing.assert_allclose(np.sum(probs, axis=1), np.array([1.0, 1.0]))
        
        # Max probabilities should resolve correctly
        labels = class_labels(probs)
        self.assertEqual(labels[0], 2) # 3.0 is max at index 2
        
    def test_min_max_scaling_guard(self):
        # A matrix where one feature has constant values (range is 0)
        X = np.array([[100.0, 5.0], [200.0, 5.0], [300.0, 5.0]])
        
        # Normal scaling will cause division by zero for column 2.
        # Our scaled output should handle it without NaN or Inf crashes.
        scaled_X = min_max_scale(X)
        
        self.assertFalse(np.isnan(scaled_X).any())
        self.assertFalse(np.isinf(scaled_X).any())
        self.assertEqual(scaled_X[0, 1], 0.0)

if __name__ == "__main__":
    unittest.main()
