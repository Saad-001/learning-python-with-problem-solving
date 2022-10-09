# clean your data

data_1 = "AnBpEiqo>>/nU"
new_data = data_1.lower()

output_data = ""

for character in new_data : 
    if(character == 'a') or (character == 'e') or (character == 'i') or (character == 'o') or (character == 'u') :
            output_data += character + "_"

print(output_data[0:9]);

# encrypt your data

data_2 = 'firebaby'
shift = 4

encrypted_data = ""

for character in data_2 :
    encrypted_data += chr((ord(character) + shift - 97) % 26 + 97)

print(encrypted_data);

# now decrypt your encrypt data

decrypted_data = ""

for character in encrypted_data :
    decrypted_data += chr((ord(character) - shift - 97) % 26 + 97)

print(decrypted_data);
