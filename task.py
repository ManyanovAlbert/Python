def authenticate(username, password):
    if username == "user" and password == "password":
        return True
    else:
        return False


def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def write_to_file(filename, content, shift):
    encrypted_content = caesar_cipher_encrypt(content, shift)
    with open(filename, 'w') as file:
        file.write(encrypted_content)
        print("Данные успешно зашифрованы и записаны в файл", filename)


def read_from_file(filename, shift):
    with open(filename, 'r') as file:
        content = file.read()
        decrypted_content = caesar_cipher_decrypt(content, shift)
        print("Дешифрованное содержимое файла", filename, ":", decrypted_content)


def main():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if authenticate(username, password):
        choice = input("Выберите действие: 1 - записать в файл, 2 - прочитать из файла: ")
        filename = input("Введите название файла: ")

        if choice == '1':
            data = input("Введите данные для записи в файл: ")
            shift = int(input("Введите сдвиг для шифра Цезаря: "))
            write_to_file(filename, data, shift)
        elif choice == '2':
            shift = int(input("Введите сдвиг для шифра Цезаря: "))
            read_from_file(filename, shift)
        else:
            print("Некорректный выбор действия")
    else:
        print("Неправильное имя пользователя или пароль")


if __name__ == "__main__":
    main()

