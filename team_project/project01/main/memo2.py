import os
DIR_WORD_PATH = '../word/'


reList = os.listdir(DIR_WORD_PATH)
# dirlist = []
# for i in reList:
#     if not '.txt' in i:
#         dirlist+=[i]
# for i in dirlist:
#     for j in os.listdir(DIR_WORD_PATH+i):
#         os.remove(DIR_WORD_PATH+i+'/'+j)
#     os.rmdir(DIR_WORD_PATH+i)
# for i in reList:

print(reList)
double=['ㄲ','ㄸ','ㅃ','ㅆ','ㅉ']
for i in reList:
    for j in double:
        if j in i:
            if os.path.isfile(DIR_WORD_PATH+i):
                os.remove(DIR_WORD_PATH+i)