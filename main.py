import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QLineEdit, QApplication
from backend import Chatbot
import threading


class Chatbotwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setWindowTitle("GPT Chatbot GUI")
        self.setMinimumSize(600, 400)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setGeometry(10, 10, 480, 320)
            # 10 pixels from the left border
            # 10 pixels from the upper boarder
            # 480 width and 320 height

        # Add input field widget
        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(10, 340, 480, 30)
        self.input_box.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 80, 30)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        prompt = self.input_box.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {prompt}</p>")
        self.input_box.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(prompt,))
        thread.start()

    def get_bot_response(self, user_prompt):
        answer = self.chatbot.get_response(user_prompt)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Botti: {answer}</p>")

app = QApplication(sys.argv)
main_window = Chatbotwindow()
sys.exit(app.exec())
