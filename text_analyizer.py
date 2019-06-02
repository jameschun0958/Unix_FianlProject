# coding=UTF-8
""""
#1:分析文本輸出關鍵字(找最出現頻率最高n個關鍵字並給予權重)
#2:分析文本輸出關鍵句(比較每個句子中關鍵字出現頻率，輸出前n項出現最多關鍵字句子維結果)
"""

from bs4 import BeautifulSoup
import urllib.request
import heapq
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from sys import argv



def tokenText(text):
    tokens = [t for t in text.split()]

    clean_tokens = tokens[:]

    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

    return clean_tokens

def freqText(clean_tokens):
    freq = nltk.FreqDist(clean_tokens)

    # for key,val in freq.items():
    # print (str(key) + ':' + str(val))

    #取出出現頻率最高單字
    max_value = float(max(freq.values()))
    #print(max_value)

    # 所有單字頻率為所有單字除以max_value
    for i in list(freq):
        freq[i] /= max_value
        if(freq[i] < 0.1): #刪除頻率小於0.1的單字
            del freq[i]

    #for key, val in freq.items():
    #    print(str(key) + ':' + str(val))

    #freq.plot(20, cumulative=False)

    return freq

def ranking(sentence, freq, n):
    rank=[0]*len(sentence)

    for i in range(0,len(sentence)):
         for key in freq:
            if(key in sentence[i]):
                rank[i]+=freq[key]

    max_list = heapq.nlargest(n,rank) #取出前n筆關鍵句子

    for i in range(0,len(max_list)):
        print(i+1,". ",sentence[rank.index(rank[i])])

    #print(len(rank),rank)


def splitSentence(text):
    sen_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    sentences = sen_tokenizer.tokenize(text)

    #print(sentences)

    return sentences


if __name__=="__main__":

    """
    response = urllib.request.urlopen('http://php.net/')
    html = response.read()
    soup = BeautifulSoup(html,"html5lib")
    text = soup.get_text(strip=True)
    """
    n = 3

    filename = argv[1]

    if(len(argv) > 2):
        if(argv[2].isnumeric()):
            n = int(argv[2])

    text = open(filename,'r').read()

    freq = freqText(tokenText(text)[:])

    sentence = splitSentence(text).copy()

    ranking(sentence, freq,n)


