import os, sys, time

print''' 

# By: AM7  
'''
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/Emails.txt"

def getSize(filename):
    st = os.stat(filename)
    return st.st_size


ch = 'y'
while ch == 'y' or ch == 'Y':
    i = 0
    Doiman = raw_input("Enter The Domain Name: ")
    if os.path.exists(filename):
        emails = open(filename, "r")
    else:
        print 'Emails.txt not Found !!!!'
        time.sleep(10)
        break

    icloud = open(str(Doiman) + ".txt", "a")

    for email in emails:
        if str(Doiman) in email.split('@')[1]:
            i = i+1
            icloud.write(email)

    emails.close()
    icloud.close()
    if getSize(icloud.name) <= 0:
        os.remove(icloud.name)
        print 'Not Found Any Item \n'
    else:
        print 'Found: '+str(i)+' times'
    ch = raw_input("Enter (y OR Y) To Continue: ")
