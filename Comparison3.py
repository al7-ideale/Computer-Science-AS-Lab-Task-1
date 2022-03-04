#To Compare the number of words in two sentences which are entered by the user and
#display the sentence with less number words and it's word count.

first_sentence = str(input("Enter the first sentence: "))
second_sentence = str(input("Enter the second sentence: "))

if len(first_sentence) < len(second_sentence):
    print("The sentence with less number of words is ",first_sentence,".It consists",len(first_sentence),"words")
else:
    print("The sentence with less number of words is ",second_sentence,".It consists",len(second_sentence),"words")
