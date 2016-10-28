from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()

prompt = raw_input("Do you want to close your files(y/n): ")

if prompt == 'y':
    print "Closing the filename %s:" %filename
    txt.close()

else:
    print "File still open"