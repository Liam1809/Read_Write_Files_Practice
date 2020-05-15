# Reading a File
# Computers use file systems to store and retrieve data. Each file is an individual container of related information. If you’ve ever saved a document, downloaded a song, or even sent an email you’ve created a file on some computer somewhere. Even script.py, the Python program you’re editing in the learning environment, is a file.

# So, how do we interact with files using Python? We’re going to learn how to read and write different kinds of files using code. Let’s say we had a file called real_cool_document.txt with these contents:

# real_cool_document.txt

# Wowsers!
# We could read that file like this:

# script.py

# with open('real_cool_document.txt') as cool_doc:
#   cool_contents = cool_doc.read()
# print(cool_contents)
# This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file. We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents. Then we print cool_contents, which outputs the statement Wowsers!.

# Alternatively, one could write the code as follows.

# text_file = open('welcome.txt')
# text_data = text_file.read()
# print(text_data)
# text_file.close()

# Iterating Through Lines
# When we read a file, we might want to grab the whole document in a single string, like .read() would return. But what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line instead of having the whole thing. Suppose we have a file:

# keats_sonnet.txt

# To one who has been long in city pent,
# ’Tis very sweet to look into the fair
# And open face of heaven,—to breathe a prayer
# Full in the smile of the blue firmament.
# script.py

# with open('keats_sonnet.txt') as keats_sonnet:
#   for line in keats_sonnet.readlines():
#     print(line)
# The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt. It then iterates over each line in the document and prints the entire file out.

# Reading a Line
# Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, .readline(), which will only read a single line at a time. If the entire document is read line by line in this way subsequent calls to .readline() will not throw an error but will start returning an empty string (""). Suppose we had this file:

# millay_sonnet.txt

# I shall forget you presently, my dear,
# So make the most of this, your little day,
# Your little month, your little half a year,
# Ere I forget, or die, or move away,
# script.py

# with open('millay_sonnet.txt') as sonnet_doc:
#   first_line = sonnet_doc.readline()
#   second_line = sonnet_doc.readline()
#   print(second_line)
# This script also creates a file object called sonnet_doc that points to the file millay_sonnet.txt. It then reads in the first line using sonnet_doc.readline() and saves that to the variable first_line. It then saves the second line (So make the most of this, your little day,) into the variable second_line and then prints it out.

# Writing a File
# Reading a file is all well and good, but what if we want to create a file of our own? With Python we can do just that. It turns out that our open() function that we’re using to open a file to read needs another argument to open a file to write to.

# script.py

# with open('generated_file.txt', 'w') as gen_file:
#   gen_file.write("What an incredible file!")
# Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.

# This code creates a new file in the same folder as script.py and gives it the text What an incredible file!. It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.

# Appending to a File
# So maybe completely deleting and overwriting existing files is something that bothers you. Isn’t there a way to just add a line to a file without completely deleting it? Of course there is! Instead of opening the file using the argument 'w' for write-mode, we open it with 'a' for append-mode. If we have a generated file with the following contents:

# generated_file.txt

# This was a popular file...
# Then we can add another line to that file with the following code:

# script.py

# with open('generated_file.txt', 'a') as gen_file:
#   gen_file.write("... and it still is")
# In the code above we open a file object in the temporary variable gen_file. This variable points to the file generated_file.txt and, since it’s open in append-mode, adds the line ... and it still is as a new line to the file. If you were to open the file after running the script it would look like this:

# generated_file.txt

# This was a popular file...
# ... and it still is
# Notice that opening the file in append-mode, with 'a' as an argument to open(), means that using the file object’s .write() method appends whatever is passed to the end of the file in a new line. If we were to run script.py again, this would be what generated_file.txt looks like:

# generated_file.txt

# This was a popular file...
# ... and it still is
# ... and it still is
# Notice that we’ve appended "... and it still is" to the file a second time! This is because in script.py we opened generated_file.txt in append-mode.

