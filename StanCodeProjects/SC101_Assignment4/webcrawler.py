"""
File: webcrawler.py
Name: Karen Chang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        # filter the html data to get the data between <tr> and </tr>
        data1 = soup.find('tbody')
        data2 = data1.find_all('tr')

        male_total = 0      # the sum of total male babies number
        female_total = 0    # the sum of total Female babies number

        # get the data of babies number
        for tr in data2:
            txt = tr.text
            txt_list = txt.split()

            if not str(txt_list)[2].isalpha():
                if not str(txt_list)[4].isalpha():
                    male_total += int(transfer_number(txt_list[2]))
                    female_total += int(transfer_number(txt_list[4]))

        print('Male number:', male_total)
        print('Female number:', female_total)


def transfer_number(trans_number):
    """
    This function will transfer a string of number with is with ',' into a figure format of number

    Input:
        trans_number(str): a string of numbers with "," between every three numbers, e.g. '123,456'

    Output:
        return: figure(int): the figure format of the trans_number without ",' in it, e.g. '123456'
    """

    figure = ''
    for i in range(len(trans_number)):
        if trans_number[i] != ',':
            figure += trans_number[i]
    return int(figure)


if __name__ == '__main__':
    main()
