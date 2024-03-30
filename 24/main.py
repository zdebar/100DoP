#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("24/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("24/Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    file_name = f"{name}_letter.txt"
    with open(f"24/Output/ReadyToSend/{file_name}", mode="w") as file:
        file.write(new_letter)

