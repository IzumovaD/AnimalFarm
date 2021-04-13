import math
import random
import copy
from enum import Enum
import constants as const


class EndSimulation(Enum):
    SUCCESS = 0
    BANKRUPT = 1
    ANIMALS_ARE_ENDED = 2
    CONTRACT_ENDED = 3


class Experiment:
    def __init__(self):
        self.money = const.default_money
        self.curr_animals = copy.deepcopy(const.default_curr_animals)
        self.curr_feed = const.default_curr_feed
        self.years = const.default_years
        self.feed_for_purchase = const.default_feed_for_purchase
        self.feed_price = const.default_feed_price
        self.animals_for_sale = copy.deepcopy(const.default_animals_for_sale)
        self.animals_price = copy.deepcopy(const.default_animals_price)
        self.forfeit = const.default_forfeit
        
    def create_farm_contract(self):
        self.farm = Farm(self.money, self.curr_animals, self.curr_feed,
                         self.animals_price)
        self.contract = Contract(self.years, self.feed_for_purchase,
                                 self.feed_price, self.animals_price,
                                 self.animals_for_sale, self.forfeit)
            
    def get_details(self):
        string = ""
        string += "Текущий год контракта: " +\
                    str(self.years - self.contract.years) + "-й\n"
        string += "Денежный капитал: " + str(self.farm.money) + "\n"
        string += "Общий капитал: " + str(self.farm.capital) + "\n"
        string += "Выплачено неустойки за год: " +\
                    str(self.farm.paid_forfeit) + "\n"
        string += "За год от нехватки корма умерло:\n"
        string += "Молодых животных: " +\
                    str(self.farm.animals.died_of_hunger["young"]) + "\n"
        string += "Взрослых животных: " +\
                    str(self.farm.animals.died_of_hunger["adult"]) + "\n"
        string += "Старых животных: " +\
                    str(self.farm.animals.died_of_hunger["old"]) + "\n"
        string += "За год от неблагоприятных условий умерло:\n"
        string += "Молодых животных: " +\
                    str(self.farm.animals.died_of_UC["young"]) + "\n"
        string += "Взрослых животных: " +\
                    str(self.farm.animals.died_of_UC["adult"]) + "\n"
        string += "Старых животных: " +\
                    str(self.farm.animals.died_of_UC["old"]) + "\n"
        string += "За год продано:\n"
        string += "Молодых животных: " +\
                    str(self.farm.animals.sold_animals["young"]) + "\n"
        string += "Взрослых животных: " +\
                    str(self.farm.animals.sold_animals["adult"]) + "\n"
        string += "Старых животных: " +\
                    str(self.farm.animals.sold_animals["old"]) + "\n"
        string += "Текущее количество животных на ферме:\n"
        string += "Молодых животных: " +\
                    str(self.farm.animals.animals["young"]) + "\n"
        string += "Взрослых животных: " +\
                    str(self.farm.animals.animals["adult"]) + "\n"
        string += "Старых животных: " +\
                    str(self.farm.animals.animals["old"]) + "\n"
        string += "Корм в наличии: " + str(round(self.farm.feed, 2)) + "\n"
        string += "Оставшийся период контракта: " +\
                    str(self.contract.years) + "\n" 
        return string

    def step(self):
        #обновление данных за год
        self.farm.update_stat()
        #закупка корма
        self.farm.feed_buying(self.contract.feed_price,
                              self.contract.feed_for_purchase,
                              self.contract.forfeit)
        #изменение числа животных
        self.farm.animals_update()
        #продажа животных
        flag = self.farm.animals_sale(self.contract.animals_price,
                                      self.contract.animals_for_sale,
                                      self.contract.forfeit)
        #перерасчёт капитала
        self.farm.capital_update(self.contract.animals_price)
        #обновление контракта
        self.contract.contract_update()
        #вывод статистики
        string = self.get_details()
        if (flag == "BANKRUPT" or flag == "ANIMALS_ARE_ENDED" or
            self.contract.years == 0):
            string += "Прибыль за весь срок контракта составила: " +\
                       str(self.farm.capital - self.farm.init_capital) + "\n"
        if self.contract.years == 0:
            return EndSimulation.CONTRACT_ENDED.name, string
        return flag, string
        
   
