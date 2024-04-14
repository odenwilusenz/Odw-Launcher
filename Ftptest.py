from ftplib import FTP

ftp = FTP("192.168.42.10")  # Connect to FTP server
ftp.login("anyuser", "Resuyna2")  # Login

initial_directory = ftp.pwd()  # Get initial working directory

# Change directory to 'Launcher/Memes'
ftp.cwd('Launcher/Memes')

# List directory contents
directory_contents = ftp.nlst()
print("Directory contents:")
for item in directory_contents:
    print(item)

# Retrieve image file 'meme1.png' and save it locally
with open('meme1.png', 'wb') as fp:
    ftp.retrbinary('RETR meme1.png', fp.write)

# Change directory back to the initial directory

# Retrieve text file 'test.txt' and print its contents
def print_line(line):
    print(line)




ftp.quit()



ftp = FTP("192.168.42.10")  # Connect to FTP server
ftp.login("anyuser", "Resuyna2")  # Login

initial_directory = ftp.pwd()  # Get initial working directory

# Change directory to 'Launcher/Memes'
ftp.cwd('Launcher/Games')

# List directory contents
directory_contents = ftp.nlst()
print("Directory contents:")
for item in directory_contents:
    print(item)

# Retrieve image file 'meme1.png' and save it locally

# Change directory back to the initial directory

# Retrieve text file 'test.txt' and print its contents
def print_line(line):
    print(line)



with open('test.txt', 'rb') as fp:
    ftp.retrlines('RETR test.txt', callback=print)

ftp.quit()
