import unittest

from hello_world import greet


class TestSum(unittest.TestCase):

    def test_say_hello(self):
        hello_world = greet.hello_world()
        self.assertEqual(hello_world.say_hello(), "Hello, World!")

    def test_say_hello_const_parameter(self):
        hello_world = greet.hello_world("Rajendra")
        self.assertEqual(hello_world.say_hello(), "Hello, Rajendra!")

    def test_say_hello_with_parameter(self):
        hello_world = greet.hello_world()
        self.assertNotEqual(hello_world.say_hello(), "Hello, Rajendra!")


if __name__ == '__main__':
    unittest.main()
