from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Configuração do navegador
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Barra de navegação
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Botão Voltar
        voltar_btn = QAction(QIcon('Icons/return.png'), 'Voltar', self)
        voltar_btn.setStatusTip('Voltar para a página inicial')
        voltar_btn.triggered.connect(self.return_to_home)  # Conectar ao método return_to_home
        navbar.addAction(voltar_btn)

        # Adicionando um espaçador (widget invisível com largura fixa)
        spacer = QLabel()
        spacer.setFixedWidth(10)
        navbar.addWidget(spacer)

        # Botão Recarregar
        recarregar_btn = QAction(QIcon('Icons/Reload.png'), 'Recarregar', self)
        recarregar_btn.setStatusTip('Recarregar a página atual')
        recarregar_btn.triggered.connect(self.browser.reload)
        navbar.addAction(recarregar_btn)

        # Adicionando um espaçador adicional
        spacer = QLabel()
        spacer.setFixedWidth(10)
        navbar.addWidget(spacer)

        # Barra de pesquisa
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.search_bar)

        # Conectar o sinal urlChanged ao método update_url
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        # Obtém o texto da barra de pesquisa e navega para a URL
        q = QUrl(self.search_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    # Método para atualizar a barra de pesquisa com a URL atual
    def update_url(self, q):
        self.search_bar.setText(q.toString())

    # Método para voltar para a página inicial
    def return_to_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName('VegaX')
    app.setWindowIcon(QIcon('VegaX.ico'))

    window = MainWindow()
    sys.exit(app.exec_())
