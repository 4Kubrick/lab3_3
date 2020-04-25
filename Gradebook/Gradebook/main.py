from Gradebook.GradebookClass.gradebook import GradeBook


def do_operations(gbook):

    id = 0
    check_id = True
    while check_id:
        gbook.show_all_student()
        id = int(input("Podaj id studenta >> "))
        check = gbook.check_student(id)
        if check:
            check_id = False
        else:
            exit_while = input("Wprowadz 0 zeby wyjsc >> ")
            if exit_while == "0":
                check_id = False

    select = True
    while select:
        #try:
            print("\n1. Przypisz ocene oraz wage\n2. Wypis wszystki ocene\n3. Wyjdz")

            choose_op = input("Podaj liczbę >> ")

            if choose_op == "1":
                rate = int(input("Podaj ocene >> "))
                weigth = int(input("Podaj podaj wage >> "))
                gbook.add_rate(id, rate, weigth)
            elif choose_op == "2":
                gbook.show_all_rate(id)
            elif choose_op == "3":
                select = False
            else:
                print("\nPodany nieprawidłowa wartosc\n")
        #except:
            #print("Blad przetwarzania:")
            #select = False


def main():
    gbook = GradeBook()
    select = True
    while select:
        #try:
            print("\n1. Dodaj nowego studenta\n2. Pokaz liste studentow\n3. Przeprowadz operazji z danymi studentow\n4. Policz srednia ocene\n5. Wyjdz")
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
        #except:
            #print("Blad przetwarzania:")
            #select = False




if '__main__' == __name__:
    main()