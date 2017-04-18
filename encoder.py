# -*- coding: utf-8 -*-
__author__ = 'Vit'
import csv,sys

class Dates:
    def __init__(self, row:list):

        self.start_col=None
        self.dates=[]

        for i, date in enumerate(row):
            if date:
                self.start_col=i
                break

        for date in row[self.start_col:]:
            if date:
                self.dates.append(date)
            else:
                break

        # print(self.dates)

class LineData:
    def __init__(self, row:list, start_col:int, columns:int):
        self.data=[]
        for x in row[start_col:start_col+columns]:
            self.data.append(self.convert_data(x))

        # print(self.data)

    def convert_data(self, string:str):
        return string


class ServersData(LineData):
    pass

class MenuData(LineData):
    def __init__(self, row: list, start_col: int, columns: int):
        self.category=row[0]
        self.sub_category=row[1]
        self.goods=row[2]
        self.price=row[3]

        if self.is_goods():
            super().__init__(row, start_col, columns)
        else:
            self.data = None

        # print(self.category,self.sub_category,self.goods,self.data)

    def convert_data(self, string: str):
        return int(string) if string else 0

    def is_category(self)->bool:
        return self.category

    def is_sub_category(self)->bool:
        return self.sub_category

    def is_goods(self)->bool:
        return self.goods

class CardsData(LineData):
    def convert_data(self, string: str):
        return int(string)


class Check:
    def __init__(self, date:str):
        self.date=date
        self.categories=[]

    def set_server(self, name:str):
        self.server_name=name
        # print('set server', name, 'to', self.date)

    def add_category(self, name:str):
        # print('add category',name, 'to', self.date)
        self.categories.append(dict(name=name, data=[]))

    def add_goods(self, name:str, price:str, count:int):
        self.categories[-1]['data'].append(dict(name=name,price=self._read_price(price),count=count))
        # print('add goods', name, 'price',self._read_price(price), 'count', count, 'to', self.date)

    def set_cards(self, amount:int):
        self.cards=amount
        # print('set cards',amount, 'to', self.date)

    def _read_price(self,price_str:str)->float:
        return float(price_str.rstrip('р.').replace(',','.'))

    def _format_rub(self, sum:float)->str:
        return '{0:,.2f}'.format(sum).replace(',',' ').replace('.', ',') + 'р.'

    def _category_total(self, category:dict)->float:
        sum=0.0
        for item in category['data']:
            sum+=item['price']*item['count']

        return sum

    def _total(self)->float:
        sum=0.0
        for cat in self.categories:
            sum+=self._
        return '100.00р.'

    def _total_cash(self):
        return self._total()

    def print(self, stream=sys.stdout):
        TWO_RECORD_FORMAT='{0:31}{1:>11}'
        THREE_RECORD_FORMAT='{0:17}{1:>10}{2:>15}'

        print('                POS DEMO RU',file=stream)
        print('              ИП Никитин В.А.')
        print('             ИНН: 781124376625')
        print('------------------------------------------')#, len('------------------------------------------'))
        print('{0:^42}'.format(self.date))
        print('------------------------------------------')
        print(TWO_RECORD_FORMAT.format('Итого', self._total()))
        print('=========================================')
        print('-----------------------------------------')
        print('Продажи по товарам                        ')
        print('------------------------------------------')

        # print('printing check')
        # print('date',date)
        # print('server',server)
        for category in self.categories:
            if self._category_total(category):
                print(TWO_RECORD_FORMAT.format(category['name'],'####'))
                print('Наименован.          Кол-во          Сумма')
                print('-----------------------------------------')
                for item in category['data']:
                    # print(item)
                    name=item['name']
                    count='{0:.2f}'.format(item['count']).replace('.',',')
                    sum=self._format_rub(item['count']*item['price'])


                    first_line_name=name[:17]
                    name=name[17:]
                    # print(first_line_name,name)
                    print(THREE_RECORD_FORMAT.format(first_line_name,count,sum))
                    while name:
                        print('{0:42}'.format(name[:17]))
                        name = name[17:]



                print('-----------------------------------------')
                print(TWO_RECORD_FORMAT.format('Итого: ' + category['name'], self._format_rub(self._category_total(category))))
                print('=========================================')
                print()


        print('Продажи по Официантам                     ')
        print('------------------------------------------')
        print('Наименование                         Сумма')
        print('-----------------------------------------')

        print(TWO_RECORD_FORMAT.format(self.server_name,self._total()))
        print(TWO_RECORD_FORMAT.format('-Наличные', self._total_cash()))
        if self.cards:
            print('cards', self.cards)
        else:
            print()

        print('=========================================')
        print('POS Sector - 2015')


csv_filename='files/menu_prepared1.csv'

with open(csv_filename, encoding='cp866') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')

    data_row=csvreader.__next__()
    # print(data_row)
    dates=Dates(data_row)

    checks=[]
    for date in dates.dates:
        checks.append(Check(date))

    server_row=csvreader.__next__()
    # print(server_row)
    servers=ServersData(server_row,dates.start_col,len(dates.dates))

    for check,server in zip(checks,servers.data):
        check.set_server(server)

    for row in csvreader:
        if row[0].startswith('#'):
            break
        # print(row)
        menu_data=MenuData(row,dates.start_col,len(dates.dates))
        if menu_data.is_category():
            for check in checks:
                check.add_category(menu_data.category)

        if menu_data.is_goods():
            for check, count in zip(checks,menu_data.data):
                if count:
                    check.add_goods(menu_data.goods, menu_data.price, count)


    summ_row=csvreader.__next__()
    # print(summ_row)

    card_row=csvreader.__next__()
    # print(card_row)
    cards=CardsData(card_row,dates.start_col,len(dates.dates))
    for check,card in zip(checks,cards.data):
        check.set_cards(card)

    for check in checks:
        check.print()
