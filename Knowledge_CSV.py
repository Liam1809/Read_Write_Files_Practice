# Reading a CSV File
# Recall our CSV file from our last exercise:

# users.csv

# Name,Username,Email
# Roger Smith,rsmith,wigginsryan@yahoo.com
# Michelle Beck,mlbeck,hcosta@hotmail.com
# Ashley Barker,a_bark_x,a_bark_x@turner.com
# Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com
# Even though we can read these lines as text without a problem, there are ways to access the data in a format better suited for programming purposes. In Python we can convert that data into a dictionary using the csv library’s DictReader object. Here’s how we’d create a list of the email addresses of all of the users in the above table:

# import csv

# list_of_email_addresses = []
# with open('users.csv', newline='') as users_csv:
#   user_reader = csv.DictReader(users_csv)
#   for row in user_reader:
#     list_of_email_addresses.append(row['Email'])
# In the above code we first import our csv library, which gives us the tools to parse our CSV file. We then create the empty list list_of_email_addresses which we’ll later populate with the email addresses from our CSV. Then we open the users.csv file with the temporary variable users_csv.

# We pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV (read more about this in the Python documentation).

# After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python dictionaries which we can use access methods for. The keys of the dictionary are, by default, the entries in the first line of our CSV file. Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key in each row of our DictReader.

# When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary). By accessing the 'Email' key of each of these rows we can grab the email address in that row and append it to our list_of_email_addresses.

# Reading Different Types of CSV Files
# I need to level with you, I’ve been lying to you for the past two exercises. Well, kind of. We’ve been acting like CSV files are Comma-Separated Values files. It’s true that CSV stands for that, but it’s also true that other ways of separating values are valid CSV files these days.

# People used to call Tab-Separated Values files TSV files, but as other separators grew in popularity everyone realized that creating a new .[a-z]sv file format for every value-separating character used is not sustainable.

# So we call all files with a list of different values a CSV file and then use different delimiters (like a comma or tab) to indicate where the different values start and stop.

# Let’s say we had an address book. Since addresses usually use commas in them, we’ll need to use a different delimiter for our information. Since none of our data has semicolons (;) in them, we can use those.

# addresses.csv

# Name;Address;Telephone
# Donna Smith;126 Orr Corner Suite 857\nEast Michael, LA 54411;906-918-6560
# Aaron Osborn;6965 Miller Station Suite 485\nNorth Michelle, KS 64364;815.039.3661x42816
# Jennifer Barnett;8749 Alicia Vista Apt. 288\nLake Victoriaberg, TN 51094;397-796-4842x451
# Joshua Bryan;20116 Stephanie Stravenue\nWhitneytown, IA 87358;(380)074-6173
# Andrea Jones;558 Melissa Keys Apt. 588\nNorth Teresahaven, WA 63411;+57(8)7795396386
# Victor Williams;725 Gloria Views Suite 628\nEast Scott, IN 38095;768.708.3411x954
# Notice the \n character, this is the escape sequence for a new line. The possibility of a new line escaped by a \n character in our data is why we pass the newline='' keyword argument to the open() function.

# Also notice that many of these addresses have commas in them! This is okay, we’ll still be able to read it. If we wanted to, say, print out all the addresses in this CSV file we could do the following:

# import csv

# with open('addresses.csv', newline='') as addresses_csv:
#   address_reader = csv.DictReader(addresses_csv, delimiter=';')
#   for row in address_reader:
#     print(row['Address'])
# Notice that when we call csv.DictReader we pass in the delimiter parameter, which is the string that’s used to delineate separate fields in the CSV. We then iterate through the CSV and print out each of the addresses.


# Writing a CSV File
# Naturally if we have the ability to read different CSV files we might want to be able to programmatically create CSV files that save output and data that someone could load into their spreadsheet software. Let’s say we have a big list of data that we want to save into a CSV file. We could do the following:

# big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

# import csv

# with open('output.csv', 'w') as output_csv:
#   fields = ['name', 'userid', 'is_admin']
#   output_writer = csv.DictWriter(output_csv, fieldnames=fields)

#   output_writer.writeheader()
#   for item in big_list:
#     output_writer.writerow(item)
# In our code above we had a set of dictionaries with the same keys for each, a prime candidate for a CSV. We import the csv library, and then open a new CSV file in write-mode by passing the 'w' argument to the open() function.

# We then define the fields we’re going to be using into a variable called fields. We then instantiate our CSV writer object and pass two arguments. The first is output_csv, the file handler object. The second is our list of fields fields which we pass to the keyword parameter fieldnames.

# Now that we’ve instantiated our CSV file writer, we can start adding lines to the file itself! First we want the headers, so we call .writeheader() on the writer object. This writes all the fields passed to fieldnames as the first row in our file. Then we iterate through our big_list of data. Each item in big_list is a dictionary with each field in fields as the keys. We call output_writer.writerow() with the item dictionaries which writes each line to the CSV file.