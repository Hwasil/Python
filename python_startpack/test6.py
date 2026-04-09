# 26.04.09
## 라이브러리
import tkinter as tk

c = 0  # <- 전역변수 (함수 밖에 있으면 모두 전역변수, 프로그램 끝날때까지 살아있음, 함수 안에서도 접근 가능 global)

def click():
    global c
    c += 1
    label.config(text=f"{c}번 클릭!")

def show_text():
    text = entry.get()
    label.config(text=text)

window = tk.Tk()  # Tk -> 윈도우 창
window.title("My window")
window.geometry("300x200")  # 창 크키

# 문자 붙이기
label = tk.Label(window, text="Hello World!")
label.pack()

# 버튼
btn = tk.Button(window, text="ck", command=click)
btn.pack()

btn2 = tk.Button(window, text="확인", command=show_text)
btn2.pack()

# 입력창
entry = tk.Entry(window)
entry.pack()

window.mainloop()
