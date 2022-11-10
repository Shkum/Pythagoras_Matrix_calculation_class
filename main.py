class Pythagoras:
    def __init__(self, b_day, b_month, b_year):
        self.variables = {}
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year

    def get_pythagoras(self):
        calc_str = (self.b_day + self.b_month + self.b_year).replace('0', '')
        first_num = sum(map(int, calc_str))
        second_num = sum(map(int, str(first_num)))
        third_num = first_num - int(self.b_day.lstrip('0')[0]) * 2
        forth_num = sum(map(int, str(third_num)))
        final_string = (calc_str + str(first_num) + str(second_num) + str(third_num) + str(forth_num)).replace('0', '')
        self.variables['embodiment'] = len(final_string)
        self.variables['first_num'] = first_num
        self.variables['second_num'] = second_num
        self.variables['third_num'] = third_num
        self.variables['forth_num'] = forth_num
        nums = []
        for i in range(1, 10):
            nums.append(final_string.count(str(i)) * str(i))

        return nums


a = Pythagoras('26', '06', '1979')
print(a.get_pythagoras())
print(a.variables)
