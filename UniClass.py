class UniversityPeeps:

    def __init__(self,n):

        self.name =  n

    def get_ID(self):

        self.id = int(input("Provide your ID number: "))

    def get_DoB(self):

        self.DoB = input("Provide your Date of Birth: ")

    def get_Gender(self):

        self.Gender = input("Provide your Gender: ")



class Academic(UniversityPeeps):

    def __init__(self,n):

        super(Academic, self).__init__(n)

        self.name = n
        self.mentees = []


    def get_Module(self):

        self.module = input("What are you teaching? ")



    def get_Mentee(self, mentee):

        mentees.append(mentee)

    def show_Students(self):

        actual = []

        for connection in mentees:

            actual.append(connection.show_Student())











class Students(UniversityPeeps):

    def __init__(self,n):

        super(Students, self).__init__(n)

        self.name =  n




    def get_Module(self):

        self.modules = []

        while True:

            current = input("What are you taking? Type done when finished. ")

            if current not in {"done", "Done"}:

                self.modules.append(current)

            else:

                break






class PGR(Students):

    def __init__(self,n):

        super(Students, self).__init__(n)

        self.name =  n


        self.mentor = None

    def get_Mentor(self, source):

        if self.mentor == None:

            self.mentor = source

        else:

            raise RuntimeError("Error: Mentor already assigned.")

    def show_Mentor(self):

        mentor.show_Mentor()




class UG(Students):

    def __init__(self,n):

        super(Students, self).__init__(n)

        self.name =  n



class Connect:

    def __init__(self, m, s):

        self.mentor = m

        self.student = s

        #connection = (m,s)

        s.get_Mentor(self)

        m.get_Mentee(self)

    def show_Mentor(self):

        return self.mentor

    def show_Student(self):

        return self.student
