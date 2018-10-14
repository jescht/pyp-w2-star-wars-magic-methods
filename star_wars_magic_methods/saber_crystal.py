class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]



    @property
    def color(self):
        return (self.red,self.green,self.blue)
        

    def __eq__(self,other):
        if self.color == other.color: 
            return True
        else:
            return False

    def __add__(self,other):
        if isinstance(other, tuple):
            other=SaberCrystal(color=other)
        
        new_color = [self.color[0] + other.color[0], self.color[1] + other.color[1], self.color[2] + other.color[2]]
        newlist=[]
        for value in new_color: 
            if value> 255:
                value = 255
            newlist.append(value)        

        return SaberCrystal(tuple(newlist))



