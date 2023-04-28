def open_pos(word):
    cnt=0
    with open('./NTUSD_traditional/NTUSD_positive_unicode.txt', 'r', encoding='utf-8') as f:
        for line in f:
            #去除空白
            line=line.strip()
            if word == line:
                cnt += 1
                print("word:", word)
                print("pos_line:", line)
                break;
    return cnt
            
def open_neg(word):
    cnt=0
    with open('./NTUSD_traditional/NTUSD_negative_unicode.txt', 'r', encoding='utf-8') as f:
        for line in f:
            #去除空白
            line=line.strip()
            if word == line:
                cnt -= 1
                print("word:", word)
                print("neg_line:", line)
                break;
            
    return cnt