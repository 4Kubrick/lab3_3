class GradeBook:
    def __init__(self):
        self.__student_list = []

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
                    print(f"Ocena: {rate.get_rate} Waga: {rate.get_weight}")

    def calc_avg_ratings(self, id):
        for i in self.__student_list:
            if i.get_id == id:
                rate_list = i.get_rate_list
                sum_rate = sum(rate_list, axis=0)
                print(f'Srednia: {sum_rate/len(rate_list)}')

    def add_rate(self, id, rate, weigth):
        for i in self.__student_list:
            if i.get_id == id:
                i.add_rate(rate, weigth)


class Student:
    __name = ""
    __surename = ""
    __student_id = 0

    def __init__(self, name, surename, id):
        self.__student_id = id
        self.__name = name
        self.__surename = surename
        self.__rat_list = []

    def add_rate(self, rate, weigth):
        rating = Rating(rate,weigth)
        rating.set_rate(rate)
        self.__rat_list.append(rating)

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