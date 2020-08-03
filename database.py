class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def cridentiald(self):
        with open("cridentials.txt",'a') as f:
            f.writelines(self.name + "\n")
            f.writelines(str(self.age))
            f.close()
    def cridentiald2(self):
        with open("cridentials.txt",'a') as f:
            f.writelines(self.name +"\n")
            f.writelines(str(self.age))
            f.close()
