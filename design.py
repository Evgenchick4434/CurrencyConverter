from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 468)
        MainWindow.setMinimumSize(QSize(380, 468))
        MainWindow.setMaximumSize(QSize(380, 468))
        font = QFont()
        font.setFamilies([u"Rubik Black"])
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/static/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #22222e")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 381, 141))
        self.frame.setStyleSheet(u"background-color: #228B22")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(70, 10, 251, 41))
        font1 = QFont()
        font1.setFamilies([u"Rubik ExtraBold"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.logo.setFont(font1)
        self.logo.setStyleSheet(u"color: white")
        self.logo_pic = QPushButton(self.frame)
        self.logo_pic.setObjectName(u"logo_pic")
        self.logo_pic.setEnabled(False)
        self.logo_pic.setGeometry(QRect(130, 50, 111, 91))
        self.logo_pic.setStyleSheet(u"border: None")
        icon1 = QIcon()
        icon1.addFile(u":/icons/static/exchange.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_pic.setIcon(icon1)
        self.logo_pic.setIconSize(QSize(85, 85))
        self.input_currency = QLineEdit(self.centralwidget)
        self.input_currency.setObjectName(u"input_currency")
        self.input_currency.setGeometry(QRect(30, 170, 321, 41))
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet(u"color: white;\n"
"background-color: #228B22;\n"
"border: 2px solid white;\n"
"border-radius: 20")
        self.input_currency.setAlignment(Qt.AlignCenter)
        self.input_amount = QLineEdit(self.centralwidget)
        self.input_amount.setObjectName(u"input_amount")
        self.input_amount.setGeometry(QRect(30, 230, 321, 41))
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet(u"color: white;\n"
"background-color: #228B22;\n"
"border: 2px solid white;\n"
"border-radius: 20")
        self.input_amount.setAlignment(Qt.AlignCenter)
        self.output_currency = QLineEdit(self.centralwidget)
        self.output_currency.setObjectName(u"output_currency")
        self.output_currency.setGeometry(QRect(30, 290, 321, 41))
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet(u"color: white;\n"
"background-color: #228B22;\n"
"border: 2px solid white;\n"
"border-radius: 20")
        self.output_currency.setAlignment(Qt.AlignCenter)
        self.output_amount = QLineEdit(self.centralwidget)
        self.output_amount.setObjectName(u"output_amount")
        self.output_amount.setGeometry(QRect(30, 350, 321, 41))
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet(u"color: white;\n"
"background-color: #228B22;\n"
"border: 2px solid white;\n"
"border-radius: 20")
        self.output_amount.setAlignment(Qt.AlignCenter)
        self.copyright = QLabel(self.centralwidget)
        self.copyright.setObjectName(u"copyright")
        self.copyright.setGeometry(QRect(280, 450, 101, 16))
        font2 = QFont()
        font2.setFamilies([u"28 Days Later Cyr"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.copyright.setFont(font2)
        self.copyright.setStyleSheet(u"color: white;\n"
"background: None")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 400, 71, 61))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border: 2px solid white;\n"
"background: #5b9e00\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/static/change.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Evgenchick4434's CurrencyConverter", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u041d\u0412\u0415\u0420\u0422\u0415\u0420 \u0412\u0410\u041b\u042e\u0422", None))
        self.logo_pic.setText("")
        self.copyright.setText(QCoreApplication.translate("MainWindow", u"By Evgenchick4434", None))
        self.pushButton.setText("")
    # retranslateUi

