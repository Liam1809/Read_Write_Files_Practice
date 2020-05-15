import csv
# Reading a CSV File
with open("cool_csv.csv") as cool_csv_file:
  # for row in cool_csv_file:
  #   print(row.strip())
  cool_csv_dict = csv.DictReader(cool_csv_file)
  # print(list(cool_csv_dict))
  for row in cool_csv_dict:
    print(row['Cool Fact'])
# Reading Different Types of CSV Files
with open("books.csv", newline = '') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter = "@")
  isbn_list = [row['ISBN'] for row in books_reader]
  print(isbn_list)