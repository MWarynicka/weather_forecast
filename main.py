from requests import get
from json import loads
from terminaltables import AsciiTable

citis = input("Enter the name of the city: ")
def main():

    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows= [
        ['Miasto','Godzina pomiaru','Temperatura']
    ]

    for data in loads(response.text):
        if data['stacja'] in citis:
            rows.append([
                data['stacja'],
                data['godzina_pomiaru'],
                data['temperatura']
            ])
            print(data)
    table= AsciiTable(rows)
    print(table.table)
main()

