import copy


class GradeBookList:
    def __init__(self):
        self.__gradebook_list = []

    def add_gbook(self, name):
        name = name.strip()
        if name == "" or name is None:
            return
        st_count = len(self.__gradebook_list)
        gradebook = GradeBook(st_count + 1, name)
        self.__gradebook_list.append(gradebook)

    def show_all_gbook(self):
        for entry in self.__gradebook_list:
            print(f"ID: {entry.get_id} nazwa: {entry.get_name}")

    def clone_gbook(self, id, name, b_remove_rate):
        for entry in self.__gradebook_list:
            if entry.get_id == id:
                new_gbook = copy.deepcopy(entry)
                if b_remove_rate:
                    new_gbook.remove_all_rate()
                st_count = len(self.__gradebook_list)
                new_gbook.set_id = st_count + 1
                new_gbook.set_name = name
                self.__gradebook_list.append(new_gbook)

    def check_gbook(self, id):
        check = False
        for i in self.__gradebook_list:
            if i.get_id == id:
                check = True
        return check

    def get_gbook(self, id):
        for g in self.__gradebook_list:
            print(f'Nazwe: {g.get_name}')
            if g.get_id == id:
                return g


class GradeBook:
    def __init__(self, id, name):
        self.__student_list = []
        self.__gbook_name = name.strip()
        self.__gbook_id = id

    @property
    def get_list(self):
        return self.__student_list

    @get_list.setter
    def set_list(self, value):
        self.__student_list = value

    @property
    def get_id(self):
        return self.__gbook_id

    @get_id.setter
    def set_id(self, value):
        self.__gbook_id = value

    @property
    def get_name(self):
        return self.__gbook_name

    @get_name.setter
    def set_name(self, value):
        self.__gbook_name = value

    def check_student(self, id):
        check = False
        for i in self.__student_list:
            print(f'Imie: {i.get_name}')
            if i.get_id == id:
                check = True
        return check

    def add_student(self, name, surename):
        st_count = len(self.__student_list)
        student = Student(name, surename, st_count + 1)
        self.__student_list.append(student)

    def show_all_student(self):
        for entry in self.__student_list:
            print(f"ID: {entry.get_id} Imie: {entry.get_name} Nazwisko: {entry.get_surename}")

    def show_all_rate(self, id):
        for i in self.__student_list:
            if i.get_id == id:
                for rate in i.get_rate_list:
                    print(f"Ocena: {rate.get_rate} Waga: {rate.get_weigth}")

    def calc_avg_ratings(self):
        for i in self.__student_list:
            avg = 0
            total = 0
            rate_list = i.get_rate_list
            for ele in range(0, len(rate_list)):
                total = total + rate_list[ele].get_rate
            if total == 0:
                avg = 'niema ocen'
            else:
                avg = total/len(rate_list)
            print(f'Student {i.get_name} {i.get_surename}\r\nMa srednia ocene: {avg}')

    def add_rate(self, id, rate, weigth):
        for i in self.__student_list:
            if i.get_id == id:
                i.add_rate(rate, weigth)

    def remove_all_rate(self):
        for i in self.__student_list:
            i.remove_rate()


class Student:
    __name = ""
    __surename = ""
    __student_id = 0

    def __init__(self, name, surename, id):
        self.__student_id = id
        self.__name = name.replace(" ", "")
        self.__surename = surename.replace(" ", "")
        self.__rat_list = []

    def add_rate(self, rate, weigth):
        rating = Rating(rate, weigth)
        self.__rat_list.append(rating)

    def remove_rate(self):
        self.__rat_list.clear()

    @property
    def get_rate_list(self):
        return self.__rat_list

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, value):
        self.__name = value

    @property
    def get_surename(self):
        return self.__surename

    @get_surename.setter
    def set_surename(self, value):
        self.__surename = value \

    @property
    def get_id(self):
        return self.__student_id

    @get_id.setter
    def set_id(self, value):
        self.__student_id = value


class Rating:
    rate = 0
    weigth = 0

    def __init__(self, rate, weight):
        self.__rate = rate
        self.__weigth = weight

    @property
    def get_rate(self):
        return self.__rate

    @get_rate.setter
    def set_rate(self, value):
        self.__rate = value

    @property
    def get_weigth(self):
        return self.__weigth

    @get_weigth.setter
    def set_weigth(self, value):
        self.__weigth = value