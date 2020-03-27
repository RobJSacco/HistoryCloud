

# Create class with the following methods:
# frequency_data.add(Keyword, Count) Adds a new keyword and count to the object
# frequency_data.Keyword() Returns an list array containing Keywords so that frequency_data.Keyword()[0] is the first keyword in the list
# FrequencyData.Count() Returns an int array of frequency counts so that frequency_data.Count()[0] is the frequency count corresponding to FrequencyData.Keyword()[0]
#
# Create src/test/python/test_frequency_data.py to test the class and provide dummy data


# Python Dictionary function and list used to create class

class FrequencyData:

    def __init__(self, Keyword, num):
        self.freqdict = {Keyword: num}

    # The following function will add a given keyword and count to the list. If the Keyword existed previously in the list
    # The new count value is added to the old one. Conversly, if the keyword did not originally exist in the list, it will
    # be added with the associated count value.
    def add(self, Keyword, num):
        if Keyword in self.freqdict:
            self.freqdict[str(Keyword)] += num
        else:
            self.freqdict[str(Keyword)] = num

    # The following function will a list of the keywords in the freqdict dictionary.
    def Keywords(self):
        return list(self.freqdict.keys())

    # The following function will a list of the keywords in the freqdict dictionary.

    def Count(self):
        return list(self.freqdict.values())


p1 = FrequencyData("Grant", 1)
p1.add("Nate", 25)
p1.add("Rob", 305)
p1.add("Grant", 4)
p1.add("Nate", 15)
p1.add("Grant", 4040)

print(p1.freqdict)
print(p1.Keywords()[0])
print(p1.Count()[0])

