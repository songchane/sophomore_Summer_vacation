from Chapter5_Calculator1 import FourCal

class FourCal:
    class MoreFourCal(FourCal):
        def pow(self):
            result = self.first ** self.second
            return result

    # a = MoreFourCal(4,2)
    # print(a.pow())
    # print(a.add())

