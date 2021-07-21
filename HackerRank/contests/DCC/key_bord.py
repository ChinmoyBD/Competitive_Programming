while True:
    a_string = input().lower()
    if a_string == 'end.':
        break

    remove_characters = ["b","t","p","q",'r','m']

    for character in remove_characters:
        a_string = a_string.replace('b', '9')
        a_string = a_string.replace('t', '2')
        a_string = a_string.replace('p', '@')
        a_string = a_string.replace('q', '0')
        a_string = a_string.replace('r', '3')
        a_string = a_string.replace('m', '&')

    print(a_string)