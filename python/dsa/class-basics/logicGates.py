class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None
    
    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"--> "))
        return self.pin_a.get_from().get_output()
    
    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"--> "))
        return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None
    
    def get_pin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"--> "))
        return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, lb1):
        super().__init__(lb1)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 and b == 1:
            return 1
        return 0

class OrGate(BinaryGate):

    def __init__(self, lb2):
        super().__init__(lb2)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 0 and b == 0:
            return 0
        return 1

class NotGate(UnaryGate):

    def __init__(self, lb3):
        super().__init__(lb3)

    def perform_gate_logic(self):
        a = self.get_pin()

        return 1 if a == 0 else 0

class Connector:
    
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        
        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate



g1 = AndGate("G1")
g2 = OrGate("G2")
g3 = NotGate("G3")


print(g3.get_output())

