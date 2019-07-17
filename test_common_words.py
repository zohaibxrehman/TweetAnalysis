"""A3. Tester for the function common_words in tweets.
"""

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    """Tester for the function common_words in tweets.
    """

    def test_empty(self):
        """Empty dictionary."""

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    
    def test_one_word_limit_zero(self):
        """Dictionary with one word"""
        
        arg1 = {'hello': 2}
        arg2 = 0
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
        
    def test_one_word_limit_two(self):
        """Dictionary with one word"""
        
        arg1 = {'hello': 2}
        arg2 = 2
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)      
     
     
    def test_multi_word_limit_zero(self): 
        """Dictionary with multiple words"""
        
        arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        arg2 = 0
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        
    def test_multi_word_limit_one(self): 
        """Dictionary with multiple words"""
        
        arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        arg2 = 1
        exp_arg1 = {'a': 6}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        
    def test_multi_word_limit_two(self): 
        """Dictionary with multiple words"""
        
        arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        arg2 = 2
        exp_arg1 = {'a': 6}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        
    def test_multi_word_limit_three(self): 
        """Dictionary with multiple words"""
        
        arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        arg2 = 3
        exp_arg1 = {'a': 6, 'b': 5, 'c': 5}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        
    def test_multi_word_limit_four(self): 
        """Dictionary with multiple words"""
        
        arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        arg2 = 4
        exp_arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        
    def test_multi_word_limit_five(self): 
        """Dictionary with multiple words"""
        
        arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        arg2 = 5
        exp_arg1 = {'a': 6, 'b': 5, 'c': 5, 'd': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        
        
    def test_all_duplicates_value(self):
        """Dictionary with only duplicates"""
        
        arg1 = {'a': 5, 'b': 5, 'c': 5}
        arg2 = 3
        exp_arg1 = {'a': 5, 'b': 5, 'c': 5}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg) 
    
    def test_all_duplicates_one(self):
        """Dictionary with only duplicates"""
        
        arg1 = {'a': 5, 'b': 5, 'c': 5}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)     
    
if __name__ == '__main__':
    unittest.main(exit=False)
