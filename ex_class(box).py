class Box:
    length=0
    width=0
    height=0


    def getLongestSide(self) :
        self.max = self.length
        if self.width > self.max :
            self.max = self.width
        if self.height > self.max :
            self.max = self.height
        return self.max

    def getShortestSide(self) :  
        self.min = self.length
        if self.min > self.width:
            self.min = self.width
        if self.min > self.height:
            self.min = self.height
        return self.min
        



box1 = Box()
dimensions = input("Enter box1's dimensions ex. 1 2 3").split()
box1.length = int(dimensions[0])
box1.width = int(dimensions[1])
box1.height = int(dimensions[2])
                
box2 = Box()
dimensions = input("Enter box2's dimensions ex. 1 2 3").split()
box2.length = int(dimensions[0])
box2.width = int(dimensions[1])
box2.height = int(dimensions[2])

    

        
def canBox1FitInBox2(box1, box2) :
    if box1.getLongestSide() < box2.getShortestSide():
        return True
    else:
        return False

    
    

if canBox1FitInBox2(box1,box2) == True :
    print("box1 will fit in box2")
else :
    print("box1 wont fit in box2")   