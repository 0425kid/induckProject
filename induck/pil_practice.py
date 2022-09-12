import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('사진 불러오기')
root.geometry('800x600')

img = Image.open("C:\\Users\\wkdrl\\induckProject\\induck\\image\\duckImage.png")
img_resize = img.resize((20, 20))
imgimg = ImageTk.PhotoImage(img_resize)
label = tk.Label(image=imgimg)
label.pack()

quit = tk.Button(root, text='종료하기', command=root.quit)
quit.pack()

root.mainloop()


#img_resize.show()
# img_resize.save('data/dst/sample_pillow_resize_nearest.jpg')

# img_resize_lanczos = img.resize((256, 256), Image.LANCZOS)
# img_resize_lanczos.save('data/dst/sample_pillow_resize_lanczos.jpg')