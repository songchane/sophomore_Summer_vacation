from Chapter5_Calculator1 import FourCal


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first /self.second


a = SafeFourCal(4,0)
print(a.div())