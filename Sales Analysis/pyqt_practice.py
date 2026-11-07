import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle("Hello!")

        #Setting Layout as Vertical
        self.setLayout(qtw.QVBoxLayout())

        # Label
        my_label = qtw.QLabel("Hello World! Enter your name!")
        my_label.setFont(qtg.QFont('Helvetical',27))
        self.layout().addWidget(my_label)

        #Entry Box
        # entry_box = qtw.QLineEdit(self)
        # entry_box.setObjectName("name_field")
        # entry_box.setText("")
        # self.layout().addWidget(entry_box)


        #  Combo Box
        combo = qtw.QComboBox(self,
                                editable = True,
                                insertPolicy = qtw.QComboBox.InsertAtTop
                            )
        #Add Items to combobox
        lol = "loser"
        combo.addItem("Vishu","GOD")
        combo.addItem("Uma","GodofGods")
        combo.addItem("Prem","SuperGOD")
        combo.addItem("Megha",lol)

        self.layout().addWidget(combo)

        # Create button
        btn = qtw.QPushButton("ENTER",
                                clicked = lambda: press_it())
        self.layout().addWidget(btn)

       

        # Show the app
        self.show()


        def press_it():
            my_label.setText(f'Hello {combo.currentText()}!')
            # entry_box.setText("")          

app = qtw.QApplication([])
mw = MainWindow()


app.exec_()
