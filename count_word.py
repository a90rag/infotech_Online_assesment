import re 

def count_word(input_word):
    input_word = re.sub(r'[^\w\s]', '', input_word)
    word=input_word.split()
    word_dict={}
    for i in word:
        if i in word_dict:
            word_dict[i]+=1
        else:
            word_dict[i]=1
            
    return word_dict 

input_word = "Hello, World! This is hellow World"

print(count_word(input_word))