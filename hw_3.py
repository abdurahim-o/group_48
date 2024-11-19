class Computer:

    def __init__(self,memory,cpu):
        self.__memory = memory
        self.__cpu = cpu

    def __str__(self):
        return f'CPU: {self.__cpu}, memory: {self.__memory}'

    @property
    def memory(self):
        return (self.__memory)

    @property
    def cpu(self):
        return (self.__cpu)

    @memory.setter
    def memory(self,value):
        self.__memory = value

    @cpu.setter
    def cpu(self,value):
        self.__cpu = value


    def make_computations(self):
        return self.__memory * self.__cpu

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    def __str__(self):
        return f'sim_card_list: {self.__sim_card_list}'

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self,value):
        self.__sim_card_list = value

    def cell(self,sim_card_number, call_to_number):

        if sim_card_number ==1:
            return (f" Идет звонок на номер {call_to_number} с сим карты - {sim_card_number} - {self.__sim_card_list[0]}")

        elif sim_card_number == 2:
            return (f" Идет звонок на номер {call_to_number} с сим карты - {sim_card_number} - {self.__sim_card_list[1]}")

class Smartphone(Computer,Phone):

    def __init__(self,memory,cpu,sim_card_list):
        Computer.__init__(self,memory,cpu)
        Phone.__init__(self,sim_card_list)




    def use_gps(self,location):
        print(f"Чтобы дойти до {location}, сядтье на автобус 51\n"
              f"выйти на остановке 'Третьяковский'\n"
              f"пройти на восток по улице 'Койбагарова'\n"
              f"на перекрестке пройти налево. Вы дошли до пункта назначение {location}")
    def __str__(self):
        return super().__str__() + f' ,sim_card_list: {self.sim_card_list}'



acer = Computer(64,16)
nokia = Phone(["'Beeline", "Megacom"])
pocox3 = Smartphone(32,8,["0","Megacom" ])
iphone = Smartphone(86,6,["Beeline", "Megacom"])


print(acer)
print(nokia)
print(pocox3)
print(iphone)


pocox3.use_gps("Спорт зал 'ЛЕОНИК'")
print(f'func make_computations : {acer.make_computations()}')
print(nokia.cell(1,"+9969997120220"))
print(nokia.cell(2,"=9969997120220"))

print(acer > iphone)
print(acer < iphone)
print(iphone <= pocox3)
print(acer >= pocox3)
print(pocox3 != acer)
print(iphone == iphone)