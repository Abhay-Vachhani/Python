# # Write a file

# with open('data.txt', 'w') as fp:
#     fp.write('Hello World')

# # Read File

# with open('data.txt', 'r') as fp:
#     data = fp.read()

# print(data)

# # Check the file is exists or not
# import os

# if os.path.isfile('data1.txt'):
#     print('The file is exist')
# else:
#     print('The file not found')

# # Create a file if not exist and write user input to it other wise read the content of the file

# import os

# fileName = 'user.txt'

# if os.path.isfile(fileName):
#     with open(fileName, 'r') as fp:
#         print('Name in a file is', fp.read())
# else:
#     with open(fileName, 'w') as fp:
#         fp.write(input('Enter your name: '))

# # Count the lines words and chars in a file

# with open('user.txt', 'r') as fp:
#     fileData = fp.readlines()

# lines = len(fileData) # get lines

# words = 0
# chars = 0

# for line in fileData:
#     words += len(line.split()) # words = words + len(line.split())
#     chars += len(line.replace('\n', '')) # chars = chars + len(line.replace('\n', ''))

# # print(f'Lines: {lines}\nWords: {words}\nChars: {chars}')

# print('Lines: ', lines)
# print('Words: ', words)
# print('Chars: ', chars)

# # Copy image file to the another file

# with open('screenshot.png', 'rb') as fp1:
#     with open('newImage.png', 'wb') as fp2:
#         fp2.write(fp1.read())
