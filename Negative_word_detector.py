import pandas as pd

file = pd.read_csv('abusive_words.csv')
critical_index = 0

voice_text_file = open('final_speech_to_text.txt','r')

file_string = [(line.strip()).split() for line in voice_text_file]

i=len(file_string[0])-1
while i>=0:
    sub = file_string[0][i]
    index = file[file['words']==sub].index.values
    critical_index+=file._get_value(index[0],'N_index')

    i-=1

print(critical_index)