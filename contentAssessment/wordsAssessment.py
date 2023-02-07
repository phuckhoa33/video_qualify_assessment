from better_profanity import profanity 

def validate_swear_words(file_validation):
    file = open(file_validation)
    video_content = file.readlines()
    print(video_content)
    checkable = profanity.contains_profanity(video_content)
    return checkable
validate_swear_words("contentAssessment/readContent/recognized.txt")