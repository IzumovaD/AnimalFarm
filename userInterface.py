from PyQt5 import QtCore, QtGui, QtWidgets

import classes as cls
import constants as const


class UiMainWindow(object):
    def __init__(self):
        self.exp = cls.Experiment()

    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        #основное окно
        MainWindow.setObjectName("MainWindow")
        MainWindow.setBaseSize(QtCore.QSize(800, 1000))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        #надпись "Начальные данные"
        self.label_initData = QtWidgets.QLabel(self.centralwidget)
        self.label_initData.setObjectName("label_initData")
        self.verticalLayout_3.addWidget(self.label_initData)
        
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setObjectName("formLayout")

        #надпись "Денежный капитал (у.е.)"
        self.label_initMoney = QtWidgets.QLabel(self.centralwidget)
        self.label_initMoney.setObjectName("label_initMoney")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label_initMoney)

        #поле ввода денежного капитала
        self.lineEdit_initMoney = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_initMoney.setObjectName("lineEdit_initMoney")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.lineEdit_initMoney)
        self.lineEdit_initMoney.setPlaceholderText(_translate('', 'от 0 до 9 999 999'))
        self.lineEdit_initMoney.setValidator(QtGui.QIntValidator(0, 9000000))
        self.lineEdit_initMoney.setText(_translate("MainWindow", str(const.default_money),
                                                   None))

        #надпись "Молодые животные"
        self.label_initYoung = QtWidgets.QLabel(self.centralwidget)
        self.label_initYoung.setObjectName("label_initYoung")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.label_initYoung)

        #надпись "Корм (кг)"
        self.label_initFeed = QtWidgets.QLabel(self.centralwidget)
        self.label_initFeed.setObjectName("label_initFeed")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                  self.label_initFeed)

        #поле ввода кол-ва корма
        self.lineEdit_initFeed = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_initFeed.setObjectName("lineEdit_initFeed")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                  self.lineEdit_initFeed)
        self.lineEdit_initFeed.setPlaceholderText(_translate('', 'от 0 до 999999'))
        self.lineEdit_initFeed.setValidator(QtGui.QIntValidator(0, 900000))
        self.lineEdit_initFeed.setText(_translate("MainWindow", str(const.default_curr_feed),
                                                  None))

        #поле ввода молодых животных
        self.lineEdit_initYoung = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_initYoung.setObjectName("lineEdit_initYoung")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.lineEdit_initYoung)
        #допустимый диапазон
        self.lineEdit_initYoung.setPlaceholderText(_translate('', 'от 0 до 9999'))
        #контроль диапазона
        self.lineEdit_initYoung.setValidator(QtGui.QIntValidator(0, 9000))
        #значение по умолчанию
        self.lineEdit_initYoung.setText(_translate("MainWindow",
                                                   str(const.default_curr_animals["young"]),
                                                   None))

        #надпись "Взрослые животные"
        self.label_initAdult = QtWidgets.QLabel(self.centralwidget)
        self.label_initAdult.setObjectName("label_initAdult")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_initAdult)

        #надпись "Старые животные"
        self.label_initOld = QtWidgets.QLabel(self.centralwidget)
        self.label_initOld.setObjectName("label_initOld")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.label_initOld)

        #поле ввода взрослых животных
        self.lineEdit_initAdult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_initAdult.setObjectName("lineEdit_initAdult")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.lineEdit_initAdult)
        self.lineEdit_initAdult.setPlaceholderText(_translate('', 'от 0 до 9999'))
        self.lineEdit_initAdult.setValidator(QtGui.QIntValidator(0, 9000))
        self.lineEdit_initAdult.setText(_translate("MainWindow",
                                                   str(const.default_curr_animals["adult"]),
                                                   None))

        #поле ввода старых животных
        self.lineEdit_initOld = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_initOld.setObjectName("lineEdit_initOld")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.lineEdit_initOld)
        self.lineEdit_initOld.setPlaceholderText(_translate('', 'от 0 до 9999'))
        self.lineEdit_initOld.setValidator(QtGui.QIntValidator(0, 9000))
        self.lineEdit_initOld.setText(_translate("MainWindow",
                                                 str(const.default_curr_animals["old"]),
                                                 None))
        
        self.verticalLayout_3.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        #кнопка "Конец моделирования"
        self.pushButton_end = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_end.setObjectName("pushButton_end")
        self.gridLayout.addWidget(self.pushButton_end, 3, 1, 1, 1)
        self.pushButton_end.setEnabled(False)
        self.pushButton_end.clicked.connect(self.end_button)

        #кнопка "Ввести данные"
        self.pushButton_enterData = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enterData.setObjectName("pushButton_enterData")
        self.gridLayout.addWidget(self.pushButton_enterData, 3, 0, 1, 1)
        self.pushButton_enterData.clicked.connect(self.enter_data_button)

        #кнопка "Шаг моделирования"
        self.pushButton_step = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_step.setObjectName("pushButton_step")
        self.gridLayout.addWidget(self.pushButton_step, 4, 0, 1, 1)
        self.pushButton_step.clicked.connect(self.step_button)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_step.setEnabled(False)

        #надпись "Контракт"
        self.label_contract = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(self.label_contract.sizePolicy().hasHeightForWidth())
        self.label_contract.setSizePolicy(sizePolicy)
        self.label_contract.setMinimumSize(QtCore.QSize(0, 27))
        self.label_contract.setObjectName("label_contract")
        self.verticalLayout_2.addWidget(self.label_contract)
        
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")

        #надпись "Срок (лет)"
        self.label_years = QtWidgets.QLabel(self.centralwidget)
        self.label_years.setObjectName("label_years")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                    self.label_years)

        #поле ввода срока контракта
        self.lineEdit_years = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_years.setObjectName("lineEdit_years")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_years)
        self.lineEdit_years.setPlaceholderText(_translate('', 'от 1 до 9'))
        self.lineEdit_years.setValidator(QtGui.QIntValidator(1, 9))
        self.lineEdit_years.setText(_translate("MainWindow", str(const.default_years),
                                               None))

        #надпись "Молодые животные для продажи"
        self.label_youngForSale = QtWidgets.QLabel(self.centralwidget)
        self.label_youngForSale.setObjectName("label_youngForSale")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                    self.label_youngForSale)

        #поле ввода молодых животных для продажи
        self.lineEdit_youngForSale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_youngForSale.setObjectName("lineEdit_youngForSale")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_youngForSale)
        self.lineEdit_youngForSale.setPlaceholderText(_translate('', 'от 0 до 9999'))
        self.lineEdit_youngForSale.setValidator(QtGui.QIntValidator(0, 9000))
        self.lineEdit_youngForSale.setText(_translate("MainWindow",
                                                      str(const.default_animals_for_sale["young"]),
                                                      None))

        #надпись "Цена молодых животных (у.е.)"
        self.label_youngPrice = QtWidgets.QLabel(self.centralwidget)
        self.label_youngPrice.setObjectName("label_youngPrice")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                    self.label_youngPrice)

        #поле ввода цены молодых животных 
        self.lineEdit_youngPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_youngPrice.setObjectName("lineEdit_youngPrice")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_youngPrice)
        self.lineEdit_youngPrice.setPlaceholderText(_translate('', 'от 1 до 99999'))
        self.lineEdit_youngPrice.setValidator(QtGui.QIntValidator(0, 90000))
        self.lineEdit_youngPrice.setText(_translate("MainWindow",
                                                    str(const.default_animals_price["young"]),
                                                    None))

        #надпись "Кол-во корма для закупки (кг)"
        self.label_feedForPurchase = QtWidgets.QLabel(self.centralwidget)
        self.label_feedForPurchase.setObjectName("label_feedForPurchase")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole,
                                    self.label_feedForPurchase)

        #надпись "Цена корма (у.е. за кг)"
        self.label_feedPrice = QtWidgets.QLabel(self.centralwidget)
        self.label_feedPrice.setObjectName("label_feedPrice")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole,
                                    self.label_feedPrice)

        #поле ввода цены корма
        self.lineEdit_feedPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_feedPrice.setObjectName("lineEdit_feedPrice")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_feedPrice)
        self.lineEdit_feedPrice.setPlaceholderText(_translate('', 'от 1 до 99999'))
        self.lineEdit_feedPrice.setValidator(QtGui.QIntValidator(0, 90000))
        self.lineEdit_feedPrice.setText(_translate("MainWindow",
                                                   str(const.default_feed_price), None))

        #надпись "Неустойка (у.е.)"
        self.label_forfeit = QtWidgets.QLabel(self.centralwidget)
        self.label_forfeit.setObjectName("label_forfeit")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole,
                                    self.label_forfeit)

        #поле ввода неустойки
        self.lineEdit_forfeit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_forfeit.setObjectName("lineEdit_forfeit")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_forfeit)
        self.lineEdit_forfeit.setPlaceholderText(_translate('', 'от 0 до 999999'))
        self.lineEdit_forfeit.setValidator(QtGui.QIntValidator(0, 900000))
        self.lineEdit_forfeit.setText(_translate("MainWindow",
                                                 str(const.default_forfeit), None))

        #поле ввода кол-ва корма для закупки
        self.lineEdit_feedForPurchase = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_feedForPurchase.setObjectName("lineEdit_feedForPurchase")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_feedForPurchase)
        self.lineEdit_feedForPurchase.setPlaceholderText(_translate('', 'от 0 до 999999'))
        self.lineEdit_feedForPurchase.setValidator(QtGui.QIntValidator(0, 900000))
        self.lineEdit_feedForPurchase.setText(_translate("MainWindow",
                                                         str(const.default_feed_for_purchase),
                                                         None))

        #надпись "Взрослые животные для продажи"
        self.label_adultForSale = QtWidgets.QLabel(self.centralwidget)
        self.label_adultForSale.setObjectName("label_adultForSale")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                    self.label_adultForSale)

        #поле ввода кол-ва взрослых животных для продажи
        self.lineEdit_adultForSale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_adultForSale.setObjectName("lineEdit_adultForSale")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_adultForSale)
        self.lineEdit_adultForSale.setPlaceholderText(_translate('', 'от 0 до 9999'))
        self.lineEdit_adultForSale.setValidator(QtGui.QIntValidator(0, 9000))
        self.lineEdit_adultForSale.setText(_translate("MainWindow",
                                                      str(const.default_animals_for_sale["adult"]),
                                                      None))

        #надпись "Старые животные для продажи"
        self.label_oldForSale = QtWidgets.QLabel(self.centralwidget)
        self.label_oldForSale.setObjectName("label_oldForSale")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                    self.label_oldForSale)

        #поле ввода кол-ва старых животных для продажи
        self.lineEdit_oldForSale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_oldForSale.setObjectName("lineEdit_oldForSale")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_oldForSale)
        self.lineEdit_oldForSale.setPlaceholderText(_translate('', 'от 0 до 9999'))
        self.lineEdit_oldForSale.setValidator(QtGui.QIntValidator(0, 9000))
        self.lineEdit_oldForSale.setText(_translate("MainWindow",
                                                    str(const.default_animals_for_sale["old"]),
                                                    None))

        #надпись "Цена взрослых животных (у.е.)"
        self.label_adultPrice = QtWidgets.QLabel(self.centralwidget)
        self.label_adultPrice.setObjectName("label_adultPrice")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole,
                                    self.label_adultPrice)

        #поле ввода цены взрослых животных
        self.lineEdit_adultPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_adultPrice.setObjectName("lineEdit_adultPrice")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_adultPrice)
        self.lineEdit_adultPrice.setPlaceholderText(_translate('', 'от 1 до 99999'))
        self.lineEdit_adultPrice.setValidator(QtGui.QIntValidator(0, 90000))
        self.lineEdit_adultPrice.setText(_translate("MainWindow",
                                                    str(const.default_animals_price["adult"]),
                                                    None))

        #надпись "Цена старых животных (у.е.)"
        self.label_oldPrice = QtWidgets.QLabel(self.centralwidget)
        self.label_oldPrice.setObjectName("label_oldPrice")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole,
                                    self.label_oldPrice)

        #поле ввода цены старых животных
        self.lineEdit_oldPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_oldPrice.setObjectName("lineEdit_oldPrice")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEdit_oldPrice)
        self.lineEdit_oldPrice.setPlaceholderText(_translate('', 'от 1 до 99999'))
        self.lineEdit_oldPrice.setValidator(QtGui.QIntValidator(0, 90000))
        self.lineEdit_oldPrice.setText(_translate("MainWindow",
                                                  str(const.default_animals_price["old"]),
                                                  None))
        
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        #надпись "Начальные данные"
        self.label_entParams = QtWidgets.QLabel(self.centralwidget)
        self.label_entParams.setObjectName("label_entParams")
        self.gridLayout.addWidget(self.label_entParams, 0, 0, 1, 1)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        #надпись "Статистика"
        self.label_stat = QtWidgets.QLabel(self.centralwidget)
        self.label_stat.setObjectName("label_stat")
        self.verticalLayout.addWidget(self.label_stat)

        #окно вывода статистики
        self.textBrowser_stat = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_stat.setObjectName("textBrowser_stat")
        self.verticalLayout.addWidget(self.textBrowser_stat)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 3, 1)

        #кнопка "Выход"
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout.addWidget(self.pushButton_exit, 4, 1, 1, 1)
        self.pushButton_exit.clicked.connect(self.end)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #функция изменения активности полей
    def change_line_edits(self, flag):
        self.lineEdit_initMoney.setReadOnly(flag)
        self.lineEdit_initFeed.setReadOnly(flag)
        self.lineEdit_initYoung.setReadOnly(flag)
        self.lineEdit_initAdult.setReadOnly(flag)
        self.lineEdit_initOld.setReadOnly(flag)
        self.lineEdit_years.setReadOnly(flag)
        self.lineEdit_youngForSale.setReadOnly(flag)
        self.lineEdit_adultForSale.setReadOnly(flag)
        self.lineEdit_oldForSale.setReadOnly(flag)
        self.lineEdit_youngPrice.setReadOnly(flag)
        self.lineEdit_adultPrice.setReadOnly(flag)
        self.lineEdit_oldPrice.setReadOnly(flag)
        self.lineEdit_feedForPurchase.setReadOnly(flag)
        self.lineEdit_feedPrice.setReadOnly(flag)
        self.lineEdit_forfeit.setReadOnly(flag)
        
    #закрытие окна
    def end(self):
        self.close()

    def enter_data(self):
        self.exp = cls.Experiment()
        _translate = QtCore.QCoreApplication.translate
        #если что-то было введено в поле
        if self.lineEdit_initMoney.text() != "":
            #считываем
            self.exp.money = int(self.lineEdit_initMoney.text())
        #если поле пустое 
        else:
            #берём значение по умолчанию
            self.lineEdit_initMoney.setText(_translate("MainWindow",
                                                       str(const.default_money),
                                                       None))
        if self.lineEdit_initYoung.text() != "":
            self.exp.curr_animals["young"] = int(self.lineEdit_initYoung.text())
        else:
            self.lineEdit_initYoung.setText(_translate("MainWindow",
                                                       str(const.default_curr_animals["young"]),
                                                       None))
        if self.lineEdit_initAdult.text() != "":
            self.exp.curr_animals["adult"] = int(self.lineEdit_initAdult.text())
        else:
            self.lineEdit_initAdult.setText(_translate("MainWindow",
                                                       str(const.default_curr_animals["adult"]),
                                                       None))
        if self.lineEdit_initOld.text() != "":
            self.exp.curr_animals["old"] = int(self.lineEdit_initOld.text())
        else:
            self.lineEdit_initOld.setText(_translate("MainWindow",
                                                     str(const.default_curr_animals["old"]),
                                                     None))
        if self.lineEdit_initFeed.text() != "":
            self.exp.curr_feed = int(self.lineEdit_initFeed.text())
        else:
            self.lineEdit_initFeed.setText(_translate("MainWindow",
                                                      str(const.default_curr_feed),
                                                      None))
        if self.lineEdit_years.text() != "":
            self.exp.years = int(self.lineEdit_years.text())
        else:
            self.lineEdit_years.setText(_translate("MainWindow",
                                                   str(const.default_years),
                                                   None))
        if self.lineEdit_feedForPurchase.text() != "":
            self.exp.feed_for_purchase = int(self.lineEdit_feedForPurchase.text())
        else:
            self.lineEdit_feedForPurchase.setText(_translate("MainWindow",
                                                             str(const.default_feed_for_purchase),
                                                             None))
        if self.lineEdit_feedPrice.text() != "":
            self.exp.feed_price = int(self.lineEdit_feedPrice.text())
        else:
            self.lineEdit_feedPrice.setText(_translate("MainWindow",
                                                       str(const.default_feed_price),
                                                       None))
        if self.lineEdit_youngForSale.text() != "":
            self.exp.animals_for_sale["young"] = int(self.lineEdit_youngForSale.text())
        else:
            self.lineEdit_youngForSale.setText(_translate("MainWindow",
                                                          str(const.default_animals_for_sale["young"]),
                                                          None))
        if self.lineEdit_adultForSale.text() != "":
            self.exp.animals_for_sale["adult"] = int(self.lineEdit_adultForSale.text())
        else:
            self.lineEdit_adultForSale.setText(_translate("MainWindow",
                                                          str(const.default_animals_for_sale["adult"]),
                                                          None))
        if self.lineEdit_oldForSale.text() != "":
            self.exp.animals_for_sale["old"] = int(self.lineEdit_oldForSale.text())
        else:
            self.lineEdit_oldForSale.setText(_translate("MainWindow",
                                                        str(const.default_animals_for_sale["old"]),
                                                        None))
        if self.lineEdit_youngPrice.text() != "":
            self.exp.animals_price["young"] = int(self.lineEdit_youngPrice.text())
        else:
            self.lineEdit_youngPrice.setText(_translate("MainWindow",
                                                        str(const.default_animals_price["young"]),
                                                        None))
        if self.lineEdit_adultPrice.text() != "":
            self.exp.animals_price["adult"] = int(self.lineEdit_adultPrice.text())
        else:
            self.lineEdit_adultPrice.setText(_translate("MainWindow",
                                                        str(const.default_animals_price["adult"]),
                                                        None))
        if self.lineEdit_oldPrice.text() != "":
            self.exp.animals_price["old"] = int(self.lineEdit_oldPrice.text())
        else:
            self.lineEdit_oldPrice.setText(_translate("MainWindow",
                                                      str(const.default_animals_price["old"]),
                                                      None))
        if self.lineEdit_forfeit.text() != "":
            self.exp.forfeit = int(self.lineEdit_forfeit.text())
        else:
            self.lineEdit_forfeit.setText(_translate("MainWindow",
                                                     str(const.default_forfeit),
                                                     None))
        self.exp.create_farm_contract()

    def enter_data_button(self):
        self.enter_data()
        self.change_line_edits(True)
        self.pushButton_enterData.setEnabled(False)
        self.pushButton_end.setEnabled(True)
        self.pushButton_step.setEnabled(True)

    def end_simulation(self):
        self.pushButton_enterData.setEnabled(True)
        self.change_line_edits(False)
        self.pushButton_end.setEnabled(False)
        self.pushButton_step.setEnabled(False)

    def step_button(self):
        #делаем шаг
        flag, string = self.exp.step()
        self.textBrowser_stat.append(string)
        #если срок контракта кончился или контракт завершён досрочно
        if flag != "SUCCESS":
            if flag == "BANKRUPT":
                self.textBrowser_stat.append("БАНКРОТ, конец моделирования\n\n")
            if flag == "ANIMALS_ARE_ENDED":
                self.textBrowser_stat.append("Все животные распроданы, конец моделирования\n\n")
            if flag == "CONTRACT_ENDED":
                self.textBrowser_stat.append("Срок контракта закончен, конец моделирования\n\n")
            #заканчиваем моделирование
            self.end_simulation()
        return flag

    def end_button(self):
        flag = "SUCCESS"
        #завершаем все шаги
        while self.step_button() == "SUCCESS":
            continue
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "Животноводческая ферма"))
        self.label_initData.setText(_translate("MainWindow",
                                               "<html><head/><body><p align=\"center\">Начальные данные</p></body></html>"))
        self.label_initMoney.setText(_translate("MainWindow",
                                                "Денежный капитал (у.е.)"))
        self.label_initYoung.setText(_translate("MainWindow",
                                                "Молодые животные"))
        self.label_initFeed.setText(_translate("MainWindow",
                                               "<html><head/><body><p align=\"center\">Корм (кг)</p></body></html>"))
        self.label_initAdult.setText(_translate("MainWindow",
                                                "Взрослые животные"))
        self.label_initOld.setText(_translate("MainWindow",
                                              "Старые животные"))
        self.pushButton_end.setText(_translate("MainWindow",
                                               "Конец моделирования"))
        self.pushButton_enterData.setText(_translate("MainWindow",
                                                     "Ввести данные"))
        self.pushButton_step.setText(_translate("MainWindow",
                                                "Шаг моделирования (год)"))
        self.label_contract.setText(_translate("MainWindow",
                                               "<html><head/><body><p align=\"center\">Контракт</p></body></html>"))
        self.label_years.setText(_translate("MainWindow", "Срок (кол-во лет)"))
        self.label_youngForSale.setText(_translate("MainWindow",
                                                   "Молодые животные для продажи"))
        self.label_youngPrice.setText(_translate("MainWindow",
                                                 "Цена молодых животных (у.е.)"))
        self.label_feedForPurchase.setText(_translate("MainWindow",
                                                      "Кол-во корма для закупки (кг)"))
        self.label_feedPrice.setText(_translate("MainWindow",
                                                "Цена корма (у.е. за кг)"))
        self.label_forfeit.setText(_translate("MainWindow", "Неустойка (у.е.)"))
        self.label_adultForSale.setText(_translate("MainWindow",
                                                   "Взрослые животные для продажи"))
        self.label_oldForSale.setText(_translate("MainWindow",
                                                 "Старые животные для продажи"))
        self.label_adultPrice.setText(_translate("MainWindow",
                                                 "Цена взрослых животных (у.е.)"))
        self.label_oldPrice.setText(_translate("MainWindow",
                                               "Цена старых животных (у.е.)"))
        self.label_entParams.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Ввод параметров</span></p></body></html>"))
        self.label_stat.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\">Статистика</p></body></html>"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход"))


class App(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
