# -*- coding: utf-8 -*-
__author__ = 'Vit'

def open_menu(filename:str)->list:
    def reconvert_menu(record:dict)->dict:
        result=dict()
        result['PRODUCT']=int(record['PRODUCT_CODE'])
        result['ITEM'] = int(record['ITEM_CODE'])
        result['GROSS_WEIGHT'] = float(record['ITEM_GROSS_WEIGHT'])
        result['NET_WEIGHT'] = float(record['ITEM_NET_WEIGHT'])
        result['OUT_WEIGHT'] = float(record['ITEM_OUT_WEIGHT'])
        result['AMOUNT'] = float(record['AMOUNT'])

        # print(result)
        return result

    with open(filename, encoding='UTF-8') as fd:
        first_line=fd.readline().strip()
        first_line_split=first_line.split(';')
        # print(first_line_split)
        menu=list()
        for line in fd:
            split=line.strip().split(';')
            record=dict()
            for key,value in zip(first_line_split,split):
                record[key]=value
            # reconvert_menu(record)
            menu.append(reconvert_menu(record))
        return menu



def open_base(filename:str)->dict:
    def reconvert_base(record:dict)->tuple:
        print(record)
        result=dict()
        key=int(record['NUM'])
        result['NAME']=record['NAME']
        result['TYPE'] = record['TYPE']
        result['UNIT'] = record['MEASURE_UNIT']
        result['UNIT_WEIGHT'] = float(record['UNIT_WEIGHT'].replace(',','.')) if record['UNIT_WEIGHT'] else 0.0
        result['PRICE'] = float(record['PRICE'].replace(',','.')) if record['PRICE'] else 0.0

        result['PARENT_CODE'] = int(record['PARENT_CODE']) if record['PARENT_CODE'] else -1
        result['IN_MENU'] = True if record['INCLUDED_IN_MENU'] == '1' else False

        print(key,result)
        return key, result

    with open(filename, encoding='UTF-8') as fd:
        first_line=fd.readline().strip()
        first_line_split=first_line.split(';')
        print(first_line_split)
        base=dict()
        for line in fd:
            split=line.strip().split(';')
            record=dict()
            for key,value in zip(first_line_split,split):
                record[key]=value
            num=int(record['NUM'])
            base[num]=record
            reconvert_base(record)

        return base


if __name__ == "__main__":
    base=open_base('files/меню лист 2.csv')
    # for key in sorted(base):
    #     print(key,base[key])

    menu=open_menu('files/Меню 2.csv')
    # for item in menu:
    #     print(item)