class Farm:
    def __init__(self, money, curr_animals, curr_feed, animals_price):
        self.animals = Animals(curr_animals)
        self.money = money
        self.feed = curr_feed
        self.capital = money
        for key in curr_animals:
            self.capital += curr_animals[key]*animals_price[key]
        #изначальный капитал
        self.init_capital = self.capital
        #выплаченная за год неустойка
        self.paid_forfeit = 0

    #обновление статистических данных за год
    def update_stat(self):
        self.paid_forfeit = 0
        self.animals.died_of_hunger = {"young": 0, "adult": 0, "old": 0}
        self.animals.died_of_UC = {"young": 0, "adult": 0, "old": 0}
        self.animals.sold_animals = {"young": 0, "adult": 0, "old": 0}
        
    def animals_sale(self, animals_price, animals_for_sale, forfeit):
        #продажа по контракту
        for key in self.animals.animals:
            #животных в наличии хватает для продажи
            if animals_for_sale[key] <= self.animals.animals[key]:
                #продаём животных
                self.money += animals_for_sale[key] * animals_price[key]
                self.animals.animals[key] -= animals_for_sale[key]
                self.animals.sold_animals[key] += animals_for_sale[key] 
            #животных в наличии не хватает
            else:
                #продаём всё то, что есть
                self.money += self.animals.animals[key] * animals_price[key]
                #платим неустойку за каждое непроданное животное
                self.money -= forfeit * (animals_for_sale[key]-self.animals.animals[key])
                self.paid_forfeit += forfeit * (animals_for_sale[key]-self.animals.animals[key])
                self.animals.sold_animals[key] += self.animals.animals[key]
                self.animals.animals[key] = 0
        #если в минусе
        if self.money <= 0:
            #пробуем продавать больше животных
            while self.money <= 0 and any(elem > 0 for elem in self.animals.animals.values()):
                #сначала продаём старых животных
                if self.animals.animals["old"] > 0:
                    self.money += animals_price["old"]
                    self.animals.animals["old"] -= 1
                    self.animals.sold_animals["old"] += 1
                #потом молодых
                if self.money <= 0 and self.animals.animals["young"] > 0:
                    self.money += animals_price["young"]
                    self.animals.animals["young"] -= 1
                    self.animals.sold_animals["young"] += 1
                #в последнюю очередь взрослых
                if self.money <= 0 and self.animals.animals["adult"] > 0:
                    self.money += animals_price["adult"]
                    self.animals.animals["adult"] -= 1
                    self.animals.sold_animals["adult"] += 1
        #если продали всех животных
        if all(elem == 0 for elem in self.animals.animals.values()):
            if self.money <= 0:
                return EndSimulation.BANKRUPT.name
            else:
                return EndSimulation.ANIMALS_ARE_ENDED.name
        return EndSimulation.SUCCESS.name
        
    def feed_buying(self, feed_price, feed_for_purchase, forfeit):
        #расчёт необходимого животным корма (на год)
        necessary_feed = self.animals.animals["young"]/ 2 + \
                         self.animals.animals["adult"] + \
                         self.animals.animals["old"]/3
        #затраты на корм по контракту
        purchase_expenses = feed_price * feed_for_purchase
        #затраты на необходимый корм
        necessary_expenses = 0
        if self.feed < necessary_feed:
            necessary_expenses = feed_price * (necessary_feed-self.feed)
        #денег меньше, чем необходимо корма для животных
        if self.money < necessary_expenses:
            #денег меньше, чем необходимо по контракту
            if self.money < purchase_expenses:
                #платим неустойку
                self.money -= forfeit
                self.paid_forfeit += forfeit
                #на все оставшиеся деньги закупаем корм
                if self.money > 0:
                    self.feed += self.money // feed_price
                    self.money = self.money % feed_price
            #денег хватает для покупки корма по контракту
            else:
                #покупаем только кол-во по контракту
                self.money -= purchase_expenses
                self.feed += feed_for_purchase
        #денег хватает для покупки необходимого корма 
        else:
            #денег меньше, чем необходимо по контракту
            if self.money < purchase_expenses:
                #покупаем необходимый корм
                self.money -= necessary_expenses
                self.feed += necessary_expenses / feed_price
                #выбираем, что выгоднее: неустойка или корм по контракту
                purchase_expenses -= necessary_expenses
                if forfeit < purchase_expenses:
                    self.money -= forfeit
                    self.paid_forfeit += forfeit
                else:
                    self.money -= purchase_expenses
                    self.feed += purchase_expenses / feed_price
            else:
                expenses = max(purchase_expenses, necessary_expenses)
                self.money -= expenses
                self.feed += expenses / feed_price
            
    def animals_update(self):
        #кормление
        self.feed = self.animals.animals_feeding(self.feed)
        #смерть от неблагоприятных условий
        self.animals.unfavourable_conditions()
        #рост поголовья
        self.animals.animals_growth()
        
    def capital_update(self, animals_price):
        self.capital = self.money + \
                       animals_price["young"]*self.animals.animals["young"] + \
                       animals_price["adult"]*self.animals.animals["adult"] + \
                       animals_price["old"]*self.animals.animals["old"]


