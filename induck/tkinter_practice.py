import tkinter as tk
from PIL import ImageTk, Image

#윈도우.geometry("가로x세로") : 윈도우 창이 띄워질 때의 기본 크기를 설정

#윈도우.resizeable(가로, 세로) : 띄워진 후 변경 가능한 크기를 설정 (보통 0,0으로 수동 크기변경 불가하게 설정)

#이름 = [객체 종류 영어명](윈도우 명, text="텍스트") : 요소를 추가하는 기본 문법

#font : 무조건 영어 이름으로, 글꼴이 있는경우 적용. 굵게, 눕히기 등의 효과도 적용 가능

#command : 입력에 맞게 이벤트를 발생시키는 메인
#command='함수명'

#pack() : 해당 객체를 패킹해 불필요한 공간을 없애주는 함수, 기본적으로 한줄에 하나씩
#grid(row=열, column=행) : pack() 대신에 수동으로 레이아웃 배치d : 레이아웃 배치
#place : 절대 좌표 배치



window = tk.Tk() #윈도우 생성
window.title("Hello") #윈도우 타이틀 설정
window.geometry("800x800")
window.resizable(0,0)

def your_name():
    print(f"Hello {inpt.get()}")
    lbl.configure(text="complete") #라벨의 텍스트 내용을 재설정 가능

#Label : 상자, 텍스트를 넣거나 image attribute를 이용해 이미지도 삽입 가능
lbl = tk.Label(window, text="name", font="D2Coding 20") #윈도우, 내부 텍스트, 글꼴과 크기순으로 입력
lbl.grid(row=1, column=0)
#lbl.pack()

#Entry : 입력 상자
inpt = tk.Entry(window)
inpt.grid(row=1, column=1)
#inpt.pack()

#Button : 버튼
btn = tk.Button(window, text="ok", command=your_name)
btn.grid(row=2, column=1)
#btn.pack()

window.mainloop() #윈도우 띄워두기 (맨 마지막에 실행되어야 함)