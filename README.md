<h1 align="center"><img src="https://raw.githubusercontent.com/TheZoidMaster/KEELib/refs/heads/main/graphics/kee_github.svg" height="256px"><br>KEELib</h1>

<p align="center"><strong>An unoffical KEE library.</strong></p>

# Topics

1. [About](#about)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Encrypting/Decrypting files with a key](#encryptingdecrypting-files-with-a-key)
4. [License](#license)

# About

> "KEE is a joke turned real project. Originally I wanted to have my own cipher system (similar to a caesar cipher) for some of my friends, but then I moved on to ciphering on a binary level, and it became more of an encryption system. After a bit of back-and-forth messaging, I decided to actually make an encryption system and language." - [JaegerwaldDev](https://github.com/JaegerwaldDev)

KEELib is an unoffical KEE library. The original project is [here](https://github.com/JaegerwaldDev/KEE).

Please show Jae some support and star the KEE repo if you like it.

# Installation

To install KEELib, simply run `pip install keelib`.

It has only been tested on Python 3.11 and 3.12 at the time of writing.

# Usage

~~This section will explain every feature of KEE and XKEE, if you want to skip to certain parts, look [here](https://github.com/JaegerwaldDev/KEE/tree/main?tab=readme-ov-file#topics)!~~

This section will only explain how to use the library. To learn how to use XKEE and KEE, please refer to [KEE](https://github.com/JaegerwaldDev/KEE).

## Encrypting/Decrypting files with a key

Encrypting/Decrypting files with a key is simple. First set up an encryptor with your KEE file.

```py
from keelib import Encryptor
encryptor = Encryptor(key_path)
```

Then you can encrypt/decrypt files with the encryptor.

```py
encryptor.encrypt_file(input_file_path, output_file_path)
encryptor.decrypt_file(input_file_path, output_file_path)
```

# License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
