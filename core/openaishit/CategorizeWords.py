import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

'''
to use, import catoregizeWordList from CategorizeWords.py

catoregizeWordList(words):
    words - a string of words seperated by commas
    returns - a string of words and their categories in the format Word: {'word'} Category: {'category'}, Word: {'word'} Category: {'category'}
    
(i can change the format to something better if you want)

'''

def getClient():
    return OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

def getContext():
    context = "You will be given a list of words seperated by commas. "
    context += "For example - chicken, water, beer, bread. "
    context += "Create a few subcategories for the list of words. "
    context += "Try to minimize the number of subcategories. "
    context += "Assign each word to one subcategory. "
    context += "For example, chicken -> animal, water -> drink, beer -> drink, bread -> food. "
    context += "Each category should have at least one word. "
    context += "Return the subcategories for each word in a comma seperated list. "
    context += "Follow the format - Word: {'word'} Category: {'category'}, Word: {'word'} Category: {'category'}. "
    
    return context

def getPrompt(words):
    s = ""
    for w in words.split(","):
        s += w.rstrip() + ", "
    return s

def callOpenAI(context, prompt, client):
    context = getContext()
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    return response.choices[0].message.content

def catoregizeWordList(words):
    client = getClient()
    
    context = getContext()
    prompt = getPrompt(words)
    
    phrase = callOpenAI(context, prompt, client)
    
    return phrase

def main():
    # wordlist = input("words: ")
    wordlist = "chicken, water, carrot, wallet, bottle, tree, hat, shirt, spinach, cow, steak, bush, watch, lemonade, beer, bread, book"
    
    categories = catoregizeWordList(wordlist)
    
    for c in categories.split(", "):
        print(c)
    # print(categories)
    
    # context = getContext()
    # prompt = getPrompt(wordlist)
    
    # phrase = callOpenAI(context, prompt, getClient())
    
    # print(phrase)
    
    # generateImage(phrase)

if __name__ == "__main__":
    main()
