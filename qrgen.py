import segno
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, 
                             QFrame, QLabel, QHBoxLayout, QVBoxLayout, QGraphicsScene, 
                             QGraphicsView, QGraphicsPixmapItem, QDialog, QTextEdit, QFileDialog)
from PyQt6.QtGui import (QAction, QPixmap, QIntValidator)
from PyQt6.QtCore import (Qt)
from io import BytesIO

class QrGen(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.__license = "".join(open("license.dat", "r").readlines())
        self.setWindowTitle("Qr Code Generator")
        self.resize(400, 400)
        frame = QFrame()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(1,1,1,1)
        frame.setLayout(vbox)
        qrline = self.ui_qr_line()
        qrimage = self.ui_qr_image()
        vbox.addWidget(qrline)
        vbox.addWidget(qrimage)
        self.setCentralWidget(frame)
        self.center()
        
    def ui_qr_line(self):
        action = self.menuBar().addMenu("Action")
        about = self.menuBar().addMenu("About")
        
        generate_action = QAction("Generate", self)
        generate_action.triggered.connect(self.generate_button_clicked)
        action.addAction(generate_action)
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_button_clicked)
        action.addAction(save_action)
        action.addSeparator()
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_button_clicked)
        action.addAction(exit_action)
        about_action = QAction("About", self)
        about_action.triggered.connect(self.about_button_clicked)
        about.addAction(about_action)
        frame = QFrame()
        hbox = QHBoxLayout()
        hbox.setContentsMargins(1,1,1,1)
        frame.setLayout(hbox)
        self.__label = QLineEdit("")
        self.__generate = QPushButton("Generate")
        self.__generate.clicked.connect(self.generate_button_clicked)
        self.__save = QPushButton("Save")
        self.__save.clicked.connect(self.save_button_clicked)
        
        hbox.addWidget(QLabel("Label:"))
        hbox.addWidget(self.__label)
        hbox.addWidget(QLabel("Scale:"))
        self.__scale = QLineEdit("10")
        self.__scale.setValidator(QIntValidator())
        self.__scale.setFixedWidth(30)
        hbox.addWidget(self.__scale)
        hbox.addWidget(self.__generate)
        hbox.addWidget(self.__save)       
        return frame
    
    def ui_qr_image(self):
        frame = QFrame()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(1,1,1,1)
        frame.setLayout(vbox)
        self.__view = QGraphicsView()
        self.__scene = QGraphicsScene()
        self.__view.setScene(self.__scene)
        self.__image = QGraphicsPixmapItem()
        self.__scene.addItem(self.__image)
        vbox.addWidget(self.__view)
        return frame
        
    def generate_button_clicked(self):
        qr = segno.make(self.__label.text())
        buffer = BytesIO()
        qr.save(buffer, kind="png", scale=int(self.__scale.text()))  # QR kodunu PNG formatında belleğe kaydet
        buffer.seek(0)  # Belleğin başına dön
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.read())
        self.__scene.setSceneRect(0,0,pixmap.width(), pixmap.height())
        self.__image.setPixmap(pixmap)
        
    def save_button_clicked(self):
        fname = QFileDialog.getSaveFileName(self,
                                            "Save image",
                                            "",
                                            "PNG image (*.png)")
        if fname:
            file_name = fname[0]
            if ".png" not in file_name:
                file_name = file_name + ".png"
            self.__image.pixmap().save(file_name, "PNG")
            
    def exit_button_clicked(self):
        sys.exit(0)
    
    def about_button_clicked(self):
        about_dialog = QDialog(self)
        about_dialog.setWindowTitle("About")  # Pencere başlığı
        about_dialog.setFixedSize(400, 200)  # Pencere boyutu sabitlendi

        # Yazılar için Dikey Düzen
        layout = QVBoxLayout()
        layout.setContentsMargins(1,1,1,1)
        # Yazıları ve Stil Ayarlarını Ekleyelim
        title_label = QLabel("QR Code Generator V 1.0.0")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Ortala
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #2E86C1;")  # Kalın, büyük ve mavi renk
        version_label = QTextEdit()
        version_label.setText(self.__license)
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Ortala
        version_label.setStyleSheet("font-size: 12px; color: #34495E;")  # Kalın, biraz daha küçük
        # Yazıları Düzen İçine Ekleyelim
        version_label.setReadOnly(True)
        layout.addWidget(title_label)
        layout.addWidget(version_label)
        # Düzeni Pencereye Ayarla
        about_dialog.setLayout(layout)
        # Pencereyi Göster
        about_dialog.exec()
    
    def center(self):
        # Ekranın boyutlarını al
        screen = self.screen()
        screen_geometry = screen.availableGeometry()
        screen_center = screen_geometry.center()

        # Pencerenin boyutlarını al
        window_rect = self.frameGeometry()

        # Pencereyi ekranın ortasına yerleştir
        window_rect.moveCenter(screen_center)
        self.move(window_rect.topLeft())
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    qrgen = QrGen()
    qrgen.setGeometry(100,100, 400, 400)
    qrgen.show()
    sys.exit(app.exec())