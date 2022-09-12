import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=810, height=800)
canvas.pack()

for i in range(11):
    canvas.create_line((10+80*i, 0), (10 + 80*i, 800), fill='black', width=1, smooth=False)
    canvas.create_line((10, 80*i), (10 + 800, 80*i), fill='black', width=1, smooth=False)

canvas.create_line((10,0), (10, 800), fill='black', width=1, smooth=False)


window.mainloop()

#print(__name__)
# python 파일.py
# 파일 > 모듈 > 모듈 > 모듈
# 파일 : 진입점, 엔트리포인트, 메인

class Duck:
    def __init__(self, hp):
        self.hp = hp
    def getHp(self):
        return self.hp



a = 10
b = 20
def c():
    return 30