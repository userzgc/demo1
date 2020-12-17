try:
    f = open(r"C:\Users\Administrator\PycharmProjects\demo1\file\send.txt","r")
    # f.write("zhang")
    print(f.read())

except IOError as e:
    print(e)


