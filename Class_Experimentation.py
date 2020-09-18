# Just code of me playing around with classes
class Num():
    global nums, random, n
    def __init__(self,n=1):
        self.len = n*100
        self.nums = [x for x in range(self.len)]
    def nums_samp(self, n = None):
        if n == None:
            n = self.len
        print(random.sample(self.nums,n))
        return random.sample(self.nums,n)
    def first_nums(self, n = None):
        if n == None:
            n = self.len
        print(self.nums[:n])
        return self.nums[:n]

artist = ['Human Abstract', 'Miles Davis', 'Jacob Collier']
song = ['Zenith', 'Love For Sale', 'Hideaway']
rating = [7, 6, 10]
tuples = list(map(lambda x: list(x), list(zip(artist, song, rating))))
#print(tuples)

class Music():
    def __init__(self, n = [0,1,2], c = tuples):
        if type(n) == int:
            n = [n]
        self.artist = [c[e][0] for e in n]
        self.song = [c[e][1] for e in n]
        self.rating = [c[e][2] for e in n]
        self.tuple = [c[e] for e in n]
    def read_tuple(self):
        list_comp = ["Artist : {}, Song: {}, Rating: {}" \
            .format(elem[0], elem[1], elem[2])  \
            for elem in self.tuple]
        return "\n".join(list_comp)
    def evaluate(self):
        ev = ["{} = Good ".format(elem) if elem > 7 else "{} = Not Good".format(elem) for elem in self.rating]
        return "\n".join(ev)
    def add_rating(self,x,y):
        return Music(x).rating[0] + Music(y).rating[0]
    def rat(self):
        return self.rating[0]
#print(Music().add_rating(0,1))
#print(Music(2).rat())

L = [
    Music(0),
    Music(1),
    Music(2)
]

class People():
    global names, births
    names = []
    def __init__(self,namey = None,year_born = None,current_year = 2020,knowledge = 0):
        self.name = namey
        self.born = year_born
        self.current = current_year
        self.know = knowledge
        if self.name != None:
            names.append(self)
    def get_age(self):
        return self.current - self.born
    def get_names(self):
        gnames = [x.name for x in names]
        #print("list of size: {}".format(len(names)))
        return gnames
    def __str__(self):
        return "{} : {}".format(self.name,self.born)
    def search(self,n):
        for elem in names:
            if elem.name == n:
                return elem

class Student(People):
    global namesy
    namesy = []
    def __init__(self,name=None, year_born = None):
        People.__init__(self, name, year_born, current_year=2020, knowledge=0)
        if self.name != None:
            namesy.append(self)
    def studied(self, n = 0):
        self.know += n
        return self
    def get_names(self):
        gnames = [x.name for x in namesy]
        # print("list of size: {}".format(len(names)))
        return gnames
    def search(self,n):
        for elem in namesy:
            if elem.name == n:
                return elem

class Staff(People):
    global namesyy
    namesyy = []
    def __init__(self,name=None, year_born = None):
        People.__init__(self, name, year_born, current_year=2020, knowledge=0)
        if self.name != None:
            namesyy.append(self)
    def get_names(self):
        gnames = [x.name for x in namesyy]
        # print("list of size: {}".format(len(names)))
        return gnames


for elem in names:
    print(elem.know)

class dudes():
    global namesyyy
    namesyyy = []
    def __init__(self, name = None, year_born = None):
        self.name = name
        self.born = year_born
        if self.name != None:
            namesyyy.append(self)
    def get_names(self):
        gnames = [x.name for x in namesyyy]
        # print("list of size: {}".format(len(names)))
        return gnames

B = People("Alice",1994)
A = Student("Tony",1994).studied(4)
E = Student("Sully",1984).studied(6)
C = Staff("Reginald",1970)
D = dudes("Mike",1990)

class Society():
    global membe
    membe = []
    def __init__(self,member = 'Jeff'):
        self.member = member
    def add(self,new_membs):
        for elem in new_membs:
            membe.append(elem)
        #return membe
    def members(self):
        return membe

Society().add(dudes().get_names())
Society().add(Student().get_names())
print(Society().members())
