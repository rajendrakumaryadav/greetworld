import unittest

from greetworld import greet


class TestSum(unittest.TestCase):
	
	def test_say_hello(self):
		hello_world = greet.greet()
		self.assertEqual(hello_world.say_hello(), "Hello, World!")
	
	def test_say_hello_const_parameter(self):
		hello_world = greet.greet("Rajendra")
		self.assertEqual(hello_world.say_hello(), "Hello, Rajendra!")
	
	def test_say_hello_with_parameter(self):
		hello_world = greet.greet()
		self.assertNotEqual(hello_world.say_hello(), "Hello, Rajendra!")


if __name__ == '__main__':
	unittest.main()
