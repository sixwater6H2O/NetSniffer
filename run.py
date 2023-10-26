from sniffer import *
from globalVal import globalVal,init_globalVal

if __name__ == "__main__":
    ## 实例化
    app = QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()

    ## init globalVal
    init_globalVal()
    globalVal.sniff_form = Ui_Form()
    globalVal.sniff_form.setupUi(widgets)

    widgets.setWindowTitle("网路嗅探器")
    widgets.show()

    sys.exit(app.exec_())