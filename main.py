from MyWidgets import *

def main():
	qpp = QApplication(sys.argv)
	myWeb = MyWebBrowser()
	sys.exit(qpp.exec_())

if __name__ == "__main__":
	main()