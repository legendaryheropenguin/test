import time
import pandas as pd
import os
import openpyxl
import random
import multiprocessing


DIR_WORD = '../word/'
DIRC_EXCEL = './rank.xlsx'

def givechosung(): # ex) 랜덤으로 ㅇㄹ.txt 추출
    question = random.choice(os.listdir(DIR_WORD))
    print(question)

# 랜덤 단어에서 초성 분리
def getchosung(word):
    """Return chosung as a string from a two letters word"""
    if isinstance(word, str):
        chosung = ''
        for w in word:
            chosung += chr(((ord(w) - 44032) // 588) + 4352)
        return chosung

print(givechosung())