# 상승장 알리미 (2) -- UI 파일 불러오기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("ch5/bull.ui")[0]

class MyWindow(QMainWindow, form_class):  
    def __init__(self):                      # 타이머 만들기
        super().__init__()  
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)   # 5초마다 업데이트
        timer.timeout.connect(self.timeout)

    def timeout(self):                       #  가상화폐 이름 출력하기
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

            price, last_ma5, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(state))
    
    def get_market_infos(self, ticker):       # 나머지 데이터 추가하기
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)

        state = None
        if price > last_ma5:
            state = "상승장"
        else:
            state = "하락장"

        return price, last_ma5, state
        

app = QApplication(sys.argv)  
window = MyWindow()
window.show()
app.exec_()
