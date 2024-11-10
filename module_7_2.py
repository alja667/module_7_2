

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}

    for i, string in enumerate(strings, 0):
        strings_position[i, file.tell()] = string
        file.write(f'{string}\n')
    file.close()


    return strings_position

info = ['Text for tell.','Используйте кодировку utf-8.',
    'Because there are 2 languages!', 'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)






