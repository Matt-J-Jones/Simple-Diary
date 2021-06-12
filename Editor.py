from datetime import datetime

def Filename_Date():
    global formatted_date
    date = datetime.now()
    formatted_date=(date.strftime("%a, %d %B %Y. %H:%M:%S"))
    print(formatted_date)
def newEntry():
    Filename_Date()
    #filename_Name=input("Enter Filename: ")
    subject=input("""
    Enter Post Title: 
    >""")
    if subject=="":
        subject="<No Subject>"
    else:
        subject=subject
    post=input("""
    Enter Text to Post:
    >""")
    f=open("./Logbook.txt", "a+")
    f.write(formatted_date)
    f.write("\n")
    f.write("Subject: "+subject)
    f.write("\n")
    f.write("Body: "+post)
    f.write("\n")
    f.write("\n")
    f.close()

newEntry()
