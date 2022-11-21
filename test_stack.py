import unittest
from stack import Stack

class TestStack(unittest.TestCase):
  
  def setUp(self):
    self.stack = Stack()
  
  def testEmptyStack(self):
    self.assertEquals(True,self.stack.is_empty())

  def testNotEmptyStack(self):
    self.stack.push(10)
    self.assertEquals(False,self.stack.is_empty())

  def testSizeStack(self):
    self.stack.push(10)
    self.stack.push(20)
    self.stack.push(30)
    self.assertEquals(3,self.stack.size)

  def testPushPopStack(self):
    self.stack.push(10)
    self.stack.push(20)
    self.stack.push(30)
    result = self.stack.pop()
    result = self.stack.pop()
    self.assertEquals(20,result)
    

  def testEmptyStackException(self):
    self.assertRaises(TypeError, self.stack.pop, "Stack is empty :(")