class Animals:
    def __init__(self, curr_animals):
        self.animals = curr_animals
        #кол-во животных, умерших за год от нехватки корма
        self.died_of_hunger = {"young": 0, "adult": 0, "old": 0}
        #кол-во животных, умерших за год от неблагоприятных условий
        self.died_of_UC = {"young": 0, "adult": 0, "old": 0}
        #кол-во проданных за год животных
        self.sold_animals = {"young": 0, "adult": 0, "old": 0}

    def animals_growth(self):
        old_value_young = self.animals["young"]
        old_value_adult = self.animals["adult"]
        #округляем в большую сторону - оптимистичные прогнозы
        self.animals["young"] = math.ceil(const.ADULT_BIRTH_RATE*self.animals["adult"] +
                                          const.OLD_BIRTH_RATE*self.animals["old"])
        self.animals["adult"] = math.ceil(const.YOUNG_SURVIVAL_CHANCE*old_value_young)
        self.animals["old"] = old_value_adult + math.ceil((1-const.OLD_MORTALITY) *
                                                           self.animals["old"])

    def unfavourable_conditions(self):
        #генерируем процент погибающих животных от неблагоприятных условий
        percent = random.randint(const.LEFT_RANGE_BORDER, const.RIGHT_RANGE_BORDER)
        for key in self.animals:
            self.died_of_UC[key] = self.animals[key]
            self.animals[key] -= math.ceil(percent/100*self.animals[key])
            self.died_of_UC[key] -= self.animals[key]
        
    def animals_feeding(self, curr_feed):
        #расчёт необходимого животным корма (на год)
        necessary_feed = self.animals["young"]/2 + self.animals["adult"] + \
                        self.animals["old"]/3
        #рассчитываем долю животных, которые выживут
        if necessary_feed != 0:
            survivor_proportion = curr_feed / necessary_feed
        else:
            return curr_feed
        if survivor_proportion >= 1:
            return curr_feed - necessary_feed
        else:
            #часть животных погибает
            for key in self.animals:
                self.died_of_hunger[key] = self.animals[key]
                self.animals[key] = math.ceil(survivor_proportion*self.animals[key])
                self.died_of_hunger[key] -= self.animals[key] 
            #израсходовали весь корм
            return 0
                     

class Contract:
    def __init__(self, period, feed_for_purchase, feed_price,
                 animals_price, animals_for_sale, forfeit):
        self.years = period
        self.animals_price = animals_price
        self.animals_for_sale = animals_for_sale
        self.forfeit = forfeit
        self.feed_price = feed_price 
        self.feed_for_purchase = feed_for_purchase

    def contract_update(self):
        self.years -= 1
        
