import os
import openai
import config
openai.api_key = config.OPEN_API_KEY

def generateVideoTitles(prompt1):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate viral YouTube video titles for: {}. \n \n 1.".format(prompt1),
    temperature=0.7,
    max_tokens=120,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response['choices'][0]['text']
def generateVideoScripts(prompt1):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Expand the video title into a high-level 750-word-maximum YouTube video script: {} \n\n- Script:".format(prompt1),
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']

def videoExpander(prompt1):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Expand the video script to include a professional, captivating intro and outro.\n\n {}:".format(prompt1),
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']
