import pandas as pd

file = pd.read_csv('abusive_words.csv')
critical_index = file.sum(axis = 0, skipna = True)

file.dropna(inplace = True)
sub ='joint'

file["Indexes"]= file["words"].str.find(sub)


voice_text_file = open('final_speech_to_text.txt','r')

file_string = [(line.strip()).split() for line in voice_text_file]

i=len(file_string[0])-1
while i>=0:




print(list_of_lists)