


class Car:
    color: str = 'White' #Выбираем цвет автомобиля. В данном примере цвет ЧЕРНЫЙ
    power: int =  750 #мощность двигателя лошадиные силы
    m_topl: int = 40 #Запас бенза
    ras_topl: float = 1 #значения расхода топлива на 1 километр
    topl_isn: float = 0 #изначальное значение топлива в баке
    seats: int = 4 #Количество сидуушек

    def __init__ (self, color:str = 'White', power: int = 666, m_topl: float = 989, ras_topl = 23, topl_isn = 2, seats = 4):
        self.color = color
        self.power = power
        self.m_topl = m_topl
        self.ras_topl = ras_topl
        self.topl_isn = topl_isn
        self.seats = seats

    def set_color(self, color):
        """
        Данная функция позволяет установить значение цвета для автомобиля
        """
        self.color = color
        return self.color


    def get_color(self):
        """
        Даннная функция позволяет вывести на экран значение цвета, который установлен для автомобиля
        """
        return self.color
    def set_m_topl(self, m_topl):
        """
        Данная функция позволяет изменить количество топлива
        """

        self.m_topl = m_topl
        return self.m_topl
    
    def get_max_fuel(self):
        '''
        Функция выводит максимальное значение топлива
        '''
        return self.m_topl

    def get_fuel(self): 
        """
        Получаем значение топлива на данный момент
        """
        return self.topl_isn
    

    def get_ras(self):
        '''
        Данная функция позволяет вывести расход топлива
        '''
        return self.ras_topl

    def get_refill(self):
        ''' 
        В данной функции получаем значение возможности заправки топливом
        '''
        return self.m_topl - self.topl_isn

    def refill(self, topl):
        """
        Функция дозаправки и обработчик перелива 
        """
        if self.m_topl >= self.topl_isn:
            if topl > c.get_refill():
                print('Бак уже полон, больше нельзя')
            else:
                self.topl_isn += topl
                return self.topl_isn
        else:
            print('Дозаправка не требуется')

    def true_distance(self):
        return self.topl_isn / self.ras_topl
    
    def get_seats(self):
        return self.seats
    
    def set_seats(self, seats):
        self.seats = seats
        return self.seats

# проверки
def test_init1():
    Car(color = 'White', power = 3030, m_topl = 80, ras_topl = 4, topl_isn = 11)
def test_init2():
    Car(color = "White")
def test_color1():
    c = Car(color = 'White', power = 3030, m_topl = 80, ras_topl = 4, topl_isn = 11)
    assert c.get_color() == 'White'
def test_color2():
    c = Car(color = 'White', power = 3030, m_topl = 80, ras_topl = 4, topl_isn = 11)
    assert c.get_color() == 'White'
    c.set_color('red')
def test_color3():
    c = Car(color = 'White', power = 3030, m_topl = 80, ras_topl = 4, topl_isn = 11)
    assert c.get_color() == 'White'
    c.set_color('red')

    assert c.get_color() == 'red'

def test_1():
    c = Car()
    assert c.get_seats() == 4
    c.set_seats(5) 
    assert c.get_seats() == 5

#вызовы функции проверок 
test_init2()
test_init1()
test_color1()
test_color2()
test_color3()
test_1()



c = Car(color = 'White', power = 3030, m_topl = 80, ras_topl = 4, topl_isn = 11, seats = 5)
#блок вывода результатов
print('Цвет машины:', c.get_color())
print('Объём бака:', c.get_fuel())
print(f'У тебя запас топлива {c.get_fuel()} с ним можно проехать {c.true_distance()}')
print('количество сидений')
input('Нажмите Enter, чтобы продолжить...')
c.set_color('Yellow')
c.set_m_topl(90)
print(f'Новый окрас автомобиля {c.get_color()}')
print(f'Максимальная вместимость бака {c.get_max_fuel()} литров')
print(f'Сейчас в баке залито {c.topl_isn} литров')
print(f'Возможно заправиться на {c.get_refill()} литров')
c.refill(88)
print(f'Можно проехать {c.true_distance()}')

input('Нажмите Enter, чтобы продолжить...')