from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QVBoxLayout,QRadioButton,QLineEdit,QTextEdit,QHBoxLayout
from PyQt5.QtGui import *
from ai import *


app = QApplication([])

font = QFont('verdana',12)
information = []
#language select window
lang_win = QWidget()
title = QLabel('Diet Creator App')
sel_lang = QLabel('Διαλέξτε γλώσσα-Select Language-Sprache wählen')
Greek = QPushButton("Ελληνικά")
english = QPushButton("English")
deutsch = QPushButton("Deutsch")

lang_win.setFont(font)
lang_win.resize(500,300)
lang_win.setStyleSheet("background-color: lightgreen;")
lang_win.setWindowTitle("Diet Creator App-Lang_select")

v1 = QVBoxLayout()
v1.addWidget(title,alignment= Qt.AlignCenter)
v1.addWidget(sel_lang,alignment= Qt.AlignCenter)
v1.addWidget(Greek,alignment= Qt.AlignCenter)
v1.addWidget(english,alignment= Qt.AlignCenter)
v1.addWidget(deutsch,alignment= Qt.AlignCenter)
lang_win.setLayout(v1)
lang_win.show()

#main front-end
greek_win = QWidget()


greek_win.resize(700,500)
greek_win.setStyleSheet("background-color: lightgreen;")
greek_win.setWindowTitle("Diet Creator App")

title2 = QLabel('Diet Creator App')
gender1 = QLabel("")
male1 = QRadioButton("")
female1 = QRadioButton('')
agetxt = QLabel("")
agein = QLineEdit('')
infostxt = QLabel('')
infosin = QTextEdit('')
genbutton = QPushButton("")
backbutton = QPushButton("")

h1 = QHBoxLayout()
h1.addWidget(male1,alignment= Qt.AlignLeft)
h1.addWidget(female1,alignment= Qt.AlignLeft)


v2 = QVBoxLayout()
v2.addWidget(title2,alignment= Qt.AlignCenter)
v2.addWidget(gender1,alignment= Qt.AlignLeft)
v2.addLayout(h1)
v2.addWidget(agetxt,alignment= Qt.AlignLeft)
v2.addWidget(agein,alignment= Qt.AlignLeft)
v2.addWidget(infostxt,alignment= Qt.AlignLeft)
v2.addWidget(infosin,alignment= Qt.AlignLeft)
v2.addWidget(genbutton,alignment=Qt.AlignCenter)
v2.addWidget(backbutton,alignment= Qt.AlignCenter)
greek_win.setLayout(v2)

#result screen

res_win = QWidget()

res_win.resize(1000,1000)
res_win.setStyleSheet("background-color: lightgreen;")
res_win.setWindowTitle("Diet Creator App")

title3 = QLabel('Diet Creator App')
res_text = QLabel('')
res_show = QTextEdit('')
res_show.setMinimumHeight(900) 
res_show.setMinimumWidth(1000)
backbutton2 = QPushButton('')
ask_button = QPushButton('')


h2 = QHBoxLayout()
h2.addWidget(ask_button,alignment = Qt.AlignCenter)
h2.addWidget(backbutton2,alignment = Qt.AlignCenter)

v3 = QVBoxLayout()
v3.addWidget(title3,alignment= Qt.AlignCenter)
v3.addWidget(res_text,alignment= Qt.AlignCenter)
v3.addWidget(res_show,alignment= Qt.AlignCenter)
v3.addLayout(h2)
res_win.setLayout(v3)


#questions window
ask_win = QWidget()
ask_win.resize(1000,1000)
ask_win.setStyleSheet("background-color: lightgreen;")
ask_win.setWindowTitle("Diet Creator App-questions")

title4 = QLabel('Diet Creator App')
ask_area = QTextEdit('')
ask_line = QLineEdit('')
send_questbutton = QPushButton('')
backbutton3 = QPushButton('')

ask_area.setMinimumHeight(900) 
ask_area.setMinimumWidth(1000)

ask_line.setMinimumWidth(1000)


h3 = QHBoxLayout()
h3.addWidget(ask_line,alignment = Qt.AlignRight)
h3.addWidget(send_questbutton,alignment = Qt.AlignCenter)
v4 = QVBoxLayout()
v4.addWidget(title4,alignment= Qt.AlignCenter)
v4.addWidget(ask_area,alignment = Qt.AlignCenter)
v4.addLayout(h3)
v4.addWidget(backbutton3,alignment = Qt.AlignCenter)
ask_win.setLayout(v4)


#app work method
def male_button():
    # This function only changes the UI color. Data is collected on final button press.
    greek_win.setFont(font)
    greek_win.setStyleSheet("background-color: lightblue;")
