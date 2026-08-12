text=input("enter some text: ")
def analyze_text(text):
    clean_text=text.strip()
    lower_text=clean_text.lower()
    processed_text=lower_text.replace(".","")
    processed_text=processed_text.replace("!","")
    processed_text=processed_text.replace("?","")
    processed_text=processed_text.replace(",","")
    words=processed_text.split()
    frequency={}
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    longest_word=""
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word
    count_fullstop=text.count(".")
    count_exclamation=text.count("!")
    count_question_mark=text.count("?")
    character_count=len(text)
    word_count=len(words)
    sentence_count=count_question_mark+count_exclamation+count_fullstop
    frequency_count=frequency
    results={
    "character_count":character_count,
    "word_count":word_count,
    "sentence_count":sentence_count,
    "longest_word":longest_word,
    "frequecy_count":frequency_count
}
    return results
print(analyze_text(text))
# Text Analyzer