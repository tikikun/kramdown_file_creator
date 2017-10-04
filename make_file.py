#!/usr/bin/env python3
"""
This is for creating a file in kramdown format

Running this program you can create a file with certain kramdown attribute
that you want to have

"""
from re_name import prepare_the_file

header = {'title': '', 'description': '', 'header': ''}


def adding_attribute():
    attribute = input('Input your addtional attribute : ')
    value = input('This is your key value : ')
    header[attribute] = value


def start_adding_attritube():
    while True:
        adding_attribute()
        stop = input('Next or stop?(n or s): ')
        if stop == 'n':
            continue
        elif stop == 's':
            break


def gen_front_matter(header):
    front_matter = ''
    for attribute in header:
        info_line = '{0}: {1}\n'.format(attribute, header[attribute])
        front_matter += info_line
    front_matter = '---\n' + front_matter + '---\n'
    return front_matter


def main():
    for attribute in header:
        value = input('What is your {0} : '.format(attribute))
        header[attribute] = value
    starter = input('Do you want to add more attributes (y/n) : ')
    if starter == 'y':
        start_adding_attritube()
    print(gen_front_matter(header))
    with open('tempfile.md', 'w') as file:
        file.write(gen_front_matter(header))
    prepare_the_file('tempfile.md')


if __name__ == '__main__':
    main()
