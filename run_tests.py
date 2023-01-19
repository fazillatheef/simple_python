import subprocess
import unittest

class test_strlen(unittest.TestCase):
        
    def setUp(self):
        self.proc = subprocess.Popen(["python3", "-m", "strlen"],stdin=subprocess.PIPE
                                      ,stdout=subprocess.PIPE,universal_newlines=True)
    
    def tearDown(self):
        self.proc.stdout.close()
        self.proc.stdin.close()
        while self.proc.returncode is None:
            self.proc.poll()
    
    def test_basic_input(self):
        # First prompt
        expected_output = "Enter a string : "
        output = self.read(expected_output)
        self.assertEqual(expected_output,output)

        # Input
        self.write("python is good\n")

        # Output check
        expected_output = "The string 'python is good' is 14 chars long!"
        output = self.read(expected_output)
        self.assertEqual(expected_output,output)
    
    def test_empty_input(self):
        # First prompt
        expected_output = "Enter a string : "
        output = self.read(expected_output)
        self.assertEqual(expected_output,output)

        # Input
        self.write("\n")

        # Output check
        expected_output = "The string '' is 0 chars long!"
        output = self.read(expected_output)
        self.assertEqual(expected_output,output)    

    def read(self,input):
        return self.proc.stdout.read(len(input))

    def write(self,output):
        self.proc.stdin.write(output)
        self.proc.stdin.flush()

if __name__ == '__main__':
    unittest.main()

