#!/usr/bin/python3
import openai #Import the module to actually use the AI's API

def GPT(text):
    openai.api_key = "GPT KEY" #Defining the api key so that you can use this
    response = openai.Completion.create( #make a response using opainai 
        engine = "text-davinci-003", #with the davinci engine,
        prompt = text, #with an inputted prompt,
        temperature = 0.5, #a balance between specific and creative answers, and it'll stay on topic 
        max_tokens = 4096, #with a maximum word count of 4096
    )   
    return print(response.choices[0].text) #return GPT-3's response to the user

def main(): 
    while True: #while the program is running, 
        print('GPT Prompt') #print a notice that this is the GPT prompt
        question = input('> ') #ask for input while showing ">"
        GPT(question) #run the question into GPT-3
main() #Run the program
