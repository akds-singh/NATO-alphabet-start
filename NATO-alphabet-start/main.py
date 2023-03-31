student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(key, value)
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student," : ", row.score)
    # print(row.score)
    # Access index and row
    # Access row.student or row.score
    pass
df = pandas.read_csv('nato_phonetic_alphabet.csv', index_col= None)
# Keyword Method with iterrows()

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input('Enter a word: ').upper()
# if user_word in data_dict.values():
res_list = [data_dict[letter] for letter in user_word  if letter in data_dict.keys() ]
print(res_list)