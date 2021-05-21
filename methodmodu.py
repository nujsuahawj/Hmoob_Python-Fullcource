class nujsua:
    def __init__(self,name,anmo):
        self.name=name
        self.anmo=anmo
    def add_anmo(self,anmo):
        if self.anmo +anmo <=10:
            self.anmo+=anmo
    def fire_anmo(self):
        if self.anmo >0:
            self.anmo -=1