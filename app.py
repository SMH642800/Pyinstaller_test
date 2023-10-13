from PySide6 import QtWidgets

import sys
import os
import toml

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        if getattr(sys, 'frozen', False):
            # 应用程序被打包
            app_dir = sys._MEIPASS

            config_file_path = os.path.join(app_dir, "config.toml")

            # 创建多行文本，使用<br>标签来表示换行
            path_info = "Application Directory: <br>" + app_dir + "<br><br>"
            path_info += "Current Directory: <br>" + os.path.dirname(os.path.abspath(__file__)) + "<br><br>"
            path_info += "Script File: <br>" + os.path.abspath(__file__) + "<br><br>"
            path_info += "Current Working Directory: <br>" + os.getcwd() + "<br>"
            path_info += "Config file: <br>" + config_file_path + "<br>"

        self.setWindowTitle("Hello World")
        l = QtWidgets.QLabel(path_info)
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()


if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        # 应用程序被打包
        app_dir = sys._MEIPASS
        print(app_dir)

        config_file_path = os.path.join(app_dir, "config.toml")
        print(config_file_path)

        # 檢查是否有 config file
        if not os.path.exists(config_file_path):
            print("file not exsits")
            # 如果文件不存在，创建默认配置
            default_config = {
                "Settings": {
                    "text_font_size": 14,
                    "text_color": "white"
                    # 添加其他配置项
                }
            }
            with open(config_file_path, "w") as config_file:
                toml.dump(default_config, config_file)
            print("file exsits.")

            print(config_file_path)

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()