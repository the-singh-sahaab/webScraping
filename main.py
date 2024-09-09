import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')

def text_file_maker(url, file_id):
    URL = f"{url}"
    page = requests.get(URL)
    complete = []
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("h1", class_="entry-title")
    # complete.append(title.get_text())
    if title is not None:
        complete.append(title.get_text())
        print(title.get_text())
    else:
        complete.append("there is not title.")
        print("there is not title.")
    job_elements = soup.find_all("div", class_="td-post-content tagdiv-type")
    if job_elements is not None:
        for job_element in job_elements:
            complete.append(job_element.get_text())
    with open(f"p15_webscrap\collected_file\{file_id}.txt", 'w', encoding='utf-8') as f:
        # Write each item from the list to a new line in the file
        for item in complete:
            f.write(item + '\n')
    #=============================================================================================================== 
    # try to analysis of the word
    with open(rf"p15_webscrap\collected_file\{file_id}.txt", 'r', encoding='utf-8') as file:
        text = file.read()
    # Tokenization and Preprocessin
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    # Calculate Various Metrics
    positive_score = TextBlob(text).sentiment.polarity
    negative_score = TextBlob(text).sentiment.subjectivity
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (positive_score + negative_score + 0.000001)
    avg_sentence_length = sum(len(word_tokenize(sentence)) for sentence in sentences) / len(sentences)
    percentage_complex_words = (len([word for word in words if len(word) > 2]) / len(words)) * 100
    # Additional Metrics
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = len(words) / len(sentences)
    complex_word_count = len([word for word in words if len(word) > 2])
    word_count = len(words)
    # Calculate syllable per word (a simple approximation)
    syllable_count = sum([len(list(filter(str.isdigit, word))) for word in words]) + \
                    sum([max(1, len(word) - word.lower().count('aeiou')) for word in words])
    syllable_per_word = syllable_count / word_count
    # Personal Pronouns (a simple example)
    personal_pronouns = sum([1 for word in words if word.lower() in ['i', 'me', 'my', 'mine', 'myself']])
    # Avg Word Length
    avg_word_length = sum(len(word) for word in words) / len(words)
    return [avg_word_length, personal_pronouns, syllable_per_word,word_count,complex_word_count ,avg_words_per_sentence,fog_index,percentage_complex_words,avg_sentence_length,subjectivity_score,polarity_score,negative_score ,positive_score]

           
def text_file_maker1(url, file_id):
    URL = f"{url}"
    page = requests.get(URL)
    complete = []
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("h1", class_="tdb-title-text")
    if title is not None:
        complete.append(title.text)
        print(title.text)
    else:
        complete.append("there is not title.")
        print("there is not title.")
    job_elements = soup.find_all("div", class_="tdb-block-inner td-fix-index")
    if job_element is not None:
        for job_element in job_elements:
        # print(job_element.get_text())
            complete.append(job_element.get_text())
    with open(f"p15_webscrap\collected_file\{file_id}.txt", 'w',encoding='utf-8') as f:
        # Write each item from the list to a new line in the file
        for item in complete:
            f.write(item + '\n')        
    # ================================================================================================
    # making the analysis
    with open(rf"p15_webscrap\collected_file\{file_id}.txt", 'r', encoding='utf-8') as file:
        text = file.read()
    # Tokenization and Preprocessin
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    # Calculate Various Metrics
    positive_score = TextBlob(text).sentiment.polarity
    negative_score = TextBlob(text).sentiment.subjectivity
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (positive_score + negative_score + 0.000001)
    avg_sentence_length = sum(len(word_tokenize(sentence)) for sentence in sentences) / len(sentences)
    percentage_complex_words = (len([word for word in words if len(word) > 2]) / len(words)) * 100
    # Additional Metrics
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = len(words) / len(sentences)
    complex_word_count = len([word for word in words if len(word) > 2])
    word_count = len(words)
    # Calculate syllable per word (a simple approximation)
    syllable_count = sum([len(list(filter(str.isdigit, word))) for word in words]) + \
                    sum([max(1, len(word) - word.lower().count('aeiou')) for word in words])
    syllable_per_word = syllable_count / word_count
    # Personal Pronouns (a simple example)
    personal_pronouns = sum([1 for word in words if word.lower() in ['i', 'me', 'my', 'mine', 'myself']])
    # Avg Word Length
    avg_word_length = sum(len(word) for word in words) / len(words)
    return [avg_word_length, personal_pronouns , syllable_per_word,word_count,complex_word_count ,avg_words_per_sentence,fog_index,percentage_complex_words,avg_sentence_length,subjectivity_score,polarity_score,negative_score ,positive_score]
    
 

            
df = pd.read_excel("p15_webscrap\Output Data Structure.xlsx")
for i in range(df.shape[0]):#
    try:
        output = text_file_maker(df["URL"][i], df["URL_ID"][i])
        df["POSITIVE SCORE"][i]= output[-1]
        df["NEGATIVE SCORE"][i]= output[-2]
        df["POLARITY SCORE"][i]= output[-3]
        df["SUBJECTIVITY SCORE"][i]= output[-4]
        df["AVG SENTENCE LENGTH"][i]= output[-5]
        df["PERCENTAGE OF COMPLEX WORDS"][i]= output[-6]
        df["FOG INDEX"][i]= output[-7]
        df["AVG NUMBER OF WORDS PER SENTENCE"][i]= output[-8]
        df["COMPLEX WORD COUNT"][i]= output[-9]
        df["WORD COUNT"][i]= output[-10]
        df["SYLLABLE PER WORD"][i]= output[-11]
        df["PERSONAL PRONOUNS"][i]= output[-12]
        df["AVG WORD LENGTH"][i]= output[-13]
        
        
        
    except AttributeError:
        output = text_file_maker1(df["URL"][i], df["URL_ID"][i])
        df["POSITIVE SCORE"][i]= output[-1]
        df["NEGATIVE SCORE"][i]= output[-2]
        df["POLARITY SCORE"][i]= output[-3]
        df["SUBJECTIVITY SCORE"][i]= output[-4]
        df["AVG SENTENCE LENGTH"][i]= output[-5]
        df["PERCENTAGE OF COMPLEX WORDS"][i]= output[-6]
        df["FOG INDEX"][i]= output[-7]
        df["AVG NUMBER OF WORDS PER SENTENCE"][i]= output[-8]
        df["COMPLEX WORD COUNT"][i]= output[-9]
        df["WORD COUNT"][i]= output[-10]
        df["SYLLABLE PER WORD"][i]= output[-11]
        df["PERSONAL PRONOUNS"][i]= output[-12]
        df["AVG WORD LENGTH"][i]= output[-13]
        
df.to_excel("p15_webscrap\output_new_file.xlsx", index = False)
