#!/bin/python3
import subprocess
import unittest

class test_strlen(unittest.TestCase):
        
    def setUp(self):
        self.proc = subprocess.Popen(["./src/strlen.py"],stdin=subprocess.PIPE
                                      ,stdout=subprocess.PIPE,universal_newlines=True)
    
    def tearDown(self):
        self.proc.stdout.close()
        self.proc.stdin.close()
        # Wait until the process ends
        while self.proc.returncode is None:
            self.proc.poll()
    
    # Test cases
    # Test case 1
    def test_basic_input(self):
        # First prompt
        self.check_output("Enter a string : ")

        # Input
        self.write("python is good\n")

        # Output check
        self.check_output("The string 'python is good' is 14 chars long!")
    
    # Test case 2
    def test_empty_input(self):
        # First prompt
        self.check_output("Enter a string : ")

        # Input
        self.write("\n")

        # Output check
        self.check_output("The string '' is 0 chars long!")

    def read(self,input):
        return self.proc.stdout.read(len(input))

    def check_output(self,expected_output):
        output = self.read(expected_output)
        self.assertEqual(expected_output,output)
    
    def write(self,output):
        self.proc.stdin.write(output)
        self.proc.stdin.flush()

if __name__ == '__main__':
    unittest.main()

