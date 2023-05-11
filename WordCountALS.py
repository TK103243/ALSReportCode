txt_name = "Proj_T1_Report.txt"
with open(txt_name,"r",encoding="UTF-8") as fh:
    txt_1 = fh.read()
    find_1 = txt_1.index('The usage')
    
    txt_2 = txt_1[int(find_1):len(txt_1)]
    find_2 = txt_2.index('References')
    
    txt_3 = txt_2[:int(find_2)]
    find_3 = txt_3.index('Max height')
    
    find_4 = txt_3.index('Discussion')
    txt_4a = txt_3[:int(find_3)]
    txt_4b = txt_3[int(find_4):]
    txt_4 = txt_4a + " " + txt_4b
    
    find_5 = txt_4.index('The initial velocity')
    find_6 = txt_4.index('(t1)')
    txt_5a = txt_4[:int(find_5)]
    txt_5b = txt_4[int(find_6):]
    txt_5 = txt_5a + " " + txt_5b
    
    find_7 = txt_5.index('(t1)')
    find_8 = txt_5.index('Gravitational')
    txt_6a = txt_5[:int(find_7)]
    txt_6b = txt_5[int(find_8):]
    txt_6 = txt_6a + " " + txt_6b
    
    txt_6 = txt_6.replace('F i g u r e'or'Table','')
    
    word_count = len(txt_6.split())
    print(txt_6)
    print(word_count)
