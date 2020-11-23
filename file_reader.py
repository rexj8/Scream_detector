file = open('speech_text.txt', 'r')

sq_brckt=''
waste=""
while 1:
    char = file.read(1)
    if not char:
        break

    if char==']':
        sq_brckt=']'
        waste=str(sq_brckt)

    if sq_brckt==']':
        waste = waste+char

final_str=waste[16:-4]

text_file = open('final_speech_to_text.txt', 'w+')
text_file.write(final_str)