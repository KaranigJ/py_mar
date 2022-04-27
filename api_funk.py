import gspread
from oauth2client.service.account import ServiceAccountCredentials


link = ['https://docs.google.com/spreadsheets/d/1Bk92HaMzh6zD4N8igXZbyK3BiSYzw_wA17rS2BuNTko/edit#gid=229531669']
my_creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', link)
client = gspread.authorize(my_creds)

sheet = client.open('Копия Марафон, поток 2 - 25.04.22').sheet1

get_data = sheet.get_all_records()

print(get_data)