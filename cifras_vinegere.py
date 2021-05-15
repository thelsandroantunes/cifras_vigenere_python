#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import os
import re


# In[ ]:


continue_cipher = ""
demo_alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
demo_key = "PALIMPSEST"
demo_cipher_string = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD"
demo_cipher_decoded = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION"


## Visuals
def display_header():
    print("################################################")
    print("#                                              #")
    print("#            --- CIFRA VIGENERE ---            #")
    print("#                                              #")
    print("#    Um decodificador/codificador  simples     #")
    print("#                                              #")
    print("################################################", end="\n\n")
    return
def display_results(mode, cipher_vars):
    # Clear screen for final results
    os.system('cls')

    # Display header
    display_header()

    # Decompose cipher_vars
    (alphabet, key, cipher_string, results) = cipher_vars

    print("Modo:", "Descriptografar" if mode == "D" else "Criptografar", end="\n\n")
    print("Alfabeto:", alphabet)
    print("Chave:", key)
    print("Mensagem Cifrada:", cipher_string, end="\n\n")
    print("Mensagem Decodificada:" if mode == "D" else "Mensagem Codificada:", results, end="\n\n")
    return


## Validations
def string_is_alpha(input_string):
    return True if re.match("^[a-zA-Z_]*$", input_string) else False


## Cipher variables
def get_alphabet():
    global demo_alphabet

    while True:
        alphabet = input("Digite o alfabeto cifrado: ").upper()
        if alphabet == "":
            alphabet = demo_alphabet
            break
        elif string_is_alpha(alphabet) is False:
            print("O alfabeto não é válido. O alfabeto não deve conter espaços, dígitos ou caracteres especiais.")
        else:
            break

    return alphabet
def get_key():
    global demo_key

    while True:
        key = input("Insira a chave de criptografia: ").upper()
        if key == "":
            key = demo_key
            break
        elif string_is_alpha(key) is False:
            print("A chave não é válida. A chave não deve conter espaços, dígitos ou caracteres especiais.")
        else:
            break

    return key
def get_cipher_string(mode):
    global demo_cipher_string
    global demo_cipher_decoded

    while True:
        cipher_string = input("Insira a string de criptografia: ").upper()
        if cipher_string == "":
            cipher_string = demo_cipher_string if mode == "D" else demo_cipher_decoded
            break
        elif string_is_alpha(cipher_string) is False:
            print("A sequência de criptografia não é válida. As sequências de criptografia não devem conter espaços, dígitos ou caracteres especiais.")
        else:
            break

    return cipher_string



def get_cipher_alphabets(alphabet, key):
    cipher_alphabets = []

    for char in key:
        char_index = alphabet.find(char)
        cipher_alphabet = alphabet[char_index:] + alphabet[:char_index]
        cipher_alphabets.append(cipher_alphabet)

    return cipher_alphabets
def start_cipher(mode, alphabet, key, cipher_string):
    mode_string = ""
    cipher_alphabets = get_cipher_alphabets(alphabet, key)
    
    cipher_alphabet_index = 0
    for char in cipher_string:
        
        if cipher_alphabet_index == len(cipher_alphabets):
            cipher_alphabet_index = 0
        
        
        if mode == "D":
            mode_string += alphabet[cipher_alphabets[cipher_alphabet_index].find(char)]
        else:
            mode_string += cipher_alphabets[cipher_alphabet_index][alphabet.find(char)]

        cipher_alphabet_index += 1

    return mode_string


## Cipher Mode
def get_cipher_mode():
    while True:
        cipher_mode = input("Escolha o modo de cifra - [D]escriptografar or [C]riptografar: ").upper()
        if cipher_mode != "D" and cipher_mode != "C":
            print("Essa não é uma opção válida. Por favor, digite 'D' para descriptografar e 'E' para criptografar.")
        else:
            break

    print("")
    return cipher_mode
def start_cipher_mode(mode):
    print("Pressione 'enter' para usar as opções de demonstração")
    alphabet = get_alphabet()
    key = get_key()
    cipher_string = get_cipher_string(mode)
    mode_string = start_cipher(mode, alphabet, key, cipher_string)
    return alphabet, key, cipher_string, mode_string

def get_continue_cipher():
    while True:
        continue_cipher = input("Você quer decodificar / codificar ainda?[S/N]: ").upper()
        if continue_cipher != "S" and continue_cipher != "N":
            print("Essa não é uma opção válida. Digite 'S' para continuar e 'N' para sair.")
        else:
            break
    return continue_cipher

while continue_cipher != "N":
   
    os.system('cls')

    display_header()


    cipher_mode = get_cipher_mode()
    cipher_vars = start_cipher_mode(cipher_mode)


    display_results(cipher_mode, cipher_vars)

    continue_cipher = get_continue_cipher()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




