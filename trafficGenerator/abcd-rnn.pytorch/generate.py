#!/usr/bin/env python
# https://github.com/spro/char-rnn.pytorch

import torch
import os
import argparse

from helpers import *
from model import *

def generate(decoder, prime_str='a1', predict_len=100, temperature=0.8, cuda=False):

    hidden = decoder.init_hidden(1)
    prime_input = Variable(char_tensor(prime_str).unsqueeze(0))

    if cuda:
        hidden = hidden.cuda()
        prime_input = prime_input.cuda()
    predicted = prime_str

    # Use priming string to "build up" hidden state
    for p in range(len(prime_str) - 1):
        _, hidden = decoder(prime_input[:,p], hidden)
        
    inp = prime_input[:,-1]
    
    for p in range(predict_len):
        output, hidden = decoder(inp, hidden)
        
        # Sample from the network as a multinomial distribution
        output_dist = output.data.view(-1).div(temperature).exp()
        top_i = torch.multinomial(output_dist, 1)[0]

        # Add predicted character to string and use as next input
        predicted_char = all_characters[top_i]
        predicted += predicted_char
        inp = Variable(char_tensor(predicted_char).unsqueeze(0))
        if cuda:
            inp = inp.cuda()

    return predicted

def generate_couple(decoder, prime_str='a1', predict_len=100, temperature=0.8, cuda=False):

    hidden = decoder.init_hidden(1)
    prime_input = Variable(char_tensor(prime_str).unsqueeze(0))

    if cuda:
        hidden = hidden.cuda()
        prime_input = prime_input.cuda()
    predicted = prime_str

    # Use priming string to "build up" hidden state
    for p in range(len(prime_str) - 2):
        _, hidden = decoder(prime_input[:,2*p:2*p+2], hidden)
    print prime_input, " Prime input" 
    inp = prime_input[:,-2:]
    
    for p in range(predict_len):
	print inp.data.numpy(), "Guru\n" 
        output, hidden = decoder(inp, hidden)
        
        # Sample from the network as a multinomial distribution
        output_dist = output.data.view(-1).div(temperature).exp()
        top_i = torch.multinomial(output_dist[:101], 1)[0]
	top_j = torch.multinomial(output_dist[101:], 1)[0]

        # Add predicted character to string and use as next input
        predicted_char1 = all_characters[top_i]
        predicted_char2 = all_characters[top_j]
	predicted_char = predicted_char1 + predicted_char2
        predicted += predicted_char
        inp = Variable(char_tensor(predicted_char).unsqueeze(0))
        if cuda:
            inp = inp.cuda()

    return predicted


# Run as standalone script
if __name__ == '__main__':

# Parse command line arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('filename', type=str)
    argparser.add_argument('-p', '--prime_str', type=str, default='A')
    argparser.add_argument('-l', '--predict_len', type=int, default=100)
    argparser.add_argument('-t', '--temperature', type=float, default=0.8)
    argparser.add_argument('--cuda', action='store_true')
    args = argparser.parse_args()

    decoder = torch.load(args.filename)
    del args.filename
    #print(generate(decoder, **vars(args)))
    print(generate_couple(decoder, **vars(args)))
