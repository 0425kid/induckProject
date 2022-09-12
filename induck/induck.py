import tkinter as tk
from PIL import ImageTk, Image

#######################  Duck 클래스 설정  #######################
class Duck:
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name
        self.position = (0, 0)
        self.direction = 0 #0:위 1:오른쪽 2:아래 3:왼쪽
        print(f"{self.name} 오리가 {self.getPosition()}에 생성되었습니다")

    def getHp(self):
        return self.hp

    def getPosition(self):
        return self.position

    def getDirection(self):
        if(self.direction==0): return "위쪽"
        elif(self.direction==1): return "오른쪽"
        elif(self.direction==2): return "아래쪽"
        elif(self.direction==3): return "왼쪽"

    def moveTo(self, x, y):
        self.position = (x,y)
        print(f"{self.name} 오리가 {self.getPosition()}로 이동하였습니다.")
    
    def turnRight(self):
        self.direction+=1
        self.direction%=4
        print(f"{self.name} 오리가 {self.getDirection()} 방향을 보고있습니다.")

#######################  Duck 클래스 설정  #######################



#######################  tkinter 기본 설정  #######################
window = tk.Tk() #윈도우 생성
window.title("Hello") #윈도우 타이틀 설정
window.geometry("800x800")
window.resizable(0,0)

def create_lake(row, column):
    global canvas
    global grow
    global gcolumn
    grow = row
    gcolumn = column
    
    canvas = tk.Canvas(window, width=40*row, height=40*column)
    canvas.grid(row=0, column=0)
    for i in range(row):
        canvas.create_line((40*i, 0), (40*i, 40*column), fill='black', width=1, smooth=False)
    for i in range(column):
        canvas.create_line((0, 40*i), (40*row, 40*i), fill='black', width=1, smooth=False)

create_lake(7,18)
    


#좌표축 그리기
# canvas = tk.Canvas(window, width=200, height=200)
# canvas.grid(row=0, column=0)
# for i in range(5):
#     canvas.create_line((40*i, 0), (40*i, 200), fill='black', width=1, smooth=False)
#     canvas.create_line((0, 40*i), (200, 40*i), fill='black', width=1, smooth=False)

#######################  tkinter 기본 설정  #######################

#이미지 미리 로드해둠
img = Image.open("C:\\Users\\wkdrl\\induckProject\\induck\\image\\duckImage_up.png")
img_resize = img.resize((20, 20))

duckimg_up = ImageTk.PhotoImage(img_resize)

img = Image.open("C:\\Users\\wkdrl\\induckProject\\induck\\image\\duckImage_right.png")
img_resize = img.resize((20, 20))

duckimg_right = ImageTk.PhotoImage(img_resize)

img = Image.open("C:\\Users\\wkdrl\\induckProject\\induck\\image\\duckImage_down.png")
img_resize = img.resize((20, 20))

duckimg_down = ImageTk.PhotoImage(img_resize)

img = Image.open("C:\\Users\\wkdrl\\induckProject\\induck\\image\\duckImage_left.png")
img_resize = img.resize((20, 20))

duckimg_left = ImageTk.PhotoImage(img_resize)

duck_direction = 0
duck_position_x = 8
duck_position_y = 8
walk = 40

#라벨 기본설정
duckstamp = tk.Label(image=duckimg_up)
duckstamp.place(x=duck_position_x,y=duck_position_y)


def turn_left():
    global duckstamp
    global duckimg_up
    global duckimg_right
    global duckimg_down
    global duckimg_left
    global duck_direction
    duck_direction-=1
    duck_direction%=4
    if(duck_direction==0): duckstamp.config(image=duckimg_up)
    elif(duck_direction==1): duckstamp.config(image=duckimg_right)
    elif(duck_direction==2): duckstamp.config(image=duckimg_down)
    elif(duck_direction==3): duckstamp.config(image=duckimg_left)

def turn_right():
    global duckstamp
    global duckimg_up
    global duckimg_right
    global duckimg_down
    global duckimg_left
    global duck_direction
    duck_direction+=1
    duck_direction%=4
    if(duck_direction==0): duckstamp.config(image=duckimg_up)
    elif(duck_direction==1): duckstamp.config(image=duckimg_right)
    elif(duck_direction==2): duckstamp.config(image=duckimg_down)
    elif(duck_direction==3): duckstamp.config(image=duckimg_left)

def move():
    global duck_position_x
    global duck_position_y
    if(duck_direction==0): 
        if(duck_position_y <= 8): return
        duck_position_y -= walk
    elif(duck_direction==1):
        if(duck_position_x >= 40*grow - 32): return 
        duck_position_x += walk
    elif(duck_direction==2):
        if(duck_position_y >= 40*gcolumn - 32): return  
        duck_position_y += walk
    elif(duck_direction==3):
        if(duck_position_x <= 8): return   
        duck_position_x -= walk
    duckstamp.place(x=duck_position_x,y=duck_position_y)
    

btn = tk.Button(window, text="move", command=move)
btn.grid(row=2, column=0)

btn = tk.Button(window, text="turn left", command=turn_left)
btn.grid(row=2, column=1)

btn = tk.Button(window, text="turn right", command=turn_right)
btn.grid(row=2, column=2)



lbl = tk.Label(window, text="오리의 이름 : ", font="D2Coding 10")
lbl.grid(row=3, column=0)

window.mainloop() #윈도우 띄워두기 (맨 마지막에 실행되어야 함)

# #print(__name__)
# # python 파일.py
# # 파일 > 모듈 > 모듈 > 모듈
# # 파일 : 진입점, 엔트리포인트, 메인