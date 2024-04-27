from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt5.QtCore import QTimer, Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import QFont, QGuiApplication, QLinearGradient, QColor, QPainter
from widgets import PlushyButton
import random


class EidMubarakInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.nag_timer = QTimer(self)
        self.nag_timer.timeout.connect(self.nagUser)
        self.nag_timer.start(5000)  # Start timer with 5-second delay

    def initUI(self):
        self.setWindowTitle('Eidi Teaser')
        self.setWindowState(Qt.WindowFullScreen)  # Set window to full screen

        font_title = QFont("Comic Sans MS", 64, QFont.Bold)  # Larger and bolder font for title
        font = QFont("Comic Sans MS", 48, QFont.Bold)  # Larger and bolder font

        # Get screen geometry
        screen_geometry = QGuiApplication.primaryScreen().geometry()
        pink = QColor(254, 204, 205)
        light_pink = QColor(255, 238, 236)
        white = QColor(255, 255, 255)
        # Set up gradient background
        self.gradient = QLinearGradient(0, 0, 0, screen_geometry.height())
        self.gradient.setColorAt(0.0, pink)  # Start color
        self.gradient.setColorAt(0.25, light_pink)  # Color at 25% position
        self.gradient.setColorAt(0.5, white)  # Color at 50% position
        self.gradient.setColorAt(0.75, light_pink)  # Color at 75% position
        self.gradient.setColorAt(1.0, pink)  # End color

        # Set up title label
        self.title_label = QLabel('Eid Mubarak, lovely people!', self)
        self.title_label.setFont(font_title)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(0, 0, screen_geometry.width(), 350)  # Adjusted size and position
        self.title_label.setStyleSheet("font-size: 64px; color: #cc37a4;")

        # Set up main label
        self.label = QLabel('Now send me some Eidi 🤌, pwease (❁ᴗ͈ˬᴗ͈) ', self)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())  # Adjusted size and position
        self.label.move((screen_geometry.width() - self.label.width()) // 2, (
                screen_geometry.height() - 150 - self.label.height()) // 4)  # Centered horizontally and vertically
        self.label.setStyleSheet("font-size: 48px; color: #6a0dad;")

        # Set up nag label
        self.nag_label = QLabel(self)
        self.nag_label.setAlignment(Qt.AlignCenter)
        self.nag_label.setStyleSheet("font-size: 36px; color: #FF6F61;")
        self.nag_label.setGeometry(0, 0, self.width(), self.height())
        self.nag_label.move((screen_geometry.width() - self.nag_label.width()) // 2, 380)

        # Set up "Sure, Cutie Pie" button
        self.button = PlushyButton('Sure, cutie pie ૮ ˶ᵔ ᵕ ᵔ˶ ა', self)
        self.button.setFont(font)
        self.button.setGeometry(0, 0, 450, 80)  # Adjusted size
        self.button.move((screen_geometry.width() - self.button.width()) // 2 - 250, (
                screen_geometry.height() + 200 - self.button.height()) // 2)  # Centered horizontally and vertically
        self.button.clicked.connect(self.sendEidi)

        # Set up "No, I'm Greedy" button
        self.greedyButton = PlushyButton("No, I'm greedy (｡•̀ ᴖ •́｡)", self)
        self.greedyButton.setFont(font)
        self.greedyButton.setGeometry(0, 0, 450, 80)  # Adjusted size
        self.greedyButton.move((screen_geometry.width() - self.greedyButton.width()) // 2 + 250, (
                screen_geometry.height() + 200 - self.button.height()) // 2)  # Centered horizontally and vertically
        self.greedyButton.installEventFilter(self)
        self.greedyButton.clicked.connect(self.userWin)

    def userWin(self):
        self.nag_timer.stop()  # Stop the nagging timer if the user clicks the button
        alert = QMessageBox()
        alert.setWindowTitle('Eid Mubarak!')
        alert.setText('<div style="color: #FF69B4; text-align: center;">NOOO, You\'re the worst!<br>(╥﹏╥)</div>')
        alert.setStyleSheet("font-size: 36px; background-color: #FFDAB9")  # Set a cute background color
        okay_button = alert.addButton("Yes, I know", QMessageBox.AcceptRole)
        okay_button.setStyleSheet("QPushButton {"
                                  "    background-color: #FF6F61;"
                                  "    color: white;"
                                  "    border-radius: 15px;"
                                  "    padding: 15px 30px;"
                                  "    font-size: 30px;"
                                  "    border: 3px solid #FF6F61;"  # Add border to make it look plushy
                                  "}"
                                  "}")
        alert.exec_()

    def sendEidi(self):
        self.nag_timer.stop()  # Stop the nagging timer if the user clicks the button
        alert = QMessageBox()
        alert.setWindowTitle('Eid Mubarak!')
        alert.setText('<div style="color: #FF69B4; text-align: center;">Aww! You\'re the best!<br>(｡◕‿‿◕｡)</div>')
        alert.setStyleSheet("font-size: 36px; background-color: #FFDAB9")  # Set a cute background color
        thanks_button = alert.addButton("Thanks!", QMessageBox.AcceptRole)
        thanks_button.setStyleSheet("QPushButton {"
                                    "    background-color: #FF6F61;"
                                    "    color: white;"
                                    "    border-radius: 15px;"
                                    "    padding: 15px 30px;"
                                    "    font-size: 30px;"
                                    "    border: 3px solid #FF6F61;"  # Add border to make it look plushy
                                    "}"
                                    "}")
        alert.exec_()

    def moveGreedyButton(self):
        max_x = self.width() - self.greedyButton.width()
        max_y = self.height() - self.greedyButton.height()
        self.animation = QPropertyAnimation(self.greedyButton, b"pos")
        self.animation.setDuration(50)  # Duration in milliseconds
        new_pos = QPoint(random.randint(0, max_x), random.randint(0, max_y))
        self.animation.setEndValue(new_pos)
        self.animation.start()

    def eventFilter(self, obj, event):
        if obj == self.greedyButton and (event.type() == event.Enter):
            self.moveGreedyButton()
        return super().eventFilter(obj, event)

    def nagUser(self):
        nag_labels = ["Come on now, don't be grumpy!", "Just 5000 rupees 👉👈",
                      "Click Yes, pretty please!", "You'll never win :))"]
        if not hasattr(self, 'nag_index'):
            self.nag_index = 0  # Initialize the index if not exists
        self.nag_label.setText(nag_labels[self.nag_index])
        self.nag_label.show()
        # Increment the index for the next label
        self.nag_index = (self.nag_index + 1) % len(nag_labels)
        # Hide the old nag label after 3 seconds
        QTimer.singleShot(3000, lambda: self.nag_label.hide())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.gradient)
        painter.drawRect(self.rect())
