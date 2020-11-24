import pandas as pd

file = pd.read_csv('abusive_words.csv')
critical_index = 0

file.dropna(inplace = True)




voice_text_file = open('final_speech_to_text.txt','r')

file_string = [(line.strip()).split() for line in voice_text_file]

i=len(file_string[0])-1
while i>=0:
    sub = file_string[0][i]
    critical_index = file["words"].str.find(sub)

    # file["Indexes"]= file["words"].str.find(sub)



print()