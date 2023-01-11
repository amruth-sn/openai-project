import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY

def generateVideoTitles(prompt1):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate viral YouTube video titles for: {}. \n \n 1.".format(prompt1),
    temperature=0.7,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response['choices'][0]['text']
def generateVideoScripts(prompt1):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Expand the following video title into a very long, high-level, 750-word-maximum YouTube video script, with an introduction and an outro: {} \n\n- Script:".format(prompt1),
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']

