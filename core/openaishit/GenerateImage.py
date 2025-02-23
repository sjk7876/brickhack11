import os
import requests

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

'''
to use, import generateImage from GenerateImage.py

generateImage(target):
    target - a string of the target word/phrase
    downloads images to the static/images folder with the name of the target word/phrase
'''

def getClient():
    return OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

def getImagePrompt(target):
    # art_style = "a clipart with few colors, distinct borders, and a focus on the subject"
    
    # instructions = f"Generate an image in the style of {art_style}, with the subject of '{target}'\n"
    # instructions += "The image should have a white background, black edges, and the subject should be the focal point.\n"
    # instructions += "The subject should be easily recognizable, and the colors should be vibrant.\n"
    # # instructions += "This image is going to be used for a children's book, so it should be simple and easy to understand.\n"
    # instructions += "There should be no text or logos in the image.\n"
    # # instructions += "There should be no people or faces in the image.\n"
    # instructions += "The image should be a cartoon or illustration, not a photograph.\n"
    # # instructions += 
    # instructions += "The image should be 256x256 pixels, and of standard quality."
    
    # # instructions = f"A minimalist, modern icon illustration of {target}, designed with thick, dark, rounded outlines surrounding the object and smooth geometric shapes. "
    # instructions = f"A minimalist, modern icon illustration of {target}, like clipart, designed with thick, black, rounded outlines surrounding the object and smooth shapes. "
    # instructions += "The color palette features soft pastel tones, including soft greens, oranges, blues, and a warm beige solid background. "
    # instructions += "Do NOT display the color palette in the image. "
    # instructions += "The image should ONLY contain the subject, with no other objects, background, text, dots, or lines. "
    # instructions += "Do not put a square border around the image. "
    # instructions += "The image has subtle, solid shading and highlights to create a slight three-dimensional effect, with a light source from the top left. "
    # instructions += "The style is clean, professional, resembling high-quality digital vector art - similar to clipart."
    # instructions += "There should only be one subject in the image, and it should be centered and clearly visible. "
    # instructions += "The outlines should be consistent and uniform, with no overlapping or intersecting lines - they offer clarity to the reader. "
    # instructions += "This image is going to be used for children to identify objects, so it should be simple and easy to understand. "
    # instructions += "The subject should take up 75 percent of the image with little extra space. "
    # instructions += "The border of the subject should be thick and black, with a rounded. "
    # # instructions += "The border of of the image should be thick and dark, with a rounded edge. "
    
    # instructions = f"Generate an image of {target} as simple clipart. " 
    # instructions += f"Make the image very simple, with at least one color, with only one subject, and no text. "
    # instructions += f"Make the background a cool light grey. "
    # instructions += f"Make the subject the focal point of the image - use thick black borders to surround the subject. "
    # instructions += f"It should very obviously be {target}. "
    
    # instructions = f"Create a simple clipart-style image of {target}. "
    # instructions += f"The subject should be the sole subject with distinctive thick black borders to highlight its importance and color for simple detail. "
    # instructions += f"The subject should undoubtedly resemble a real-life {target}, and be placed against a cool light grey background. "
    # instructions += f"The whole composition should be minimalistic and straightforward, with no text incorporated into the image. "
    
    instructions = f"Generate a simple, realistic image of {target}. "
    instructions += f"The image should be a realistic representation of {target}, with a focus on the subject. "
    instructions += f"The background should be a simple with no additional objects or text. "
        
    return instructions

def callDALLE(client, prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    return response

def downloadImage(target, url):
    if not url:
        return
    
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return
    
    fn = target.split(" ")
    if len(fn) > 0 and fn[0] == "a":
        fn = fn[1:]
    fn = "_".join(fn)
    
    try:
        with open(f"../static/images/{fn}.png", "wb") as file:
            file.write(response.content)
    except Exception as e:
        print(e)
        return

def generateImage(target):
    client = getClient()
    prompt = getImagePrompt(target)
    response = callDALLE(client, prompt)
    downloadImage(target, response.data[0].url)

def generageImages(targetList):
    for target in targetList:
        generateImage(target)

def main():
    client = getClient()
    
    # targetList = ["a red apple", "a glass of lemonade", "a glass of water", "a loaf of bread", "a book"]
    # targetList = ["a glass of lemonade", "a glass of water"]
    # targetList = ["clown"]
    targetList = ["a mug of beer", "beer"]
    for target in targetList:
        prompt = getImagePrompt(target)
        
        response = callDALLE(client, prompt)
        
        # for r in response.data:
        #     print(r)
        #     downloadImage(target, r.url)
        #     print(r.url)
        
        downloadImage(target, response.data[0].url)
        print(response.data[0].revised_prompt)
        print(response.data[0].url)
        # print(response)
        # print()

if __name__ == "__main__":
    main()
