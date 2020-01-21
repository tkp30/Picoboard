from PicoBoardAPI import Api
def main():
    api=Api()
    while True:
        if api.getbutton():
            print("按钮被按下")
            print("数据：",api.get())
            print("=================================")
if __name__=="__main__":
    main()
