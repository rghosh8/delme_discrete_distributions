import unittest
import binomial_dist

class TestBinomial(unittest.TestCase):

    def test_decToBin(self):
        self.assertEqual(binomial_dist.dec_to_bin(8, n_bits=8),[0, 0, 0, 0, 1, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
