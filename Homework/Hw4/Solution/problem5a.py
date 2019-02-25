def decode(word1,word2,code):
    if len(word1)==1:
        code+=word1+word2
        return code
    else:
        code+=word1[0]+word2[0]
        return decode(word1[1:],word2[1:],code)

Alice='Ti rga eoe  esg o h ore"ermetsCmuainls'
Bob='hspormdcdsamsaefrtecus Hraina optcoae"'
    
print(decode(Alice,Bob,''))
