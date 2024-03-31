import pandas

df = pandas.read_csv("./26/nato_phonetic_alphabet.csv")

# Create { "A" : "Alpha"}
data = {row["letter"]: row["code"] for index, row in df.iterrows()}

# Create a list of NATO code from user inputs
while True:
    try:
        word = input("Entry word to convert to NATO phonetic alphabet (or E for exit): ").upper()
        if word == "E":
            break
        word_list = [data[letter] for letter in word]
        print(word_list)
    except KeyError:
        print("Invalid input. Only letter in alphabet!")

    

