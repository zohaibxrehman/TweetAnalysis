"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def first_alnum_substring(text: str) -> str:
    """Return all alphanumeric characters in text from the beginning up to the
    first non-alphanumeric character, or, if text does not contain any
    non-alphanumeric characters, up to the end of text."

    >>> first_alnum_substring('')
    ''
    >>> first_alnum_substring('IamIamIam')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!andMore')
    'iamiamiam'
    >>> first_alnum_substring('$$$money')
    ''
    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'
    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word

        
def extract_least_frequent(d: Dict[str, int]) -> Dict[str, int]:
    """Return a dictionary with only those keys from d that are of the lowest
    frequenct.
    
    >>> extract_least_frequent({'a': 6, 'b': 5, 'c': 5, 'd': 3})
    {'d': 3}
    >>> extract_least_frequent({'a': 6, 'b': 5, 'c': 5})
    {'b': 5, 'c': 5}
    """
    least_frequent = {}
    values = []
    for key in d:
        values.append(d[key])
        
    smallest = values[0]
    for value in values:
        if value < smallest:
            smallest = value
            
    for word in d:
        if d[word] == smallest:
            least_frequent[word] = smallest
    return least_frequent

def extract_all_hashtags(tweet_dict: Dict[str, List[tuple]], user: str) -> List[str]:
    """Return a list which contains all the hashtags a user has used.
    
    >>> file = open('tweets_small.txt', 'r')
    >>> d = read_tweets(file)
    >>> 
    """
    all_hashtags = []
    for tweet in tweet_dict[user.lower()]:
        all_hashtags.extend(extract_hashtags(tweet[TWEET_TEXT_INDEX]))
    return all_hashtags
        
# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    """
    
    mentions_list = []
    for word in text.split():
        if word[0] == MENTION_SYMBOL and word[1].isalnum():
            mentions_list.append(first_alnum_substring(word[1:].lower()))
    return mentions_list


def extract_hashtags(text: str) -> List[str]:
    """Return a list containing all of the unique hashtags in text, in the order
    they appear in the text, converted to lowercase.
    
    >>> extract_hashtags("#UofT is a university in #Toronto")
    ['uoft', 'toronto']
    >>> extract_hashtags("#UofT #uoft #UOFT! @zohaib")
    ['uoft']
    >>> extract_hashtags("#1 #Game2 #2game #csc108")
    ['1', 'game2', '2game', 'csc108']
    """
    
    hashtags_list = []
    for word in text.split():
        if word[0] == HASH_SYMBOL and word[1].isalnum() \
           and first_alnum_substring(word[1:].lower()) not in hashtags_list:
            hashtags_list.append(first_alnum_substring(word[1:].lower()))
    return hashtags_list


def count_words(text: str, word_to_count: Dict[str, int]) -> None:
    """Update the count of words in the dictionary word_to_count in accordance
    with the number of times it appears in the text or add the word in the 
    word_to_count if it isn't already in it; Hashtags, mentions, and URLs are
    not considered words.
    
    >>> d = {'is': 1}
    >>> count_words("#UofT Toastmaster is holding elections!", d)
    >>> d
    {'is': 2, 'toastmaster': 1, 'holding': 1, 'elections': 1}
    
    """
    
    for word in text.split():
        if not (word[0] == MENTION_SYMBOL or word[0] == HASH_SYMBOL or \
                word[0:3] == URL_START):
            if clean_word(word.lower()) in word_to_count:
                word_to_count[clean_word(word.lower())] += 1
            else:
                word_to_count[clean_word(word.lower())] = 1


def common_words(word_to_count: Dict[str, int], n: int) -> None:
    """Update the dictionary word_to_count so that it only contains at most
    n words that appear with the highest frequency; none of the words with a
    particular frequncy will be included if resultant dictionary would have more
    than n words.
    
    Precondition: n >= 0
    
    >>> t = {'a': 6, 'b': 5, 'c': 4, 'd': 3}
    >>> common_words(t, 3)
    >>> t
    {'a': 6, 'b': 5, 'c': 4}
    >>> tw = {'a': 6, 'b': 5, 'c': 5, 'd': 3}
    >>> common_words(tw, 2)
    >>> tw
    """
    
    while len(word_to_count) > n:
        least_frequent_word_to_count = extract_least_frequent(word_to_count)
        for word in least_frequent_word_to_count:
                word_to_count.pop(word)


def read_tweets(file: TextIO) -> Dict[str, List[tuple]]:
    """Return a dictionary with the usernames from the file as key of the 
    dictionary and list of tuples as the value of the dictionary with each tuple 
    taking information of tweets of the user.
    """
    tweet_dic = {}
    line = file.readline()
    while line != '':
        tweet_list = []
        username = line[:-2].lower()
        line = file.readline()
        while line != '' and line[-2] != ':':
            info = line[:-1].split(',')
            date = int(info[FILE_DATE_INDEX])
            source = info[FILE_SOURCE_INDEX]
            fav_count = int(info[FILE_FAVOURITE_INDEX])
            retweet_count = int(info[FILE_RETWEET_INDEX])   
            line = file.readline()
            tweet_text = ''
            while line != '<<<EOT\n':                      
                tweet_text += line
                line = file.readline()
            line = file.readline()
            tweet_list.append((tweet_text.strip(), date, source, fav_count, 
                               retweet_count)) 
        tweet_dic[username] = tweet_list
    return tweet_dic
                

def most_popular(tweet_dict: Dict[str, List[tuple]], start_date: int,
                 end_date: int) -> str:
    """Return the user from tweet_dict who was the most popular between 
    start_date and end_date.
    
    >>> file = open('tweets_small.txt', 'r')
    >>> d = read_tweets(file)
    >>> most_popular(d, 20181107000000, 20181109000000)
    'uoftcompsci
    >>> most_popular(d, 20181103000000, 20181104000000)
    'uoftartsci'
    """
    
    popular_sum = 0
    popular_user = ''
    tie = False
    for key in tweet_dict:
        for element in tweet_dict[key]:
            date = element[TWEET_DATE_INDEX]
            if start_date <= date <= end_date:                
                count_sum = element[TWEET_FAVOURITE_INDEX] + \
                    element[TWEET_RETWEET_INDEX]
                if count_sum > popular_sum:
                    popular_user = key
                    popular_sum = count_sum
                    tie = False
                elif count_sum == popular_sum:
                    tie = True
    if popular_user == '' or tie:
        return 'tie'
    else:
        return popular_user


def detect_author(tweet_dict: Dict[str, List[tuple]], tweet: str) -> str:
    """Return the username of the most likely author of that tweet based on the
    the hashtags they use; if all hashtags in the tweet are uniquely used by a 
    single user, then return that user's username; otherwise, return the string
    'unknown'
    
    >>> file = open('tweets_small.txt', 'r')
    >>> d = read_tweets(file)
    >>> detect_author(d, "#startai")
    'uoftcompsci'
    >>> detect_author(d, "#startai #uoftalumni")
    'uoftcompsci'
    """
    tweet_hash = extract_hashtags(tweet)
    author = ''
    for key in tweet_dict:
        all_hash = extract_all_hashtags(tweet_dict, key)
        unique = True
        for hash in tweet_hash:
            if hash not in all_hash:
                unique = False
        if unique and author != '':
            return 'unknown'
        if unique:
            author = key
    if author == '':
        return 'unknown'
    else:
        return author.lower()
    
    
if __name__ == '__main__':
    # import doctest
    # doctest.testmod()