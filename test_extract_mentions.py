"""A3. Tester for the function extract_mentions in tweets.
"""

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    """Tester for the function extract_mentions in tweets.
    """

    def test_empty(self):
        """Empty tweet."""

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        """Non-empty tweet with no mentions."""

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    
    def test_nonempty_one_mention_lower(self):
        """Non-empty tweet with one mention in the lower case"""
        
        arg = 'Hi @elonmusk'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_nonempty_one_mention_upper(self):
        """Non-empty tweet with one mention in the upper case"""
        
        arg = 'Hi @ELONMUSK'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    
    def test_nonempty_mixed_case(self):
        """Non-empty tweet with one mention in the mixed case"""
        
        arg = 'Hi @ElonMusk'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_multiple_mention_no_dup(self):
        """Non-empty tweet with multiple mentions of the same case."""
        
        arg = 'Hi @elonMusk @zohaib'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk', 'zohaib']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_multiple_mention_no_dup_diff_case(self):
        """Non-empty tweet with multiple mentions of the different cases."""
        
        arg = 'Hi @elonMusk @ZOHAIB'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk', 'zohaib']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
    
    
    def test_multiple_mention_dup_same_case(self):
        """Non-empty tweet with the multiple mentions which are duplicates
        and have the same case."""
        
        arg = 'Hi @elonmusk @elonmusk'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk', 'elonmusk']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
    
    
    def test_multiple_mention_dup_diff_case(self):
        """Non-empty tweet with multiple mentions which are duplicates and have
        different case."""
        arg = 'Hi @elonmusk @ELONMUSK'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk', 'elonmusk']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
        
    def test_order_of_mention_symbol(self):
        """Non-empty tweet with the mention in between the word."""
        
        arg = 'a@b'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)     
    
    
    def test_special_character_beg(self):
        """Non-empty tweet with special character in the beginning of 
        mention."""
        
        arg = 'Hi @!elonmusk'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
        
    def test_special_character_end(self):
        """Non-empty tweet with special character at the end of mention."""
        
        arg = 'Hi @elonmusk!'
        actual = tweets.extract_mentions(arg)
        expected = ['elonmusk']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_special_characater_between(self):
        """Non-empty tweet with special character in between the mention."""
        
        arg = "Hi @elon!musk"
        actual = tweets.extract_mentions(arg)
        expected = ['elon']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        


    def test_alpha_num(self):
        """Non-empty tweet with mentions with different cobinations of alphabets
        and numbers"""
        
        arg = "Hi @elon123 @123elon @123"
        actual = tweets.extract_mentions(arg)
        expected = ['elon123', '123elon', '123']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
    

if __name__ == '__main__':
    unittest.main(exit=False)
