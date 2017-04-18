# -*- coding: utf-8 -*-
__author__ = 'Vit'
import csv

if __name__ == "__main__":
    menu_file='files/export-article-current-ingredients.txt'
    out_file='files/menu.csv'

    with open(menu_file, encoding='utf-8') as menu:
        for line in menu:
            # print(line)
            if line.startswith('-'):
                break

        with open(out_file,'w', newline='') as csv_file:
            csvwriter=csv.writer(csv_file, delimiter=';')
            for line in menu:
                if line.strip()=='':
                    continue
                print(line.__repr__())
                data=line[:33].strip()
                price=line[33:].strip()
                print(data,'*',price)

                csvwriter.writerow([data,price])

