import unittest
from src.utils.argparser import *


class ArgparserTest(unittest.TestCase):
    
    def test_parse_arguments_success(self):
        # Define test data
        arguments_i = ['-i', 'file.pdf', '-o', 'file.epub']
        
        self.assertEquals(parse_arguments(arguments_i), argparse.Namespace(
            input_file='file.pdf', output_file='file.epub', verbose=False))
        
    def test_parse_arguments_empty_input(self):
        arguments_i = ['-i', '-o', 'file.epub']
        
        with self.assertRaises(SystemExit):
            parse_arguments(arguments_i)
            
    def test_parse_arguments_empty_output(self):
        arguments_i = ['-i', 'file.pdf', '-o']
        
        with self.assertRaises(SystemExit):
            parse_arguments(arguments_i)
            
    def test_parse_arguments_no_i_argument(self):
        arguments_i = ['file.pdf', '-o', 'file.epub']
        
        with self.assertRaises(SystemExit):
            parse_arguments(arguments_i)
            
    def test_parse_arguments_no_o_argument(self):
        arguments_i = ['i', 'file.pdf', 'file.epub']
        
        with self.assertRaises(SystemExit):
            parse_arguments(arguments_i)
            
    def test_parse_arguments_unknown_arg(self):
        arguments_i = ['i', 'file.pdf', '-f', 'file.epub']
        
        with self.assertRaises(SystemExit):
            parse_arguments(arguments_i)
    
    def test_parse_arguments_upper_v(self):
        arguments_i = ['i', 'file.pdf', '-o', 'file.epub', '-V']
        
        with self.assertRaises(SystemExit):
            parse_arguments(arguments_i)