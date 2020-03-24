

# Create class with the following methods:
# FrequencyData.add(Keyword, Count) Adds a new keyword and count to the object
# FrequencyData.Keyword() Returns an list array containing Keywords so that FrequencyData.Keyword()[0] is the first keyword in the list
# FrequencyData.Count() Returns an int array of frequency counts so that FrequencyData.Count()[0] is the frequency count corresponding to FrequencyData.Keyword()[0]
#
# Create src/test/python/TestFrequencyData.py to test the class and provide dummy data


# Python Dictionary function and list used to create class

class FrequencyData:

    def __init__(self, Keyword, Count):
        self.freqdict = {Keyword: Count}

    # The following function will add a given keyword and count to the list. If the Keyword existed previously in the list
    # The new count value is added to the old one. Conversly, if the keyword did not originally exist in the list, it will
    # be added with the associated count value.
    def add(self, Keyword, Count):
        if Keyword in self.freqdict:
            self.freqdict[str(Keyword)] += Count
        else:
            self.freqdict[str(Keyword)] = Count

    # The following function will a list of the keywords in the freqdict dictionary.
    def Keywords(self):
        return list(self.freqdict.keys())

    # The following function will a list of the keywords in the freqdict dictionary.

    def Counts(self):
        return list(self.freqdict.values())


p1 = FrequencyData("Corona", 1)
p1.add("Trump", 25)
p1.add("White House", 305)
p1.add("Corona", 4)
p1.add("China", 15)
p1.add("Corona", 4000)

print(p1.freqdict)
print(p1.Keywords()[0])
print(p1.Counts()[0])

