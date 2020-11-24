import pandas as pd

file = pd.read_csv('abusive_words.csv')
critical_index = file.sum(axis = 0, skipna = True)

file.dropna(inplace = True)
sub ='joint'

file["Indexes"]= file["words"].str.find(sub)


voice_text_file = open('final_speech_to_text.txt','r')
# while()
print(file)

