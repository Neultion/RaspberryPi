f = open("output.txt","w")
for i in range(1,7):
    data = f"Line {i}\n"
    f.write(data)
f.close()