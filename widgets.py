from PyQt5.QtWidgets import QPushButton


class PlushyButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("QPushButton {"
                           "    border: 2px solid #FF6F61;"  # Pink border
                           "    border-radius: 25px;"  # Rounded corners
                           "    padding: 10px 20px;"  # Padding inside the button
                           "    font-size: 30px;"  # Font size
                           "    background-color: #ff6f61;"  # Pink background color
                           "    color: white;"  # Text color
                           "}"
                           "QPushButton:hover {"
                           "    background-color: #FFA07A;"  # Lighter pink on hover
                           "}"
                           "QPushButton:pressed {"
                           "    background-color: #FF6347;"  # Darker pink when pressed
                           "}")
