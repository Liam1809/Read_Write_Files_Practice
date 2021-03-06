import csv
# # Reading a CSV File
# with open("cool_csv.csv") as cool_csv_file:
#   # for row in cool_csv_file:
#   #   print(row.strip())
#   cool_csv_dict = csv.DictReader(cool_csv_file)
#   # print(list(cool_csv_dict))
#   for row in cool_csv_dict:
#     print(row['Cool Fact'])
# # Reading Different Types of CSV Files

with open("books.csv", newline = '') as books_csv:
#   print(books_csv.read())
  books_reader = csv.DictReader(books_csv, delimiter = "@")
  isbn_list = [row['ISBN'] for row in books_reader]
  print(isbn_list)
  
# Writing a CSV File
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']
import csv
with open("logger.csv", 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)



# Reading a JSON File
import json
with open("message.json") as message_json:
  message = json.load(message_json)
  print(message)
  print(message['text'])
# Writing a JSON File
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)