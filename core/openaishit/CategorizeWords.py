import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from GenerateImage import generateImages
from ExpandWords import expandWordList

load_dotenv()

'''
to use, import catoregizeWordList from CategorizeWords.py

catoregizeWordList(words):
    words - a string of words seperated by commas
    returns - json node object    
'''

def getClient():
    return OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

def getContext():
    context = "You will be given a list of words seperated by commas. "
    context += "For example - chicken, water, beer, bread. "
    context += "Create a few categories for the list of words. "
    context += "Try to minimize the number of categories. "
    context += "Assign each word to one category. "
    context += "For example, chicken -> animal, water -> drink, beer -> drink, bread -> food. "
    context += "Each category should have at least one word. "
    context += "You can create relevant subcategories of categories. "
    context += "For example, lettuce -> vegetable, spinach -> vegetable, vegetable -> food, chicken -> meat, meat -> food. "
    context += "Minimize the number of subcategories. "
    # context += "If there is only one word in a category, do not create a subcategory. "
    # context += "If there is only one subcategory in a category, do not create a subcategory. "
    context += "Do not return a subcategory if there is only one word in a category. "
    context += "Return the categories for each word and the subcategories of each category in a JSON format "
    context += "when returning, do not separate the words and subcategories. "
    context += "Follow the format - {'categories': [{'word': 'chicken', 'category': 'meat'}, {'word': 'meat', 'category': 'food'}, {'word': 'water', 'category': 'drink'}]}. "
    
    return context

def getPrompt(words):
    s = ""
    for w in words.split(","):
        s += w.lstrip() + ", "
    return s

def callOpenAI(context, prompt, client):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        response_format={"type": "json_object"}
    )
    
    return response.choices[0].message.content

def strToNode(s):
    def get_or_create_category(category):
        if category not in category_map:
            category_map[category] = {
                "id": str(len(category_map) + 1),
                "name": category.capitalize(),
                "image": f"core/static/images/{category}.png",
                "children": []
            }
        return category_map[category]

    
    
    data = json.loads(s)
    
    category_map = {}

    for entry in data["categories"]:
        word = entry["word"]
        category = entry["category"]
        category_node = get_or_create_category(category)
        word_node = get_or_create_category(word)
        
        # Avoid duplicate insertions
        if word_node not in category_node["children"]:
            category_node["children"].append(word_node)
    
    top_level_categories = [cat for cat in category_map.values() if all(cat not in v["children"] for v in category_map.values())]

    return top_level_categories

def downloadImageFromCatAndWord(categories):
    categories = json.loads(categories)
    print(type(categories))
    print(f"categories:\n{categories}")
    words = []
    cats = []
    print("")
    
    for word in categories['categories']:
        words.append(word["word"])
        cats.append(word["category"] + "s")
    
    for i, word in enumerate(words):
        if word + "s" in cats:
            words[i] += "s"
    
    print()
        
    print(f"words: {words}\ncategories: {cats}\n")
    
    phrases = expandWordList(", ".join(words), ", ".join(cats))
    phrases = phrases.split(", ")
    print(f"phrases: {phrases}")
    
    # for phrase in phrases:
    generateImages(phrases, cats, words)
    
def catoregizeWordList(words):
    print(os.getcwd())
    client = getClient()
    
    context = getContext()
    prompt = getPrompt(words)
    
    categories = callOpenAI(context, prompt, client)
    
    downloadImageFromCatAndWord(categories)
    
    # for phrase in phrases:
    #     print(phrase)
        
    
    node = strToNode(categories)
    
    return node

def main():
    # wordlist = input("words: ")
    wordlist = "chicken, water, carrot, wallet, bottle, tree, hat, shirt, spinach, cow, steak, bush, watch, lemonade, beer, bread, book"
    
    node = catoregizeWordList(wordlist)
    
if __name__ == "__main__":
    main()