# Appending to a File
# So maybe completely deleting and overwriting existing files is something that bothers you. Isn’t there a way to just add a line to a file without completely deleting it? Of course there is! Instead of opening the file using the argument 'w' for write-mode, we open it with 'a' for append-mode. If we have a generated file with the following contents:

# generated_file.txt

# This was a popular file...
# Then we can add another line to that file with the following code:

# script.py

# with open('generated_file.txt', 'a') as gen_file:
#   gen_file.write("... and it still is")
# In the code above we open a file object in the temporary variable gen_file. This variable points to the file generated_file.txt and, since it’s open in append-mode, adds the line ... and it still is as a new line to the file. If you were to open the file after running the script it would look like this:

# generated_file.txt

# This was a popular file...
# ... and it still is
# Notice that opening the file in append-mode, with 'a' as an argument to open(), means that using the file object’s .write() method appends whatever is passed to the end of the file in a new line. If we were to run script.py again, this would be what generated_file.txt looks like:

# generated_file.txt

# This was a popular file...
# ... and it still is
# ... and it still is
# Notice that we’ve appended "... and it still is" to the file a second time! This is because in script.py we opened generated_file.txt in append-mode.

# What's With "with"?
# We’ve been opening these files with this with block so far, but it seems a little weird that we can only use our file variable in the indented block. Why is that? The with keyword invokes something called a context manager for the file that we’re calling open() on. This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block.

# Why is closing the file so complicated? Well, most other aspects of our code deal with things that Python itself controls. All the variables you create: integers, lists, dictionaries — these are all Python objects, and Python knows how to clean them up when it’s done with them. Since your files exist outside your Python script, we need to tell Python when we’re done with them so that it can close the connection to that file. Leaving a file connection open unnecessarily can affect performance or impact other programs on your computer that might be trying to access that file.

# The with syntax replaces older ways to access files where you need to call .close() on the file object manually. We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterwards.

# fun_cities_file = open('fun_cities.txt', 'a')

# # We can now append a line to "fun_cities".
# fun_cities_file.write("Montréal")

# # But we need to remember to close the file
# fun_cities_file.close()
# In the above script we added “Montréal” as a new line in our file fun_cities.txt. However, since we used the older-style syntax, we had to remember to close the file afterwards. Since this is necessarily more verbose (requires at least one more line of code) without being any more expressive, using with is preferred.

# What Is a CSV File?
# Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional parsing library to understand. CSV files are an example of a text file that impose a structure to their data. CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format. A spreadsheet that looks like the following

# Name	Username	Email
# Roger Smith	rsmith	wigginsryan@yahoo.com
# Michelle Beck	mlbeck	hcosta@hotmail.com
# Ashley Barker	a_bark_x	a_bark_x@turner.com
# Lynn Gonzales	goodmanjames	lynniegonz@hotmail.com
# Jennifer Chase	chasej	jchase@ramirez.com
# Charles Hoover	choover	choover89@yahoo.com
# Adrian Evans	adevans	adevans98@yahoo.com
# Susan Walter	susan82	swilliams@yahoo.com
# Stephanie King	stephanieking	sking@morris-tyler.com
# Erika Miller	jessica32	ejmiller79@yahoo.com

# In a CSV file that same exact data would be rendered like this:

# users.csv

# Name,Username,Email
# Roger Smith,rsmith,wigginsryan@yahoo.com
# Michelle Beck,mlbeck,hcosta@hotmail.com
# Ashley Barker,a_bark_x,a_bark_x@turner.com
# Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com
# Jennifer Chase,chasej,jchase@ramirez.com
# Charles Hoover,choover,choover89@yahoo.com
# Adrian Evans,adevans,adevans98@yahoo.com
# Susan Walter,susan82,swilliams@yahoo.com
# Stephanie King,stephanieking,sking@morris-tyler.com
# Erika Miller,jessica32,ejmiller79@yahoo.com
# Notice that the first row of the CSV file doesn’t actually represent any data, just the labels of the data that’s present in the rest of the file. The rest of the rows of the file are the same as the rows in the spreadsheet software, just instead of being separated into different cells they’re separated by… well I suppose it’s fair to say they’re separated by commas.