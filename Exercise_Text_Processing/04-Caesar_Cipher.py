# 04. Caesar Cipher
decrypted_text = input()

encrypted_text = ''

for element in decrypted_text:
    for index in range(0, len(element)):
        encrypted_element = chr(ord(element[index]) + 3)
        encrypted_text += encrypted_element
print(encrypted_text)