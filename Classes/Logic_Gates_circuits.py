class LogicGate:
    
    def __init__(self,n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label
        
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
        
    
class BinaryGate(LogicGate):
    
    def __init__(self,n):
        LogicGate.__init__(self,n)
        
        self.PinA = None
        self.PinB = None
        
    def getPinA(self):
        if self.PinA == None:
            return int(input("Enter Pin A input for gate "+ \
            self.getLabel()+"->"))
            
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.PinB == None:
            return int(input("Enter Pin B input for gate "+\
            self.getLabel()+"-->"))
            
        else:
            return self.PinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.PinA == None:
            self.PinA = source
        else:
            if self.PinB == None:
                self.PinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
                

class UnaryGate(LogicGate):
    
    def __init__(self,n):
        LogicGate.__init__(self,n)
        
        self.Pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        
        
class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a==1 and b==1:
            return 1
        else:
            return 0
            
        
class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a==1 or b==1:
            return 1
        else:
            return 0
            

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
        
    def performGateLogic(self):
        a = self.getPin()
        
        if a == 1:
            return 0
        else:
            return 1

class NandGate(AndGate):

    def performGateLogic(self):
        if super(AndGate).performGateLogic() == 1:
            return 0
        
        else:
            return 1


class NorGate(OrGate):

    def performGateLogic(self):
        if super(NorGate).performGateLogic() == 1:
            return 0
        else:
            return  1


class Connector:
    def __init__(self,fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.setNextPin(self)
        
    def getFrom(self):
        return self.fromgate
        
    def getTo(self):
        return self.togate

            
def main():
    g1 = AndGate("G1")
    print g1.getOutput()
    
    g2 = OrGate("G2")
    print g2.getOutput()
    
    g3 = NotGate("G3")
    print g3.getOutput()
    
    c1 = Connector(g1,g2)
    print c1

    g4 = NorGate("G4")
    print g4.getOutput()
    
main()
        
   
        
    
        
        
        
    

    
        
        
    