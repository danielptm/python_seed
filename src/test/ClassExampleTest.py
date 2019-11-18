import unittest
from example.ClassExample import ClassExample


class ClassExampleTest(unittest.TestCase):

    def testHelloWorld(self):
        hello = ClassExample()
        self.assertEqual("Hello World!", hello.helloWorld())


if __name__ == '__main__':
    unittest.main()
