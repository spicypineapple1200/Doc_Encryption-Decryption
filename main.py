import string

# text = input("Enter the text here: ").strip()
text = """4hfQPW,>/,WP&,I)b&)??J)[>)G,D]>WP ,j&HWP&) ,{Hf] ,$]HW& ,Kf]b&b?_&HR>h}G,aHQQ&) ,aHQQ&),6,Je& ,aHQQ&),6,2|>)b ,a=H],2|>)b} ,a=H],'hyPHhW&b,2|>)b}?"""

choice = input("Encrypting or decrypting? Enter 'e' or 'd': ")
options = 'ed'

if choice not in options:
    while choice != 'e' or choice != 'd':
        choice = input("Incorrect. Enter 'e' or 'd': " )
        if choice == 'e' or choice == 'd':
            break

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\n']
cypher = ['s', 'Y', '7', '\n', 'n', '!', '%', '~', 'V', 'l', 'H', 'q', 'y', 'b', '&', '/', 'Q', 'P', 'f', 'L', 'w', ']', '[', 'h', '>', 'R', 'E', ')', '}', 'W', '=', 'r', '|', 'e', ':', '3', 'J', ';', 'D', 'a', "'", 'k', 'K', 'T', '5', 'U', '4', 'j', '{', '9', 'I', '$', 'd', 't', '2', 'm', '1', 'C', '_', 'v', 'A', 'B', 'F', '@', 'o', 'g', '(', '6', 'c', '-', 'X', '"', 'Z', ' ', 'M', 'x', 'S', 'G', 'z', 'u', '.', 'O', '0', 'i', '^', '*', 'N', '8', '+', '<', '`', 'p', '#', ',', '?']

if choice == 'e':
    encrypted_data = ''
    print('Encryption then. Good. Below is the encrypted data.')
    for char in text:
        if char not in cypher:
            pass
        else:
            index = characters.index(char)
            encrypted_item = cypher[index]
            encrypted_data+=encrypted_item
    print(encrypted_data)
elif choice == 'd':
    decrypted_data = ''
    print('Decryption then. Good. Below is the decryption data.')
    for char in text:
        if char not in characters:
            pass
        else:
            index = cypher.index(char)
            decrypted_item = characters[index]
            decrypted_data+=decrypted_item
    print(decrypted_data)



# ----------------------------------

# import string
# import math

# text = input("Enter the text here: ").strip()
# choice = input("Encrypting or decrypting? Enter 'e' or 'd': ")
# options = 'ed'

# if choice not in options:
#     while choice != 'e' or choice != 'd':
#         choice = input("Incorrect. Enter 'e' or 'd': " )
#         if choice == 'e' or choice == 'd':
#             break

# characters = list(string.printable)
# cypher = [num for num in range(10000)]

# if choice == 'e':
#     encrypted_data = ''
#     print('Encryption then. Good. Below is the encrypted data.')
#     for char in text:
#         index = characters.index(char)
#         encrypted_item = cypher[index**2]
#         encrypted_data+=(str(encrypted_item) + ' ')
#     print(encrypted_data)
# else:
#     decrypted_data = ''
#     print('Decryption then. Good. Below is the decryption data.')
#     text = text.split(' ')
#     for char in text:
#         index = cypher.index(int(char))
#         decrypted_item = characters[int(math.sqrt(int(char)))]
#         decrypted_data+=(decrypted_item)
#         decrypted_data = ''.join(decrypted_data)
#     print(decrypted_data)
