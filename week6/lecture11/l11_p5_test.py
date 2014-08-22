import unittest

from week6.Lecture11.l11_p5 import hashSet


class TestIntSet(unittest.TestCase):
    
    def setUp(self):
        self.s = hashSet(3)

    def test_init(self):
        with self.assertRaises(ValueError):
            s = hashSet('a')
        with self.assertRaises(ValueError):
            s = hashSet(0) 
        with self.assertRaises(ValueError):
            s = hashSet(-2)
        s = hashSet(3)
        self.assertEqual(s.buckets, [[], [], []])

    def test_hashValue(self):
        assert self.s.hashValue(3) == 0
        assert self.s.hashValue(2) == 2

    def test_member(self):
       self.s.insert(2)
       self.s.insert(3)
       self.s.insert(4)
       assert self.s.member(2)
       assert not self.s.member(-1)


if __name__ == '__main__':
    unittest.main()
