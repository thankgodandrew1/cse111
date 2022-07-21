from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)
        
        # convert the list of words to lower case letter because twas cappitalized in the main program
        word = word.lower()
        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # convert the list of words to lower case letter because twas cappitalized in the main program
        word = word.lower()

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    #To test the single nouns

    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    # This loop will repeat the statements inside it 5 times.
    
    for _ in range(5):

        # Call the get_noun function which
        # should return a singular noun.
        noun = get_noun(1)

        # convert the list of words to lower case letter because twas cappitalized in the main program
        noun = noun.lower()

        # Verify that the noun returned from get_noun
        # is one of the words in the singular_noun list.
        assert noun in single_nouns

   
    #To test the plural 
    plural_noun =  ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    #This loop repeats the statement 5 times

    for _ in range(5):

        # Call the get_nouns function which
        # should return a plural noun.
        noun = get_noun(2)
        
        # convert the list of words to lower case letter because twas cappitalized in the main program
        noun = noun.lower()
        # Verify that the noun returned from get_noun
        # is one of the words in the plural_noun list.
        assert noun in plural_noun



def test_get_verb():
    #To test the past singular
    single_past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    #This loops repeats the statement 4 times
    for _ in range(4):
        
        # Call the get_verb function which
        # should return a singular past verb.
        verb = get_verb(1, 'past')

        # convert the list of words to lower case letter because twas cappitalized in the main program
        verb = verb.lower()

        # Verify that the noun returned from get_verb
        # is one of the words in the single_past_verb list.
        assert verb in single_past_verb 

    #To test the past plural verb
    plural_past_tense = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    #This loops repeats the statement 4 times
    for _ in range(4):
        
        # Call the get_verb function which
        # should return a plural past verb.
        verb = get_verb(2, 'past')

        # convert the list of words to lower case letter because twas cappitalized in the main program
        verb = verb.lower()

        # Verify that the verb returned from get_noun
        # is one of the words in the plural past tense list.
        assert verb in plural_past_tense 

    #To test singular present tense
    singular_present_tense = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

      #This loops repeats the statement 4 times
    for _ in range(4):
        
        # Call the get_verb function which
        # should return a singular present verb.
        verb = get_verb(1, 'present')

        # convert the list of words to lower case letter because twas cappitalized in the main program
        verb = verb.lower()

        # Verify that the verb returned from get_verb
        # is one of the words in the singular present tense list.
        assert verb in singular_present_tense

    #To test plural present tense

    plural_present_tense = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    #This loops repeats the statement 4 times
    for _ in range(4):
        
        # Call the get_verb function which
        # should return a singular present tense verb.
        verb = get_verb(2, 'present')

        # convert the list of words to lower case letter because twas cappitalized in the main program
        verb = verb.lower()

        # Verify that the verb returned from get_verb
        # is one of the words in the plural_present tense list.
        assert verb in plural_present_tense

    #TO TEST SINGULAR FUTURE TENSE
    singular_future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
 
    #This loops repeats the statement 4 times
    for _ in range(4):
        
        # Call the get_verb function which
        # should return a singular future tense verb.
        verb = get_verb(1, 'future')

        # convert the list of words to lower case letter because twas cappitalized in the main program
        verb = verb.lower()

        # Verify that the verb returned from get_noun
        # is one of the words in the singular future tense list.
        assert verb in singular_future_tense

    #TO TEST plural FUTURE TENSE
    plural_future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
 
    #This loops repeats the statement 4 times
    for _ in range(4):
        
        # Call the get_verb function which
        # should return a plural future tense verb.
        verb = get_verb(2, 'future')

        # convert the list of words to lower case letter because twas cappitalized in the main program
        verb = verb.lower()

        # Verify that the verb returned from get_verb
        # is one of the words in the plural_futer_tense list
        assert verb in plural_future_tense

def test_get_preposition():
    #To test the statements in the prepositional list
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    # This repeats the statememnt 4 times
    for _ in range(4):
        
        # Calls the prepositional function
        preposition = get_preposition()

        # convert the list of words to lower case letter because twas cappitalized in the main program
        preposition = preposition.lower()
     
        # Verify that the preposition returned from get_preposition
        # is one of the words in the prepositions
        assert preposition in prepositions


def test_get_prepositional_phrase():
    # This partof the program calls the get_prepositional_phrase function
    prepositional_phrase = get_prepositional_phrase(1).split()
    assert prepositional_phrase

def test_get_adjective():
    # To test the statements in the get_adjectivelist
    adjectives = ['happy', 'bad', 'amazed', 'responsible', 'sorry', 'free', 'made', 'interested', 'slow', 'proud', 
       'fed up', 'ok', 'dissapointed', 'certain', 'involved']

    # This repeats the statememnt 4 times
    for _ in range(4):
        
        # Calls the adjective function
        adjective = get_adjective()

        # convert the list of words to lower case letter because twas cappitalized in the main program
        adjective = adjective.lower()
     
        # Verify that the adjectives returned from get_adjective
        # is one of the words in the adjectives
        assert adjective in adjectives
    
  
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
