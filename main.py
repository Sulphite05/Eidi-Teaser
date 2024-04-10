import sys
from PyQt5.QtWidgets import QApplication
from main_window import EidMubarakInterface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EidMubarakInterface()
    window.show()
    sys.exit(app.exec_())
