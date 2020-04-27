from Gradebook.GradebookClass.gradebook import GradeBook, GradeBookList


def add_rate(id, gbook):
    b_go = True

    while b_go:
        try:
            rate = int(input("Podaj ocene >> "))
            weigth = int(input("Podaj podaj wage >> "))
            gbook.add_rate(id, rate, weigth)
            b_go = False
        except ValueError:
            print("Podana wartosc nie jest liczba")
    print("Ocena zotala przypisana")


def do_operations(gbook):
    id = 0
    check_id = True
    while check_id:
        try:
            gbook.show_all_student()
            id = int(input("Podaj id studenta >> "))
            check = gbook.check_student(id)
            if check:
                check_id = False
            else:
                exit_while = input("Wprowadz 0 zeby wyjsc >> ")
                if exit_while == "0":
                    check_id = False
        except ValueError:
            print("Podana wartosc nie jest liczba")

    select = True
    while select:
        print("\n1. Przypisz ocene oraz wage\n2. Wypis wszystki ocene\n3. Wyjdz")

        choose_op = input("Podaj liczbę >> ")

        if choose_op == "1":
            add_rate(id, gbook)
        elif choose_op == "2":
            gbook.show_all_rate(id)
        elif choose_op == "3":
            select = False
        else:
            print("\nPodany nieprawidłowa wartosc\n")


def gradebook_operation(gradebook_list):
    id = 0
    check_id = True
    while check_id:
        try:
            gradebook_list.show_all_gbook()
            id = int(input("Podaj id dzienik >> "))
            check = gradebook_list.check_gbook(id)
            if check:
                check_id = False
            else:
                exit_while = input("Wprowadz 0 zeby wyjsc >> ")
                if exit_while == "0":
                    check_id = False
        except:
            print("Blad przetwarzania:")
    gbook = gradebook_list.get_gbook(id)
    select = True
    while select:
        print("\n1. Nowy student\n2. Liste studentow\n3. Operacji z studentami\n4. Policz srednia ocene\n5. Wyjdz")
        choose1 = input("Podaj liczbę >> ")
        if choose1 == "1":
            name = input("Podaj imie studenta >> ")
            sure_name = input("Podaj Nazwisko studenta >> ")
            gbook.add_student(name, sure_name)
        elif choose1 == "2":
            gbook.show_all_student()
        elif choose1 == "3":
            do_operations(gbook)
        elif choose1 == "4":
            gbook.calc_avg_ratings()
        elif choose1 == "5":
            select = False
        else:
            print("\nPodany nieprawidłowy znak\n")


def gradebook_clone(gradebook_list):
    check_id = True
    while check_id:
        try:
            gradebook_list.show_all_gbook()
            id = int(input("Podaj id dzienika >> "))
            check = gradebook_list.check_gbook(id)
            if check:
                rm_rate = False
                name = input("Podaj nazwe nowego dzienika>> ")
                s_remove_rate = input("Gdy chcesz usunac oceny to wprowadz 'rm' >> ")
                if s_remove_rate == "rm":
                    rm_rate = True
                gradebook_list.clone_gbook(id, name, rm_rate)
                check_id = False
            else:
                exit_while = input("Wprowadz 0 zeby wyjsc >> ")
                if exit_while == "0":
                    check_id = False
        except ValueError:
            print("Podana wartosc nie jest liczba")


def main():
    gradebook_list = GradeBookList()

    select = True
    while select:
        print("\n1. Nowy dzienik\n2. Lista dzienikow\n3. Operacji\n4. Kopiuj dziennik\n5. Wyjdz")
        choose1 = input("Podaj liczbę >> ")
        if choose1 == "1":
            name = input("Podaj nazwe dzienika >> ")
            gradebook_list.add_gbook(name)
        elif choose1 == "2":
            gradebook_list.show_all_gbook()
        elif choose1 == "3":
            gradebook_operation(gradebook_list)
        elif choose1 == "4":
            gradebook_clone(gradebook_list)
        elif choose1 == "5":
            select = False
        else:
            print("\nPodany nieprawidłowy znak\n")


if '__main__' == __name__:
    main()
