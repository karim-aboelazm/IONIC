import random
import json
import torch
from brain import NeuralNetwork
from neural_network import *
from voice_input import Listen
from voice_output import Say
from functionality import *
# ------------------------------------------------------------------

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# -------------------------------------------------------------------

with open('content.json','r') as jd:
    contents = json.load(jd)

FILE = 'TrainingData.pth'
data = torch.load(FILE)
model_state = data['model_state']
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model = NeuralNetwork(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def assistant():
    stm = Listen()
    result = str(stm)
    if stm == "exit" or stm == None:
        Say('Goodbye Sir')
        exit()
    stm = tokenize(stm)
    w = bag_of_words(stm,all_words)  
    w = w.reshape(1,w.shape[0])   
    w = torch.from_numpy(w).to(device)
    output = model(w)
    _ , predicted = torch.max(output,dim=1) 
    item = predicted.item()
    tag = tags[item]
    probs = torch.softmax(output,dim=1)
    prob = probs[0][item]
    if prob.item() > 0.75:
        for content in contents['content']:
            if tag == content['tag']:
                reply = random.choice(content['responses'])
                if 'time' in reply:
                    get_error(reply)
                elif 'date' in reply:
                    get_error(reply)
                elif 'day' in reply:
                    get_error(reply)
                elif "break" in reply:
                    get_error(reply)
                elif 'open word' in reply:
                    get_error(reply)
                elif 'open powerpoint' in reply:
                    get_error(reply)
                elif 'open access' in reply:
                    get_error(reply)
                elif 'open excel' in reply:
                    get_error(reply)
                elif 'open vscode' in reply:
                    get_error(reply)
                elif 'open cmd' in reply:
                    get_error(reply)
                elif 'open chrome' in reply:
                    get_error(reply)
                elif 'open zoom' in reply:
                    get_error(reply)
                elif 'open notepad' in reply:
                    get_error(reply)
                elif "close word" in reply:
                    get_error(reply)
                elif "close powerpoint" in reply:
                    get_error(reply)
                elif "close vscode" in reply:
                    get_error(reply)
                elif "close chrome" in reply:
                    get_error(reply)
                elif "close notepad" in reply:
                    get_error(reply)
                elif "close access" in reply:
                   get_error(reply)
                elif "close excel" in reply:
                    get_error(reply)
                elif "close zoom" in reply:
                   get_error(reply)
                elif "close cmd" in reply:
                    get_error(reply)
                elif 'internet speed' in reply:
                    get_error(reply)
                elif "nasa news" in reply:
                    get_error(reply)
                elif "egy news" in reply:
                    get_error(reply)
                elif "wikipedia" in reply:
                    Say('Searching Sir...')
                    get_input_error(reply,stm)
                elif "google" in reply:
                    Say('Searching Sir...')
                    get_input_error(reply,result)
                elif "YouTube" in reply:
                    Say('opening Sir...')
                    get_input_error(reply,result)
                elif "website" in reply:
                    Say('opening Sir...')
                    get_input_error(reply,result)
                elif "playvideo" in reply:
                    Say('playing Sir...')
                    get_input_error(reply,result)
                elif "weather" in reply:
                    Say('Forcasting Sir...')
                    get_input_error(reply,result)
                elif "temperature" in reply:
                    Say('Ok Sir...')
                    get_input_error(reply,result)
                elif "calculate" in reply:
                    Say('Calculating Sir...')
                    get_input_error(reply,result)

                elif "whatsapp message" in reply:
                    Say('Ok Sir...')
                    get_input_error(reply,result)

                elif "whatsapp call" in reply:
                    Say('Ok Sir...')
                    get_input_error(reply,result)

                elif "whatsapp video" in reply:
                    Say('Ok Sir...')
                    get_input_error(reply,result)

                elif "whatsapp chat" in reply:
                    Say('Ok Sir...')
                    get_input_error(reply,result)

                elif 'remember that' in reply:
                    Say("Ok Sir..")
                    get_input_error(reply,result)
                elif 'what do you remember' in reply:
                    Say("Ok Sir..")
                    get_input_error(reply,result)
                
                elif "how to" in reply:
                    get_input_error(reply,result)
                
                elif "recognize" in reply:
                     get_input_error(reply,result)

                elif "corona" in reply:
                    get_input_error(reply,result)

                else:    
                    Say(reply)

def Listen_name():
    name = Listen()
    if name == "ionic":
        Say("Yes Sir Tell Me How Can I Help You ....")
        while True:
            assistant()
    elif name == None:
        Listen_name()



