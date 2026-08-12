# AI is useful. AI is powerful.
text=input("enter some text: ")
clean_text=text.strip()
def prepare_text(text):
    lower_text=clean_text.lower()
    processed_text=lower_text.replace(".","")
    processed_text=processed_text.replace("!","")
    processed_text=processed_text.replace("?","")
    processed_text=processed_text.replace(",","")

    return processed_text

processed_text=prepare_text(text)

def word_count(text):
    text=text.split()

    return len(text)

word_count=word_count(text)

def character_count(text):
    return len(clean_text)

character_count=character_count(text)


def frequency(text):
    frequency={}
    words=text.split()
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1

    return frequency

frequency_count=frequency(processed_text)

def longest_word(text):
    words=processed_text.split()
    longest_word=""
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word
    return longest_word

longest_word=longest_word(text)

def sentence_count(text):
    count_fullstop=text.count(".")
    count_exclamation=text.count("!")
    count_question_mark=text.count("?")
    
    return count_fullstop+count_exclamation+count_question_mark

sentence_count=sentence_count(text)

results={
    "character_count":character_count,
    "word_count":word_count,
    "sentence_count":sentence_count,
    "longest_word":longest_word,
    "frequecy_count":frequency_count
}

# print(results)

import json
# json_result=json.dumps(results,indent=4)

# with open("result.json","w") as file:
#     file.write(json_result)

# print("Analysis saved to result.json")

# print(json_result)

# with open("result.json",'r') as file:
#     data=json.load(file)
# print("Saved results:")
# print(data)

try:
    with open("result.json",'r') as file:
        data=json.load(file)
    print(type(data))
except FileNotFoundError:
    print("file not found")
except json.JSONDecodeError:
    print("invalid json")
