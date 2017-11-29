from shutil import copyfile
import sys

source = input("Enter source file with full path: ")
target = input("Enter target file with full path: ")

# Adding exception handling
try:
    copyfile(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
    exit(1)
except:
    print("Unexpected error: ", sys.exc_info())

print("\nFile copy done!\n")

while True:
    print("Do you like to print the file ? (y/n) : ")
    check = input()
    if check == 'n':
        break
    elif check == 'y':
        file = open(target, 'r')
        print("\nHere follows the file content:\n")
        print(file.read())
        file.close()
        break
    else:
        continue