male1.clicked.connect(male_button)

def fem_button():
    # This function only changes the UI color. Data is collected on final button press.
    greek_win.setFont(font)
    greek_win.setStyleSheet("background-color: purple;")
female1.clicked.connect(fem_button)

def greek_wi():
    lang_win.hide()
    greek_win.show()
    information.clear()
    gender1.setText("Διάλεξε φύλο")
    male1.setText('Άνδρας')
    female1.setText('Γυναίκα')
    agetxt.setText('Ηλικια')
    infostxt.setText('Πληροφοριες για εσας(π.χ τροπος ζωης)')
    genbutton.setText('Δημιουργία Δίαιτας')
    backbutton.setText("Πισω")
    information.append('Language: Greek')
    res_text.setText('H Διαιτα σας:')
    backbutton2.setText("Πισω")
    ask_button.setText("Εχετε αποριες; Πατηστε εδω")
    send_questbutton.setText('Στειλε')
    backbutton3.setText("Πισω")

Greek.clicked.connect(greek_wi)

def back():
    lang_win.show()
    greek_win.hide()
    greek_win.setStyleSheet("background-color: lightgreen;")
    res_win.hide()
    ask_win.hide()

def back2():
    res_win.show()
    ask_win.hide()

backbutton.clicked.connect(back)
backbutton2.clicked.connect(back)
backbutton3.clicked.connect(back2)

def run_ai():
    global response
    prompt = f"use this list with information {information} in order to create a diet plan"
    print("Prompt:", prompt)
    response = model.generate_content(prompt)
    print("AI Response:", response.text)
    res_show.setMarkdown(response.text.strip())
    res_show.setReadOnly(True)

def ask():
    res_win.hide()
    ask_win.show()
    information.clear()
    prompt2 = f"use this diet {response.text}  and in order to see the question the user asks you should use this {str(ask_line.text())}in order to achieve your goals """
    response2 = model2.generate_content(prompt2)
    print("AI Response:", response2.text)
    ask_area.setMarkdown(response2.text.strip())
    ask_area.setReadOnly(True)

def send_question():
    ask()
    ask_line.clear()

ask_button.clicked.connect(ask)
send_questbutton.clicked.connect(send_question)


def generate_diet():
    """
    Collects all user inputs from the form at once,
    populates the information list, and displays the result screen.
    This is the most reliable way to handle form data.
    """
    # Preserve the language info, which should be the first item
    lang_info = information[0] if information else "Language: Not set"
    information.clear()
    information.append(lang_info)

    # 1. Get Gender from Radio Buttons
    if male1.isChecked():
        information.append(f"Φύλο: {male1.text()}")
    elif female1.isChecked():
        information.append(f"Φύλο: {female1.text()}")

    # 2. Get Age from Line Edit
    age_text = agein.text().strip()
    if age_text:
        information.append(f"Ηλικία: {age_text}")

    # 3. Get additional info from Text Edit
    info_text = infosin.toPlainText().strip()
    if info_text:
        information.append(f"Πρόσθετες Πληροφορίες: {info_text}")

    print("Final information:", information)

    greek_win.hide()
    res_win.show()
    run_ai()
genbutton.clicked.connect(generate_diet)


#language selector backend
def english_wi():
    lang_win.hide()
    greek_win.show()
    information.clear()
    gender1.setText("Select gender")
    male1.setText('Male')
    female1.setText('Female')
    agetxt.setText('Age')
    infostxt.setText('Information about yourself (E.G lifestyle)')
    genbutton.setText('Create Diet')
    backbutton.setText("Back")
    information.append('answer in english')
    res_text.setText('your Diet:')
    backbutton2.setText("back")
    ask_button.setText('Do you have any questions? Press here')
    send_questbutton.setText('Send')
    backbutton3.setText("back")

    
english.clicked.connect(english_wi)

def deutsch_wi():
    lang_win.hide()
    greek_win.show()
    information.clear()
    gender1.setText("Geschlecht auswählen")
    male1.setText('Mann')
    female1.setText('Frau')
    agetxt.setText('Alte')
    infostxt.setText('Informationen für Sie, (z. B. zum Lebensstil)')
    genbutton.setText('Diät erstellen')
    backbutton.setText("zurück")
    information.append("antwort auf Deutsch")
    res_text.setText('Ihre Diät:')
    backbutton2.setText("zurück")
    ask_button.setText('Haben Sie Fragen? Drücken Sie hier')
    send_questbutton.setText('Senden')
    backbutton3.setText("zurück")


deutsch.clicked.connect(deutsch_wi)




app.exec_()