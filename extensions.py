x = input("File name: ").strip().lower()
delimiter = x.split('.')
y = delimiter[-1]
if y == "jpg" or y == "jpeg":
    print("image/jpeg")
elif y == "txt":
    print("text/plain")
elif y == "gif":
    print("image/gif")
elif y == "pdf":
    print("application/pdf")
elif y == "zip":
    print("application/zip")
elif y == "png":
    print("image/png")
else:
    print("application/octet-stream")


