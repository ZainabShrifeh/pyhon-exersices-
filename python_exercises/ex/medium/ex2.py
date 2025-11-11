def text_analysis(text):
    dic={}
    string=""
    for i in text :
        if i == " " :
            string = string.lower()
            if string in dic:
                dic[string]+=1

            if string not in dic:
                dic[string]=dic.get(string,0)+1
            string=""
        else:
            string+=i
    if string:
        string = string.lower()
        dic[string] = dic.get(string, 0) + 1
    return dic

text = "the AI is ossa , the ai folla"
dic = text_analysis(text)
for i in dic:
    print(f'{i}:{dic[i]}')

#done