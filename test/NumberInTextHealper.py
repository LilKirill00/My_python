S1 = 'if ui_main.checkBox_'
S2 = ".isChecked():\nif ui_main.textbox_video_"
S3 = ".text() != '':\nif ui_main.textbox_name_"
S4 = ".text() != '':\nget_transcript_subtitle(ui_main.textbox_video_"
S5 = '.text(), ui_main.textbox_name_'
S6 = '.text())\n\t\telse:\nget_transcript_subtitle(ui_main.textbox_video_'
S7 = '.text(), "file'
S8 = '")'

i = 1
while i <= 24:
    # print(S1 + str(i) + S2 + str(i) + S3 + str(i) + S4 + str(i) + S5)
    # print(S1 + str(i) + S2 + str(i) + S3)
    print(S1 + str(i) + S2 + str(i) + S3 + str(i) + S4 + str(i) + S5 + str(i) + S6 + str(i) + S7 + str(i) + S8)
    i = i+1

j = 1
while j <= 24:
    with open("res/file"+str(j)+".csv", 'w') as file:
        file.close()
    j = j+1
