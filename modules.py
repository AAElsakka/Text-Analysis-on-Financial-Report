import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from nltk import word_tokenize

import time


def clean_sentencs(sentence, stopwords):
    """This Function is used to clean the html to get text"""
    words = str(sentence).lower()
    words = word_tokenize(words)
    words = [w for w in words if not w in stopwords]
    words = [w for w in words if w.isalpha()]
    
    return words

def calculate_score(word_list, text, score_name, variables):
    """This Function counts the occurance of words in text"""
    score = 0
    for word in text:
        if word in word_list:
            score += 1
        else:
            pass
    variables[score_name] = score
    return score

def polarity(positive, negative, variables):
    """this function calculates the polarity score"""
    polarity_score = (positive - negative)/(positive + negative + 0.000001)
    variables['polarity_score'] = polarity_score
    return polarity_score

def syllable_count(word):
    """This Function counts the syllables of words"""
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    for index in range(0, len(word)):
        if word[index] in vowels:
            count += 1
    if word.endswith(("e",'es','ed')):
        count -= 1
    if count == 0:
        count += 1
    return count

def complex_words(word_list, variables):
    """This function calculates the complex words score and percentage in report"""
    count = 0
    for word in word_list:
        if syllable_count(word) > 2:
            count+=1
    percentage_of_complex_words = count / len (word_list)
    variables['percentage_of_complex_words'] = percentage_of_complex_words
    variables['complex_word_count'] = count
    return percentage_of_complex_words

def fog(variables):
    """This Function calculates the fog score"""
    avg_len = variables['average_sentence_length']
    cmplx_wrds = variables['percentage_of_complex_words']
    fog_index = 0.4 * (avg_len + cmplx_wrds)
    variables['fog_index'] = fog_index
    return fog_index 

def word_proportion(prop_score, text, score_name, variables):
    #get proportion of words
    proportion = variables[score_name] / len(text)
    variables[prop_score] = proportion
    return proportion