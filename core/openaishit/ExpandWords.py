import os

from dotenv import load_dotenv
from openai import OpenAI

from GenerateImage import generateImage

load_dotenv()

'''
to use, import expandWord and expandWordList from ExpandWords.py

expandWord(word, category):
    word - a string of a word
    category - a string of a category
    returns - a string of the expanded word in the format Word: {'word'} Category: {'category'}

OR to do multiple words at once

expandWordList(words, categories):
    words - a string of words seperated by commas eg - chicken, water, beer, bread
    categories - a string of categories seperated by commas
    returns - a string of expanded words in the format Word: {'word'} Category: {'category'}, Word: {'word'} Category: {'category'}
'''

def getClient():
    return OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

def getContextOne():
    context = "You will be given a word and a category in the format Word: {'word'} Category: {'category'}. "
    context += "For example - Word: {'chicken'} Category: {'animal'}. "
    context += "Expand the given word into a descriptive phrase, making sure to keep the category in context. "
    context += "For example, water -> a glass of water, beer -> a mug of beer, bread -> a loaf of bread. "
    context += "If the category is not provided (NONE), assume the category is 'thing'. "
    context += "Some words will not need to be changed, such as shirt or clown. "
    context += "Do not overcomplicate the phrase. "
    context += "Do not add unnecessary details. "
    context += "Do not add ajdectives or adverbs. "
    context += "Do not change the plurality of the word. "
    context += "Only return the expanded text. "
    
    return context

def getContextMany():
    context = "You will be given a list of words and their categories seperated by commas. "
    context += "For example - Word: {'chicken'} Category: {'animal'}, Word: {'water'} Category: {'drink'}. "
    context += "Expand each given word into a descriptive phrase, making sure to keep the category in context. "
    context += "For example, water -> a glass of water, beer -> a mug of beer, bread -> a loaf of bread. "
    context += "If the category is not provided (NONE), assume the category is 'thing'. "
    context += "Some words will not need to be changed, such as shirt or clown. "
    context += "Do not overcomplicate each phrase. "
    context += "Do not add unnecessary details. "
    context += "Do not add ajdectives or adverbs. "
    context += "Do not change the plurality of the word. "
    context += "Return the expanded text for each word in a comma seperated list. "
    
    return context

def getPromptOne(word, category):
    return "Word: {'" + word + "'} Category: {'" + category + "'} "

def getPromptMany(wordList, categories):
    wordList = wordList.split(",")
    categories = categories.split(",")
    s = ""
    for i in range(len(wordList)):
        s += "Word: {'" + wordList[i].strip() + "'} Category: {'" + categories[i].strip() + "'}, "
    return s

def callOpenAI(context, prompt, client):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    return response.choices[0].message.content

def expandWord(word, category):
    client = getClient()
    
    context = getContextOne()
    prompt = getPrompt(word, category)
    
    phrase = callOpenAI(context, prompt, client)
    
    return phrase

def expandWordList(words, categories):
    """Expands a word list words[i] corresponding to categories[i]

    :param words: comma seperated list of words
    :type words: str
    :param categories: comma seperated list of categories
    :type categories: str
    :return: comma seperated list of expanded phrases
    :rtype: str
    """
    client = getClient()
    
    context = getContextMany()
    prompt = getPromptMany(words, categories)
    
    phrase = callOpenAI(context, prompt, client)
    
    return phrase

def main():
    word = input("word: ")
    category = input("category: ")
    
    if word.find(",") == -1:
        context = getContextOne()
        prompt = getPromptOne(word, category)
    else:
        context = getContextMany()
        prompt = getPromptMany(word, category)
    
    phrase = callOpenAI(context, prompt, getClient())
    
    print(phrase)
    
    for p in phrase.split(","):
        generateImage(p.lstrip())

if __name__ == "__main__":
    main()
