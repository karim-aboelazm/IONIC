import random
import json
import torch
from brain import NeuralNetwork
from voice_input import Listen
from voice_output import Say
from neural_network import *
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
                    singleCommand(reply)
                elif 'date' in reply:
                    singleCommand(reply)
                elif 'day' in reply:
                    singleCommand(reply)
                elif "break" in reply:
                    singleCommand(reply)
                elif 'open word' in reply:
                    singleCommand(reply)
                elif 'open powerpoint' in reply:
                    singleCommand(reply)
                elif 'open access' in reply:
                    singleCommand(reply)
                elif 'open excel' in reply:
                    singleCommand(reply)
                elif 'open vscode' in reply:
                    singleCommand(reply)
                elif 'open cmd' in reply:
                    singleCommand(reply)
                elif 'open chrome' in reply:
                    singleCommand(reply)
                elif 'open zoom' in reply:
                    singleCommand(reply)
                elif 'open notepad' in reply:
                    singleCommand(reply)
                elif "close word" in reply:
                    singleCommand(reply)
                elif "close powerpoint" in reply:
                    singleCommand(reply)
                elif "close vscode" in reply:
                    singleCommand(reply)
                elif "close chrome" in reply:
                    singleCommand(reply)
                elif "close notepad" in reply:
                    singleCommand(reply)
                elif "close access" in reply:
                   singleCommand(reply)
                elif "close excel" in reply:
                    singleCommand(reply)
                elif "close zoom" in reply:
                   singleCommand(reply)
                elif "close cmd" in reply:
                    singleCommand(reply)
                elif 'internet speed' in reply:
                    singleCommand(reply)
                elif "nasa news" in reply:
                    singleCommand(reply)
                elif "egy news" in reply:
                    singleCommand(reply)
                elif "wikipedia" in reply:
                    singleCommand(reply)
                    
                    multiCommand(reply,stm)
                elif "google" in reply:
                    multiCommand(reply,result)
                elif "YouTube" in reply:
                    Say('opening Sir...')
                    multiCommand(reply,result)
                elif "website" in reply:
                    Say('opening Sir...')
                    multiCommand(reply,result)
                elif "playvideo" in reply:
                    Say('playing Sir...')
                    multiCommand(reply,result)
                elif "weather" in reply:
                    Say('Forcasting Sir...')
                    multiCommand(reply,result)
                elif "temperature" in reply:
                    Say('Ok Sir...')
                    multiCommand(reply,result)
                elif "calculate" in reply:
                    multiCommand(reply,result)

                elif "whatsapp message" in reply:
                    Say('Ok Sir...')
                    multiCommand(reply,result)

                elif "whatsapp call" in reply:
                    Say('Ok Sir...')
                    multiCommand(reply,result)

                elif "whatsapp video" in reply:
                    Say('Ok Sir...')
                    multiCommand(reply,result)

                elif "whatsapp chat" in reply:
                    Say('Ok Sir...')
                    multiCommand(reply,result)

                elif 'remember that' in reply:
                    Say("Ok Sir..")
                    multiCommand(reply,result)
                elif 'what do you remember' in reply:
                    Say("Ok Sir..")
                    multiCommand(reply,result)
                
                elif "how to" in reply:
                    multiCommand(reply,result)
                
                elif "recognize" in reply:
                     multiCommand(reply,result)

                elif "corona" in reply:
                    multiCommand(reply,result)
                else:    
                    Say(reply)

def Listen_name():
    name = Listen()
    if str(name).lower() == "ionic":
        Say("Yes Sir Tell Me How Can I Help You ....")
        while True:
            assistant()
    elif str(name) == None:
        Listen_name()
#while True:
    #assistant()
