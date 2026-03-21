class emp:
    def calc_salary(self,salary):
        print("Employee salary:",salary)

class manager(emp):
    def calc_salary(self, salary):
        bouns = salary * 0.20
        total = salary + bouns
        print("Manager salary with bonus:",total)

e = emp()
m = manager()

e.calc_salary(200)
m.calc_salary(200)