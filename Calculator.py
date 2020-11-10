from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import sys
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        return self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)[6:-1]


def is_balanced(string):
    ans = Stack()
    for ch in string:
        if ch in "{[(":
            ans.push(ch)
        elif ch in "}])":
            if not ans.size():
                return False
            elif {'}':'{',']':'[',')':'('}[ch] != ans.pop():
                return False
    return ans.size() == 0


class Ui_Calculator(object):

    def __init__(self):
        self.parnth = False

    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(440, 700)
        Calculator.setMinimumSize(QtCore.QSize(440, 700))
        Calculator.setMaximumSize(QtCore.QSize(440, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 440, 700))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.Answer = QtWidgets.QLineEdit(self.centralwidget)
        self.Answer.setGeometry(QtCore.QRect(20, 110, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Answer.setFont(font)
        self.Answer.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Answer.setObjectName("Answer")
        self.Answer.setReadOnly(True)
        self.decimal = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.decimal.setGeometry(QtCore.QRect(10, 610, 81, 71))
        self.decimal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.decimal.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decimal.setIcon(icon1)
        self.decimal.setObjectName("decimal")
        self.zero = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(130, 610, 81, 71))
        self.zero.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero.setText("")
        self.zero.setIcon(icon1)
        self.zero.setObjectName("zero")
        self.equal = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(250, 610, 81, 71))
        self.equal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.equal.setText("")
        self.equal.setIcon(icon1)
        self.equal.setObjectName("equal")
        self.addition = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.addition.setGeometry(QtCore.QRect(350, 610, 81, 71))
        self.addition.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addition.setText("")
        self.addition.setIcon(icon1)
        self.addition.setObjectName("addition")
        self.subtraction = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.subtraction.setGeometry(QtCore.QRect(350, 510, 81, 71))
        self.subtraction.setFocusPolicy(QtCore.Qt.NoFocus)
        self.subtraction.setText("")
        self.subtraction.setIcon(icon1)
        self.subtraction.setObjectName("subtraction")
        self.division = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(350, 420, 81, 71))
        self.division.setFocusPolicy(QtCore.Qt.NoFocus)
        self.division.setText("")
        self.division.setIcon(icon1)
        self.division.setObjectName("division")
        self.multiplication = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.multiplication.setGeometry(QtCore.QRect(350, 320, 81, 71))
        self.multiplication.setFocusPolicy(QtCore.Qt.NoFocus)
        self.multiplication.setText("")
        self.multiplication.setIcon(icon1)
        self.multiplication.setObjectName("multiplication")
        self.three = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(250, 510, 81, 71))
        self.three.setFocusPolicy(QtCore.Qt.NoFocus)
        self.three.setText("")
        self.three.setIcon(icon1)
        self.three.setObjectName("three")
        self.two = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(130, 510, 81, 71))
        self.two.setFocusPolicy(QtCore.Qt.NoFocus)
        self.two.setText("")
        self.two.setIcon(icon1)
        self.two.setObjectName("two")
        self.one = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 510, 81, 71))
        self.one.setFocusPolicy(QtCore.Qt.NoFocus)
        self.one.setText("")
        self.one.setIcon(icon1)
        self.one.setObjectName("one")
        self.six = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(250, 420, 81, 71))
        self.six.setFocusPolicy(QtCore.Qt.NoFocus)
        self.six.setText("")
        self.six.setIcon(icon1)
        self.six.setObjectName("six")
        self.five = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(130, 420, 81, 71))
        self.five.setFocusPolicy(QtCore.Qt.NoFocus)
        self.five.setText("")
        self.five.setIcon(icon1)
        self.five.setObjectName("five")
        self.four = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 420, 81, 71))
        self.four.setFocusPolicy(QtCore.Qt.NoFocus)
        self.four.setText("")
        self.four.setIcon(icon1)
        self.four.setObjectName("four")
        self.nine = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(250, 320, 81, 71))
        self.nine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nine.setText("")
        self.nine.setIcon(icon1)
        self.nine.setObjectName("nine")
        self.eight = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(130, 320, 81, 71))
        self.eight.setFocusPolicy(QtCore.Qt.NoFocus)
        self.eight.setText("")
        self.eight.setIcon(icon1)
        self.eight.setObjectName("eight")
        self.seven = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 320, 81, 71))
        self.seven.setFocusPolicy(QtCore.Qt.NoFocus)
        self.seven.setText("")
        self.seven.setIcon(icon1)
        self.seven.setObjectName("seven")
        self.bracket = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.bracket.setGeometry(QtCore.QRect(10, 220, 81, 71))
        self.bracket.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bracket.setText("")
        self.bracket.setIcon(icon1)
        self.bracket.setObjectName("bracket")
        self.root = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.root.setGeometry(QtCore.QRect(130, 220, 81, 71))
        self.root.setFocusPolicy(QtCore.Qt.NoFocus)
        self.root.setText("")
        self.root.setIcon(icon1)
        self.root.setObjectName("root")
        self.clear = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(250, 220, 181, 71))
        self.clear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear.setText("")
        self.clear.setIcon(icon1)
        self.clear.setObjectName("clear")
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
        self.root.clicked.connect(self.root_click)
        self.equal.clicked.connect(self.evaluate)
        self.clear.clicked.connect(self.clear_click)
        self.decimal.clicked.connect(self.dec_clicked)
        self.bracket.clicked.connect(self.add_bracket)
        self.addition.clicked.connect(self.add_symbol)
        self.subtraction.clicked.connect(self.sub_symbol)
        self.division.clicked.connect(self.div_symbol)
        self.multiplication.clicked.connect(self.multi_symbol)
        self.nine.clicked.connect(self.put_9)
        self.eight.clicked.connect(self.put_8)
        self.seven.clicked.connect(self.put_7)
        self.six.clicked.connect(self.put_6)
        self.five.clicked.connect(self.put_5)
        self.four.clicked.connect(self.put_4)
        self.three.clicked.connect(self.put_3)
        self.two.clicked.connect(self.put_2)
        self.one.clicked.connect(self.put_1)
        self.zero.clicked.connect(self.put_0)

    def put_0(self):
        self.Answer.setText(self.Answer.text()+"0")

    def put_1(self):
        self.Answer.setText(self.Answer.text()+"1")

    def put_2(self):
        self.Answer.setText(self.Answer.text()+"2")

    def put_3(self):
        self.Answer.setText(self.Answer.text()+"3")

    def put_4(self):
        self.Answer.setText(self.Answer.text()+"4")

    def put_5(self):
        self.Answer.setText(self.Answer.text()+"5")

    def put_6(self):
        self.Answer.setText(self.Answer.text()+"6")

    def put_7(self):
        self.Answer.setText(self.Answer.text()+"7")

    def put_8(self):
        self.Answer.setText(self.Answer.text()+"8")

    def put_9(self):
        self.Answer.setText(self.Answer.text()+"9")

    def multi_symbol(self):
        self.Answer.setText(self.Answer.text()+"*")

    def div_symbol(self):
        self.Answer.setText(self.Answer.text()+"/")

    def sub_symbol(self):
        self.Answer.setText(self.Answer.text()+"-")

    def add_symbol(self):
        self.Answer.setText(self.Answer.text()+"+")

    def add_bracket(self):
        if self.parnth:
            self.Answer.setText(self.Answer.text()+")")
            self.parnth = False
        else:
            self.Answer.setText(self.Answer.text()+"(")
            self.parnth = True

    def dec_clicked(self):
        self.Answer.setText(self.Answer.text()+".")

    def clear_click(self):
        try:
            if self.Answer.text() == "Invalid Expression":
                self.Answer.clear()
            else:
                if self.Answer.text()[-1] == ')':
                    self.parnth = True
                elif self.Answer.text()[-1] == '(':
                    self.parnth = False
                self.Answer.setText(self.Answer.text()[:-1])
        except:
            pass

    def evaluate(self):
        try:
            ans = str(eval(self.Answer.text()))
        except :
            pass
        else:
            self.Answer.setText(ans)
            self.parnth = False

    def root_click(self):
        try:
            ans = str(eval(self.Answer.text())**0.5)
        except:
            pass
        else:
            self.Answer.setText(ans)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.Answer.setPlaceholderText(_translate("Calculator", "Calculation Goes Here"))


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(440, 700)
        SplashScreen.setMinimumSize(QtCore.QSize(440, 700))
        SplashScreen.setMaximumSize(QtCore.QSize(440, 700))
        SplashScreen.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 440, 700))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/splash.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "Calculator"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)

    Calculator = QtWidgets.QMainWindow()
    ui1 = Ui_Calculator()
    ui1.setupUi(Calculator)    
    SplashScreen.show()
    QtCore.QTimer.singleShot(1500, Calculator.show)
    
    sys.exit(app.exec_())