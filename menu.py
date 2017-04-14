# -*- coding: utf-8 -*-
__author__ = 'Vit'

def open_menu(filename:str)->list:
    with open(filename, encoding='UTF-8') as fd:
        first_line=fd.readline().strip()
        first_line_split=first_line.split(';')
        menu=list()
        for line in fd:
            split=line.strip().split(';')
            record=dict()
            for key,value in zip(first_line_split,split):
                record[key]=value
            menu.append(record)

        return menu

def open_base(filename:str)->dict:
    with open(filename, encoding='UTF-8') as fd:
        first_line=fd.readline().strip()
        # print(first_line)
        first_line_split=first_line.split(';')
        # print(first_line_split)
        base=dict()
        for line in fd:
            # print(line)
            split=line.strip().split(';')
            # print(split)

            record=dict()
            for key,value in zip(first_line_split,split):
                # print(key,value)
                record[key]=value
            num=int(record['NUM'])
            base[num]=record

        # for key in sorted(base):
        #     print(key,base[key])
        return base


if __name__ == "__main__":
    base=open_base('files/меню лист 2.csv')
    # for key in sorted(base):
    #     print(key,base[key])

    menu=open_menu('files/Меню.csv')
    # for item in menu:
    #     print(item)






