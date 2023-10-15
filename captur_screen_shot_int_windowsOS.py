import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PIL import Image, ImageGrab
import subprocess

class ScreenshotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建中央小部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建中央小部件的布局
        layout = QVBoxLayout(central_widget)

        # 创建截图按钮
        screenshot_button = QPushButton("Get Screenshot from Clipboard")
        screenshot_button.clicked.connect(self.getScreenshotFromClipboard)

        layout.addWidget(screenshot_button)

    def getScreenshotFromClipboard(self):
        try:
            # 调用Snipping Tool
            subprocess.run(["snippingtool.exe"])

            # # 尝试从剪贴板获取数据
            # clipboard_data = pyperclip.paste()

            # # 将剪贴板数据转换为字节数据
            # clipboard_bytes = clipboard_data.encode('utf-8')

            # # 将字节数据保存为图像
            # screenshot = Image.open(io.BytesIO(clipboard_bytes))
            screenshot = ImageGrab.grabclipboard()
            screenshot.save("screenshot.png")
            print("Screenshot saved as screenshot.png")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScreenshotApp()
    window.show()
    sys.exit(app.exec())