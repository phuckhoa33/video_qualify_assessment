from better_profanity import profanity    #import better_profanity module
text = "Hello,how are you?"               #Enter text to check
if(profanity.contains_profanity(text)):   #to check if the input text has any swear words.
    print("The text contains profane words")
else:
    print("No text does not contain profane words")