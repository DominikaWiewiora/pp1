with open("MeatAndFish.txt","r") as f1:
    content1=f1.read()
with open("GrainsAndBread.txt","r") as f2:
    content2=f2.read()
with open("allproducts.txt", "w") as file:
    file.write(content1+content2)
