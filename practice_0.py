# text = input("Enter some text: ")
# print("You entered:")
# print(text)

# text = input("Enter some text: ")
# print(f"Your text is: {text}")
# print("Text received successfully! ")

# text = input("Enter some text: ")
# print(f"character_count: {len(text)}")

# text = input("Enter some text: ")
# words = text.split()
# print(f"word_count: {len(words)}")

# text = input("Enter some text: ")
# if text=="":
#     print("error: please enter some text")
# else:
#     words=text.split()
#     print(f"character_count: {len(text)}")
#     print(f"word_count: {len(words)}")

# text = input("Enter some text: ")
# clean_text = text.strip() 
# print(f"original_text: {text}")
# print(f"cleaned_text: {clean_text}")

# text = input("Enter some text: ")
# fullstop_count=text.count(".")
# question_mark_count=text.count("?")
# exclamation_count=text.count("!")
# sentence_count=fullstop_count+question_mark_count+exclamation_count
# print(f"sentence_count: {sentence_count}")

# text = input("Enter some text: ")
# longest_word=""
# words=text.split()
# for word in words:
#     if len(word) > len(longest_word):
#        longest_word=word
# print(f"longest_word: {longest_word}")

# text = input("Enter some text: ")
# words = text.split()
# frequencies_word = {}
# for word in words:
#     if word in frequencies_word:
#         frequencies_word[word]=frequencies_word[word]+1
#     else:
#         frequencies_word[word]=1
# print(f"frequencies_word: {frequencies_word}")

# text = input("Enter some text: ")
# normalised_text=text.lower()
# words = normalised_text.split()
# frequencies_word = {}
# for word in words:
#     if word in frequencies_word:
#         frequencies_word[word]=frequencies_word[word]+1
#     else:
#         frequencies_word[word]=1
# print(f"frequencies_word: {frequencies_word}")

# text = input("Enter some text: ")
# processed_text=text.replace(".","")
# processed_text=processed_text.replace("?","")
# processed_text=processed_text.replace("!","")
# processed_text=processed_text.replace(",","")
# normalised_text=processed_text.lower()
# words = normalised_text.split()
# frequencies_word = {}
# for word in words:
#     if word in frequencies_word:
#         frequencies_word[word]=frequencies_word[word]+1
#     else:
#         frequencies_word[word]=1
# print(f"frequencies_word: {frequencies_word}")

# text = input("Enter some text: ")
# clean_text=text.strip()
# def prepare_text(text):
#     normalise_text=text.lower()
#     processed_text=normalise_text.replace(".","")
#     processed_text=processed_text.replace("!","")
#     processed_text=processed_text.replace("?","")
#     processed_text=processed_text.replace(",","")

#     return processed_text
# processed_text=prepare_text(clean_text)
# print(processed_text)

