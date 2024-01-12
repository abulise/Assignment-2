def decrypt_cryptogram(cryptogram, shift):
    decrypted_text = ''

    for char in cryptogram:
        if char.isalpha():
            ascii_value = ord(char)
            decrypted_ascii_value = (ascii_value - shift - ord('A')) % 26 + ord('A')
            decrypted_char = chr(decrypted_ascii_value)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    print("Decrypted Text:", decrypted_text)
    return decrypted_text

cryptogram = 'VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR'

for shift in range(1, 26):
    decrypted_text = decrypt_cryptogram(cryptogram, shift)
    print(f'Shift: {shift}, Decrypted Text: {decrypted_text}')
