
import unittest

from custom_meta import CustomMeta


class ExampleClass(metaclass=CustomMeta):
    x = 1
    _y = 3

    def f(self):
        return 100

    def __fun(self):
        return 200

    def __init__(self):
        self.g = 2
        self.a = 4


class TestCustomMeta(unittest.TestCase):
    def setUp(self):
        self.cls = ExampleClass()

    def test_class_attrs(self):
        self.assertEqual(hasattr(self.cls, "x"), False)
        self.assertEqual(hasattr(self.cls, "custom_x"), True)
        self.assertEqual(hasattr(self.cls, "_y"), False)
        self.assertEqual(hasattr(self.cls, "custom__y"), True)
        self.assertEqual(hasattr(self.cls, "f"), False)
        self.assertEqual(hasattr(self.cls, "custom_f"), True)
        self.assertEqual(hasattr(self.cls, "__fun"), False)
        self.assertEqual(hasattr(self.cls, "custom__ExampleClass__fun"), True)
        self.assertEqual(hasattr(self.cls, "__init__"), True)
        self.assertEqual(hasattr(self.cls, "__doc__"), True)

    def test_instance_attrs(self):
        self.assertEqual(hasattr(self.cls, "g"), False)
        self.assertEqual(hasattr(self.cls, "custom_g"), True)
        self.assertEqual(hasattr(self.cls, "a"), False)
        self.assertEqual(hasattr(self.cls, "custom_a"), True)
        self.assertEqual(hasattr(self.cls, "__repr__"), True)
        self.assertEqual(hasattr(self.cls, "__sizeof__"), True)
        self.assertEqual(hasattr(self.cls, "__str__"), True)

if __name__ == "__main__":
    unittest.main()
