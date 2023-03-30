def open_pos(word):
    pos=0
    neu=0
    with open('./NTUSD_traditional/NTUSD_positive_unicode.txt', 'r', encoding='utf-8') as f:
        for line in f:
            #去除空白
            line=line.strip()
            if word in line:
                pos += 1
                #print("word:", word)
                #print("pos_line:", line)
                break;
            else:
               neu+=1
    return pos
            
def open_neg(word):
    neg=0
    neu=0
    with open('./NTUSD_traditional/NTUSD_negative_unicode.txt', 'r', encoding='utf-8') as f:
        for line in f:
            #去除空白
            line=line.strip()
            if word in line:
                neg+=1
                #print("word:", word)
                #print("neg_line:", line)
                break;
            else:
                neu+=1
    return neg