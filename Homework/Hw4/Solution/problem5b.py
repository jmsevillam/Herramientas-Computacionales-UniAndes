def decode(word1,word2):
    word=''
    for i in range(len(word1)):
        word+=word1[i]+word2[i]
    return word

Alice='Ti rga eoe  esg o h ore"ermetsCmuainls'
Bob='hspormdcdsamsaefrtecus Hraina optcoae"'

print(decode(Alice,Bob))
