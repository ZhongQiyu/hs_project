# 11/24-11/25 (Thanksgiving)

# Task 0. User Control

# Exercise: write a program that
# - defines a range on the screen where the mouse CAN BE put in
# - detect the mouse and determine if the mouse is within the range
# - if the mouse is not within the range, report where it is and print a warning message
# - otherwise print "LEGIT LOCATION"

dims = [200, 200, 200, 200]
X = 200
Y = 200
Width = 200
Height = 200

def mouse_check(xory, pos, add):
    if pos >= xory and pos <= (xory + add):
        return "Legit Location!"
    else:
        return "Warning: Not In range!"

def on_move(x, y):
    if mouse_check(x, X, Width) == "Legit Location!" and mouse_check(y, Y, Height) == "Legit Location!":
        print("Legit Location!")
    else:
        print(f"Warning! Mouse is not in range! Mouse is at {x}, {y}")

"""
# define the Listener class
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
"""

# 11/24-11/25 HW:

# 1. debug and simplify the code for the Exercise, even more. there is a major error and a minor refactoring to do.

# 2. Exercise for pynput.keyboard

# - detects the average frequency for pressing each key
#   - e.g. since the timing session starts, the frequencies are recorded, and the average is taken by frequency/total_time_passed
#   - when the average frequency is larger than a certain self-defined threshold, report the anomaly
#   - when it is the opposite case, report the stability

# - *create listeners for both the mouse and the keyboard, and embed the functions into a Python class.
#   - when we invoke the class, would we involve any issue? Why?
#   - print the information of the process for both listeners. give a try.



"""
在眼动追踪项目中建立数据管道用于分析，通常涉及以下几个主要步骤:

1. 数据采集
从眼动追踪设备实时获取数据，包括图像和可能的传感器数据。

2. 数据预处理
对采集的原始数据进行清洗和格式化，例如，对图像进行滤波、裁剪、灰度化等预处理操作。

3. 特征提取
分析预处理后的数据，提取眼动特征，如瞳孔位置、眼睛的开闭状态、注视点等。

4. 事件检测
利用提取的特征，识别眼动事件，如固定注视、快速眼动（Saccades）、眨眼等。

5. 数据存储
将处理的数据存储在数据库或文件系统中，以便后续分析。

6. 实时分析
对实时数据进行分析，根据业务需求生成即时反馈，如疲劳检测、注意力偏移等。

7. 历史数据分析
对累积的历史数据进行深入分析，以识别长期趋势、模式或进行科研研究。

8. 可视化和报告
创建可视化的报告或仪表板，向用户展示分析结果和洞察。

实现数据管道: 在 Python 中，可以使用各种库来构建数据管道的各个环节。以下是一个简化的数据管道实现示例:
"""



# 12/1-12/2

# 12/1:

# Task 0. Review of Data Structures
# - *make a program that emulates a ChatGPT
#   - a user input is prompted, assumed as a complete English prompt upon the GUI.
#   - all the stopping notations are recorded, e.g. period, comma, colon, semicolon, exclamation mark, question mark, etc. the same for letters.
#   - try to find the pattern for a user's usage of notations: do they always include, or they do not?
#   - *try to extract the words out of the input, and store them in a prompt dictionary.

class myGTP():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("My GTP")
        self.root.resizable(False, False)
        self.patterns = {  # First array is for true and falses, second is for status
            "coma": [],
            "semicolon": [],
            "period": [],
            "question_mark": [],
            "exclamation_mark": []
        }

        self.textbox = tk.Text(self.root, height=3, font=("Arial", 18))
        self.textbox.pack(pady=3)

        self.button = tk.Button(self.root, font=("Arial", 18), text="GPTlize", command=self.GPTlize)
        self.button.pack(pady=3)
        self.root.mainloop()

    def get_index(self, string, symbol):
        splited = string
        frequencies = []
        for letter_index in range(len(splited)):
            if splited[letter_index] == symbol:
                frequencies.append(letter_index)
        return frequencies

    def get_count(self, string, symbol):
        array = self.get_index(string, symbol)
        return len(array)

    def translate_symbol(self, symbol):
        translated_symbol = ""
        if symbol == ".":  #
            translated_symbol = "coma"  # "comma"
        elif symbol == ";":
            translated_symbol = "semicolon"
        elif symbol == ".":
            translated_symbol = "period"
        elif symbol == "?":
            translated_symbol = "question_mark"
        elif symbol == "!":
            translated_symbol = "exclamation_mark"
        return translated_symbol

    def GPTlize(self):
        txt = self.textbox.get("1.0", tk.END).strip()
        text = txt.split()

        symbol_list = [",", ";", ".", "?", "!"]

        for symbol in symbol_list:
            print(symbol)  # debug from here
            print(self.translate_symbol(symbol))
            self.patterns[self.translate_symbol(symbol)].append(self.get_index(text, symbol))

        print(self.patterns)

# obj = myGTP()

"""
for key in self.patterns:
    has = 0
    nothas = 0
    status = ""
    for boolean in self.patterns[key][0]:
        if boolean == False:
            nothas += 1
        elif boolean == True:
            has += 1
    if (has > 0 and nothas > 0):
        status == "Sometimes"
    elif (nothas == 0):
        status = "Always"
    elif (has == 0):
        status = "Never"
    else:
        status = "Unknown (possible error)"
    self.patterns[key][1].append(status)
"""

# 12/1 HW: Fix myGTP so that it fully functions



# 12/2:

# Task 0. Eye-Tracking and Tiredness Detection

# - OpenCV
#   - Read the Introduction of OpenCV library in Python (or C++) up to Image Resizing with OpenCV:
#   - https://learnopencv.com/getting-started-with-opencv/. Leave comments for the parts where you do not understand.
#   - Compare the ideas of the basic 'processing' routines we have covered so far. Are they similar? If not, what makes you get around so?

# - MediaPipe
#   - Take a picture of your own. Change the format as if you need to.
#   - Use cv2.imread, face_detection and drawing_utils in mediapipe.solutions to detect your face.
#   - Interpret the results. How is the image processed? What does each parameter in the detection method do? How good a result would be?
#   - *Can we have a better result by changing our parameters?



# Task 1. User Interaction:

# - GUI Design and Control: turtle
#   - Draw any shape that assimilates an 3D object.
#   - e.g. it can be a cone, a cube, a pyramid, etc.
#   - Reveal the angle of view as well as you can.

"""
import turtle
from turtle import *

t = Turtle()

def cube(x,y,w):
    ratio = 0.8
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(w)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.left(45)
    t.forward(w * ratio)
    t.right(45)
    t.forward(w)
    t.right(135)
    t.forward(w * ratio)
    t.right(180)
    t.forward(w * ratio)
    t.right(135)
    t.forward(w)
    t.right(45)
    t.forward(w * ratio) 
"""

# Task 2: GUI Design and Control w/ tkinter and pynput

# - GUI Design and Control: tkinter
#   - The event-oriented programming toolset, assmimilating JavaScript's DOM parsing
#   - Inherit the positions from the data provided within Python's scope

# - Build a simple program that allows the user to:
#   - Click on a button that prompts the basic information; parse the information into a list; display the list.
#   - Change the color of the window. The choice of colors can be either user-input or built-in. If user-input, include another button that behaves similarly as the first one does.
#   - Make a timer that records the time since the user runs the program. Before the user shut the program down, display the total amount of time that the program runs in a pop-up window.
#   - detect the average frequency for pressing each key
#       - e.g. since the timing session starts, the frequencies are recorded, and the average is taken by frequency/total_time_passed
#       - when the average frequency is larger than a certain self-defined threshold, report the anomaly
#       - when it is the opposite case, report the stability
#   - create listeners for both the mouse and the keyboard, and embed the functions into a Python class.
#       - when we invoke the class, would we involve any issue? Why?
#       - print the information of the process for both listeners. give a try.

import time
import pynput
from pynput.mouse import Listener
from pynput import keyboard

class pynput_frequency():
    def __init__(self):
        self.key_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.key_data = {}

        for i in self.key_dict:
            self.key_data[i] = 0

        for key in keyboard.Key:
            self.key_data[str(key)] = 0

        print(self.key_data)

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        self.key_data[key_char] += 1

import time

class timer():
    def __init__(self):
        self.t = 0
        while True:
            self.change_time()

    def change_time(self):
        self.t += 1
        time.sleep(1)

def calculate_frequency():
    frecuency_obj = pynput_frequency()
    timer_obj = timer()
    time_value = timer_obj.time

# calculate_frequency()

# 12/2 HW:

# - Add tools in tk and cv2 to ensure the hardware is real-time facilitating with mouse & keyboard
# - Combine the eye-tracking module that we have covered in the middle of this past month
# - Communicate with Marisabel about each .py files that needs revision

# Task 0: GUI
# - Build the tk and pynput module for handling:
#   - A user's input with the mouse and the keyboard. 1 click of mouse counts as 1, and 1 press of any non-ESC key counts as 1. Separate the counters.
#   - A user's movement on the camera. Define a certain distance of 1 unit's bias, and move on with another.
#   - Any potential components addition onto the hardware.
# - Collect the input data so that they can be dumped into an array.

# Task 1: Detection with OpenCV and pycharm
# - Define feature arrays so that we can also find:
#   - Eyebrows
#   - Mouth
#   - Nose
# - Change the parameters for the model that we have had.
#   - Try to form different combinations. Do they populate different results? How do they differ?
#   - Can the features in the previous questions be used as auxiliary components for eye-tracking?
#   - Embed this parameter-change module into the code that we have.

# Task 2: Analytics for the Detection
# - Analyze the accuracy for the detection task.
#   - Will we be able to find alternatives for metrics other than accuracies, or we actually do not?
#   - Create another module if needed, in terms of getting the analytics stored and displayed.
# - How we can show them to the external audience?
#   - Create a dashboard if we need one. In Python there is a module called matplotlib.
#   - Can we embed them into our GUI module?

# REMEMBER THE MEMBERSHIPS OF TRIAL FOR PYCHARM IN HIS MACHINE

# LEGACY FROM tk

import tkinter as tk
from PIL import Image, ImageTk
import threading

class MyGui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("My Program")
        self.root.resizable(False, False)

        """Timer"""
        self.timer_text = tk.Label(self.root, text="Time Elapsed: 0", font=("Arial", 18))
        self.timer_text.pack(padx=10, pady=10)
        self.time = 0
        self.update_timer()

        """Data to list"""
        "Need to revise the trimming part"
        self.text_label = tk.Label(self.root, text="Data --> List Converter", font=("Arial", 20))
        self.text_label.pack()

        self.textbox = tk.Text(self.root, height=1, font=("Arial", 18))
        self.textbox.pack()

        self.list_convert = tk.Button(self.root, text="Convert to list", font=("Arial", 18), command=self.show_list)
        self.list_convert.pack()

        self.result = tk.Label(self.root, text="", font=("Arial", 20))
        self.result.pack()

        """Color Changer"""
        self.change_background_color_button = tk.Button(self.root, text="Random Color Change", font=("Arial", 18),
                                                        command=self.change_color)
        self.change_background_color_button.pack()
        self.colors = ["blue", "red", "pink", "green", "yellow", "brown", "purple", "white"]

        self.root.mainloop()

    def update_timer(self):
        self.timer_text.config(text=f"Time Elapsed: {self.time}")
        self.time += 1
        self.root.after(1000, self.update_timer)  # Update every 1000ms (1 second)

    def show_list(self):
        text = self.textbox.get("1.0", tk.END).strip()
        result_array = text.split(" ")
        self.result.config(text=str(result_array))

    def change_color(self):
        import random
        random_color = self.colors[random.randint(0, len(self.colors) - 1)]
        self.root.configure(bg=random_color)

    # ****** TO TEST ******
    def setup_canvas(self):
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()
        # 画一个简单的矩形
        self.canvas.create_rectangle(50, 50, 150, 150, fill="blue")

    def setup_camera(self):
        self.camera_button = tk.Button(self.root, text="Open Camera", command=self.open_camera)
        self.camera_button.pack()

    def open_camera(self):
        # 创建一个新窗口
        self.camera_window = tk.Toplevel(self.root)
        self.camera_label = tk.Label(self.camera_window)
        self.camera_label.pack()

        # 启动一个线程来捕捉摄像头图像
        self.camera_thread = threading.Thread(target=self.capture_image)
        self.camera_thread.start()

    def capture_image(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, frame = self.cap.read()
            if ret:
                # 将 OpenCV 图像格式转换为 Tkinter 可用的格式
                cv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv_img)
                imgtk = ImageTk.PhotoImage(image=img)
                self.camera_label.imgtk = imgtk
                self.camera_label.configure(image=imgtk)
            self.camera_label.after(20, self.capture_image)
    # ****** TO TEST ******

"""
# 在主函数中创建 GUI 实例
if __name__ == "__main__":
    gui = MyGui()
    gui.setup_camera()
"""



# 12/8-12/9

# 12/8

# Project Module 1: AI Introduction (and Modeling)

# - AI and scikit-learn
#   - We deal with arrays of data since the beginning of the class. Write a program that takes an user input of just an integer (n; n <= 8), and then:
#   - Generate an n-dimensional array of (0) zeroes, (1) ones, (2) random integers, and (3) random floating point numbers.
#   - In our final project, we would be dealing with image data.
#       - How can the images be decomposed into meaningful units? Do we need decomposition?
#       - How can the n-dimensional arrays be applied to the processes?
#   - *Write a program that:
#       - Takes a complete user input of an image stored in their local computer, and
#       - Transform that image into a black-and-white one.

# - CV
#   - ...

"""
import cv2
import dlib

# 加载面部检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 您需要下载这个预训练模型

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # 假设眼睛是第37到第42点
        for n in range(36, 42):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC键
        break

cap.release()
cv2.destroyAllWindows()
"""

# Project Module 2: Eyes Blink Engine

# - MediaPipe: Face Mesh
#   - Feature Detection
#   - Feature Construction
#   - ...

# - cv2: Web Cam
#   - Frames and Landmarks
#   - Video Capture
#   - ...

import time
import turtle
import pynput
import threading
import tkinter as tk

class MyGUI():
    def __init__(self):
        # Implement the main window
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("AI Timetracker")
        self.root.resizable(True, True)
        self.data = []  # 存储眼动数据
        self.running = False

        # Put the input frame, button, and canvas
        self.cursor_interval = self.create_input_box("Cursor Movement Interval (seconds):")
        self.keyboard_interval = self.create_input_box("Keyboard Typing Interval (seconds):")
        self.start_button = tk.Button(self.root, text="Start Tracking", command=self.start_tracking)
        self.stop_button = tk.Button(self.root, text="Stop Tracking", command=self.stop_tracking, state=tk.DISABLED)
        self.canvas = tk.Canvas(self.root, width=400, height=200)

        # Set the layout
        self.start_button.pack()
        self.stop_button.pack()
        self.canvas.pack()

        # Create the drag bar
        self.make_drag_bar()
        self.root.mainloop()

    def start_tracking(self):
        self.running = True
        threading.Thread(target=self.collect_data).start()

    def stop_tracking(self):
        self.running = False

    def create_input_box(self, label_text):
        """ Helper function to create a label and entry box. """
        label = tk.Label(self.root, text=label_text)
        label.pack()
        entry = tk.Entry(self.root)
        entry.pack()
        return entry

    def create_entry_on_canvas(canvas, x, y, width):
        # 创建一个 Entry 控件，并返回其引用
        entry = tk.Entry(canvas, width=width)
        canvas.create_window(x, y, window=entry, anchor=tk.NW)
        return entry

    def collect_data(self):
        while self.running:
            # 假设 collect_eye_data() 是收集眼动数据的函数
            data_point = self.collect_eye_data()
            self.data.append(data_point)
            time.sleep(0.1)  # 模拟数据收集的时间间隔

    def collect_eye_data(self):
        # 这里应该是与眼动追踪硬件交互的代码
        # 现在我们只是模拟一些数据
        return {'timestamp': time.time(), 'x': 0, 'y': 0}

    def process_data(self):
        while self.running:
            if self.data:
                # 处理数据
                processed_data = self.process_eye_data(self.data)
                self.update_gui_with_processed_data(processed_data)
                self.data = []  # 重置数据列表
            time.sleep(0.1)  # 模拟处理数据的时间间隔

    def process_eye_data(self, data):
        # 处理眼动数据的逻辑
        pass

    def update_gui_with_processed_data(self, data):
        # 这里需要将线程安全的方法更新 GUI
        pass

    def on_drag_start(self, event):
        # Record the item and its location
        self.drag_data = {"x": event.x, "y": event.y, "item": self.circle}

    def on_drag_motion(self, event):
        # Compute how much the mouse has moved
        delta_x = event.x - self.drag_data["x"]

        # Get the current position of the circle
        coords = self.canvas.coords(self.drag_data["item"])
        new_x1 = coords[0] + delta_x
        new_x2 = coords[2] + delta_x

        # Check if the new position is within the bounds of the bar
        if new_x1 >= self.bar_start - self.circle_radius and new_x2 <= self.bar_end + self.circle_radius:
            # Move the object the appropriate amount
            self.canvas.move(self.drag_data["item"], delta_x, 0)

        # Record the new position
        self.drag_data["x"] = event.x

    def make_drag_bar(self):
        self.bar_start = 50
        self.bar_end = 350
        self.bar_top = 50
        self.bar_bottom = 50
        self.canvas.create_line(self.bar_start, self.bar_top, self.bar_end, self.bar_bottom, width=10)
        self.circle_radius = 10
        self.circle = self.canvas.create_oval(90 - self.circle_radius, 40, 110 - self.circle_radius, 60, fill='blue')
        self.canvas.tag_bind(self.circle, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.on_drag_motion)

# my_obj = MyGUI()

# HW:
# - Build a complete, running GUI even w/o the true functions
# - Call the libraries that are invoking the system-level file operations
# - *Write test methods for the written MyGUI class



# 12/9

# API:
# Trace how often a user hits the keyboard every minute, for every key
# Trace how often the user changes the area where mouse is hovered
# Trace how often the user blinks their eyes

# GUI:
# - scale the window to fit your screen (e.g. mine is 2560*1600); can be 1920*1200
# - relocate the statistics as a transparent box in top-left/top-right/bottom-left/bottom-right
# - design where the buttons and dragger would be (this will be part of my tasks)
# Hint: What do you need to define? Why and how?

# MAIN LAYOUT:
# Hint: What do you need to define? Why and how?
# 1. Title (AI Timetracker)
# 2. User Usage
# 2.1 Total blink count:
# - how often the user blinks their eyes: blinks per minute rate (constantly updated), maximum blink count until break
# - bar dragger for person to select how strict the timer will be (Maximum blink count until break is needed
# - GUI for break (Normally hidden)
# 2.2 Total time mouse usage count:
# - how often the user changes the area where mouse is hovered
# 2.3 Total keyboard hit count:
# - for every key, how often a user hits the keyboard every minute

import turtle
import tkinter as tk
#import pynput
import time

class myGui():
    """/////////////////////////////////////////////////////////////////Constructor////////////////////////////////////////////////////////////////////""" 
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("AI Timetracker") # program title
        self.root.resizable(True, True)
        self.root.resizable(True, True)

        self.title_txt = tk.Label(self.root, text = "AI Timer", font = ("Arial", 20)) # program window, at the top
        self.title_txt.pack()
        
        self.make_drag_bar()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.strictness_textbox = tk.Text(self.frame, font=("Arial", 20), height = 1, width = 5)
        self.button = tk.Button(self.frame, text="Set Strictness", font=("Arial", 20), command = self.onclick_updateBarText)
        # Place widgets using grid
        self.strictness_textbox.grid(row=0, column=0)
        self.button.grid(row=0, column=1)
        #_tkinter.TclError: cannot use geometry manager grid inside . which already has slaves managed by pack

        #tk.Entry()

        self.bar_text = tk.Label(self.root, text = "Max blink count (Strictness): 0", font = ("Arial", 20))
        self.bar_text.pack()

        self.total_time_elapsed = tk.Label(self.root, text = "Total Time Elapsed: 0", font = ("Arial", 20))
        self.total_time_elapsed.pack()
        self.total_time_count = 0
        self.update_total_time_count()

        self.total_blink_count = tk.Label(self.root, text = "Total Blink Count: 0", font = ("Arial", 20))
        self.total_blink_count.pack()

        self.average_blink_rate = tk.Label(self.root, text = "Average Blink Rate: 0", font = ("Arial", 20))
        self.average_blink_rate.pack()

        self.alarm = tk.Label(self.root, text = "You need a break!", font = ("Arial", 30))
        #self.alarm.pack()

        self.root.mainloop()

    """/////////////////////////////////////////////////////////////////Drag bar////////////////////////////////////////////////////////////////////""" 

    def make_drag_bar(self):
        self.canvas = tk.Canvas(self.root, width=400, height=100)
        self.canvas.pack()
        # Define bar coordinates
        self.bar_start = 50
        self.bar_end = 350
        self.bar_top = 50
        self.bar_bottom = 50

        # Create a bar on the canvas
        self.canvas.create_line(self.bar_start, self.bar_top, self.bar_end, self.bar_bottom, width=10)
        # Define circle size
        self.circle_radius = 10
        # Adjust the initial position of the circle to be at the edge of the bar
        circle_x = self.bar_start + self.circle_radius
        # Create a circle on the bar
        self.circle = self.canvas.create_oval(circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60, fill='blue')
        # Bind mouse events to the circle
        self.canvas.tag_bind(self.circle, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        # Record the item and its location
        self.drag_data = {"x": event.x, "y": event.y, "item": self.circle}

    def on_drag_motion(self, event):
        # Compute the new position based on the mouse x-coordinate
        new_x1 = event.x - self.circle_radius
        new_x2 = event.x + self.circle_radius

        # Check if the new position is within the bounds of the bar
        if new_x1 >= self.bar_start - self.circle_radius and new_x2 <= self.bar_end + self.circle_radius:
            # Calculate the amount to move
            current_coords = self.canvas.coords(self.drag_data["item"])
            move_x = event.x - (current_coords[0] + self.circle_radius)

            # Move the object the appropriate amount
            self.canvas.move(self.drag_data["item"], move_x, 0)
            # Update the bar text to reflect the new position
            self.updateBarText()

    def onclick_updateBarText(self):
        # Read the value from the textbox and convert it to an integer
        try:
            count = int(self.strictness_textbox.get("1.0", tk.END).strip())
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            return

        max_count = 300  # Maximum value for strictness; try to get the input, but not using input()
        bar_length = self.bar_end - self.bar_start  # Length of the bar

        if 0 <= count <= max_count:
            # Scale the position on the bar according to the strictness value
            scaled_position = (count / max_count) * bar_length
            
            # Calculate the actual x-coordinate on the canvas
            circle_x = self.bar_start + scaled_position

            # Update the position of the circle
            self.canvas.coords(self.circle, circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60)
            self.updateBarText()
        else:
            print(f"Invalid range! Please enter a value between 0 and {max_count}.")

    def update_bar_text(self):
        coords = self.canvas.coords(self.circle)
        # Calculate the current x-coordinate (use the average of the x-coordinates of the left and right sides of the circle)
        current_x = (coords[0] + coords[2]) / 2
        self.bar_count = current_x - self.bar_start # either something between 60 and 120
        self.bar_text.config(text=f"Max blink count (Strictness): {self.bar_count:.0f}")
        
    """///////////////////////////////////////////////////////////////////Update Total Time Elapsed Function//////////////////////////////////////////////////////////////////""" 

    def change_total_time_count(self):
        self.total_time_elapsed.config(text=f"Total Time Elapsed: {self.total_time_count}")
        self.total_time_count += 1
        self.root.after(1000, self.change_total_time_count) 

# my_obj = myGui()

# 12/9 HW:

# 1. GUI:
# - scale the window to fit your screen (e.g. mine is 2560*1600); can be 1920*1200
# - relocate the statistics as a transparent box in top-left/top-right/bottom-left/bottom-right
# - design where the buttons and dragger would be (this will be part of my tasks)

# 2. AI (numpy, pandas, scikit-learn, matplotlib, etc.):
# - fit the given, sampled eye-moving dataset with linear regression, using different combinations of parameters
# - set up the pipeline of dumping the simulated data, and try to visualize them using 2-D coordinates
# - make best attempts to do an analytical pipeline for the GUI that we have built; this might be easier than the previous task

# 3. AI (opencv-python and mediapipe)
# - use the photo that you took upon yourself last time, and try to detect the face. choose a model.
#   - how is the performance? do we need to tune and why? after 1-3 rounds of tuning, are we getting better results?
#   - enlarge your image dataset to be up to 10 sefies, and try to vary the angles. use the same model. how is the performance?
# - change the view to extract the features of the eyes instead of the whole face.
#   - how to store and to re-use the features instead of putting them as-is?
#   - apply a bit of extraction when the face has different angles. what do we need to change?

# 4. Embeddings:
# - aggregate the GUI part with the first AI one.
# - *aggregate the two AI parts.

###### YOUR CODE HERE ######



# 12/15-12/16

# Project Module 3: Mouse and Keyboard Tracker

# - Keyboard and Mouse Tracker
#   - Define a callback function for mouse events (pynput.mouse.Listener.stop)
#   - Define a callback function for keyword events (pynput.keyboard.Listener.stop, pynput.keyboard.Key, and pynput.keyboard.KeyCode)
#   - Track user activity (threading.Thread and StopException)
#   - Run Tracker
#   - Test Tracker

# Project Module 4: Activity and Inactivity Engine

# - Simulate Data
#   - simulate_blink_rate(num_intervals):
#   - simulate_usage_time(session_duration_minutes, max_interval_duration_minutes):
#   - simulate_inactivity(usage_data):
#   - simulate_activity_labels(inactivity_data, activity_data, threshold_ratio, activity_threshold):
#   - train_model

# - Predict

import time
import threading
import tkinter as tk
from PIL import Image, ImageTk

import cv2
from pynput import keyboard, mouse
import mediapipe as mp

"""
class MyGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Eye and Keyboard/Mouse Tracker")
        self.root.state('zoomed')

        self.is_running = True
        self.cap = cv2.VideoCapture(0)
        self.setup_ui_components()

        # MediaPipe 面部标记配置
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        self.lbl_eye_data = tk.Label(self.root, text="Eye Data: Waiting for data...")
        self.lbl_eye_data.pack()

        self.lbl_key_data = tk.Label(self.root, text="Key Data: None")
        self.lbl_key_data.pack()

        self.lbl_mouse_data = tk.Label(self.root, text="Mouse Data: None")
        self.lbl_mouse_data.pack()

        # 启动键盘和鼠标监听
        self.start_listeners()

        # 启动MediaPipe线程
        threading.Thread(target=self.mediapipe_thread, daemon=True).start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def setup_ui_components(self):
        self.video_frame = tk.Canvas(self.root, bg='black')
        self.video_frame.pack(fill='both', expand=True)

        label_style = {"font": ("Arial", 20), "bg": "black", "fg": "white"}
        self.total_time_elapsed = tk.Label(self.root, text="Total Time Elapsed: 0", **label_style)
        self.total_time_elapsed.place(x=700, y=60)
        self.total_time_count = 0
        self.update_total_time_count()

        self.total_blink_count = tk.Label(self.root, text="Total Blink Count: 0", **label_style)
        self.total_blink_count.place(x=20, y=20)

        self.average_blink_rate = tk.Label(self.root, text="Average Blink Rate: 0", **label_style)
        self.average_blink_rate.place(x=20, y=60)

        self.make_drag_bar()

        self.start_video_thread()

    def update_total_time_count(self):
        self.total_time_elapsed.config(text=f"Total Time Elapsed: {self.total_time_count}")
        self.total_time_count += 1
        self.root.after(1000, self.update_total_time_count)

    def make_drag_bar(self):
        self.canvas = tk.Canvas(self.root, width=400, height=100)
        self.canvas.place(x=700, y=100)  # 放置拖动条

        self.bar_start = 50
        self.bar_end = 350
        self.bar_top = 50
        self.bar_bottom = 50
        self.circle_radius = 10

        self.canvas.create_line(self.bar_start, self.bar_top, self.bar_end, self.bar_bottom, width=10)
        circle_x = self.bar_start + self.circle_radius
        self.circle = self.canvas.create_oval(circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60, fill='blue')

        self.canvas.tag_bind(self.circle, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        # Record the item and its location
        self.drag_data = {"x": event.x, "y": event.y, "item": self.circle}

    def on_drag_motion(self, event):
        # Compute the new position based on the mouse x-coordinate
        new_x1 = event.x - self.circle_radius
        new_x2 = event.x + self.circle_radius

        # Check if the new position is within the bounds of the bar
        if new_x1 >= self.bar_start - self.circle_radius and new_x2 <= self.bar_end + self.circle_radius:
            # Calculate the amount to move
            current_coords = self.canvas.coords(self.drag_data["item"])
            move_x = event.x - (current_coords[0] + self.circle_radius)

            # Move the object the appropriate amount
            self.canvas.move(self.drag_data["item"], move_x, 0)
            # Update the bar text to reflect the new position
            self.update_bar_text()

    def update_bar_text(self):
        coords = self.canvas.coords(self.circle)
        # Calculate the current x-coordinate (use the average of the x-coordinates of the left and right sides of the circle)
        current_x = (coords[0] + coords[2]) / 2
        max_count = 300
        self.bar_count = ((current_x - self.bar_start) / (self.bar_end - self.bar_start)) * max_count
        self.bar_text.config(text=f"Max blink count (Strictness): {int(self.bar_count)}")

    def on_click_update_bar_text(self):
        # Read the value from the textbox and convert it to an integer
        try:
            count = int(self.strictness_textbox.get("1.0", tk.END).strip())
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            return

        max_count = 300  # Maximum value for strictness; try to get the input, but not using input()
        bar_length = self.bar_end - self.bar_start  # Length of the bar

        if 0 <= count <= max_count:
            # Scale the position on the bar according to the strictness value
            scaled_position = (count / max_count) * bar_length
            
            # Calculate the actual x-coordinate on the canvas
            circle_x = self.bar_start + scaled_position

            # Update the position of the circle
            self.canvas.coords(self.circle, circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60)
            self.update_bar_text()
        else:
            print(f"Invalid range! Please enter a value between 0 and {max_count}.")

    def start_tracking(self):
        self.running = True
        self.data_thread = threading.Thread(target=self.collect_and_process_data, daemon=True)
        self.data_thread.start()

    def stop_tracking(self):
        self.running = False
        if self.data_thread.is_alive():
            self.data_thread.join()

    def create_input_box(self, label_text):
        # Helper function to create a label and entry box.
        label = tk.Label(self.root, text=label_text)
        label.pack()
        entry = tk.Entry(self.root)
        entry.pack()
        return entry

    def create_entry_on_canvas(canvas, x, y, width):
        # Create an Entry component to embed in the canvas.
        # 创建一个 Entry 控件，并返回其引用
        entry = tk.Entry(canvas, width=width)
        canvas.create_window(x, y, window=entry, anchor=tk.NW)
        return entry

    def start_video_thread(self):
        threading.Thread(target=self.video_loop, daemon=True).start()

    def start_listeners(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def on_key_press(self, key):
        try:
            key_data = f"Key pressed: {key.char}"
        except AttributeError:
            key_data = f"Special key pressed: {key}"
        self.lbl_key_data.config(text=key_data)

    def on_mouse_move(self, x, y):
        mouse_data = f"Mouse moved to ({x}, {y})"
        self.lbl_mouse_data.config(text=mouse_data)

    def mediapipe_thread(self):
        while self.is_running:
            ret, frame = self.cap.read()
            if ret:
                # 处理MediaPipe
                results = self.face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        self.update_eye_data(face_landmarks)
            cv2.waitKey(1)

    def update_eye_data(self, keypoints):
        # 提取眼睛关键点数据
        eye_data = "Eye keypoints: "
        for point in keypoints[36:48]:  # 假设这些点是眼部关键点
            eye_data += f"({point[0]:.2f}, {point[1]:.2f}) "
        self.lbl_eye_data.config(text=eye_data)

    def video_loop(self):
        # Make a loop for the video so that the videos can be presented.
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # 获取视频的原始宽高
                orig_height, orig_width = frame.shape[:2]

                # 获取窗口大小
                window_width = self.root.winfo_width()
                window_height = self.root.winfo_height()

                # 计算新尺寸，保持宽高比
                aspect_ratio = orig_width / orig_height
                new_width = int(window_height * aspect_ratio)
                new_height = window_height

                # 如果新宽度大于窗口宽度，则按照宽度比例调整
                if new_width > window_width:
                    new_width = window_width
                    new_height = int(window_width / aspect_ratio)

                # 调整视频帧大小
                frame = cv2.resize(frame, (new_width, new_height))

                # 将视频帧放在 Canvas 中央
                x_pos = (window_width - new_width) // 2
                y_pos = (window_height - new_height) // 2

                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.video_frame.create_image(x_pos, y_pos, image=self.photo, anchor=tk.NW)

            self.root.after(10, self.video_loop)

    def collect_eye_data(self):
        simulator = ActivitySimulator()
        usage_data, inactivity_data, activity_labels = simulator.simulate_data()
        return {'usage_data': usage_data, 'inactivity_data': inactivity_data, 'activity_labels': activity_labels}

    def process_eye_data(self, data):
        total_blinks = sum(data['usage_data'])  # 假设眼动活动次数
        average_blink_rate = total_blinks / len(data['usage_data']) if data['usage_data'] else 0
        need_break = "Yes" if "break needed" in data['activity_labels'] else "No"
        return {'total_blinks': total_blinks, 'average_blink_rate': average_blink_rate, 'need_break': need_break}

    def update_gui_with_processed_data(self, data):
        self.total_blink_count.config(text=f"Total Blink Count: {data['total_blinks']}")
        self.average_blink_rate.config(text=f"Average Blink Rate: {data['average_blink_rate']:.2f}")
        self.alarm.config(text=f"You need a break: {data['need_break']}")
        # 根据需要更新其他 GUI 元素

    def process_data(self):
        while self.is_running:
            if self.data:
                # 处理数据
                processed_data = self.process_eye_data(self.data)
                self.update_gui_with_processed_data(processed_data)
                self.data = []  # 重置数据列表
            time.sleep(0.1)  # 模拟处理数据的时间间隔

    def collect_data(self):
        while self.is_running:
            data_point = self.collect_eye_data()
            processed_data = self.process_eye_data(data_point)
            self.root.after(0, lambda: self.update_gui_with_processed_data(processed_data))
            time.sleep(0.1)  # 根据需要调整时间间隔

    def on_closing(self):
        self.is_running = False  # 设置标志为 False，通知循环终止
        if self.cap.isOpened():
            self.cap.release()  # 释放摄像头资源
        self.root.destroy()  # 销毁窗口

    def run(self):
        self.root.mainloop()
        self.running = False
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
        self.cap.release()

app = MyGUI()
app.root.mainloop()
"""

"""
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading
from pynput import keyboard, mouse
import random
import time

class MyGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Eye and Keyboard/Mouse Tracker")
        self.root.state('zoomed')

        self.is_running = True
        self.cap = cv2.VideoCapture(0)
        self.setup_ui_components()

        # 启动键盘和鼠标监听
        self.start_listeners()

        # 启动视频循环线程
        self.start_video_thread()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def setup_ui_components(self):
        self.video_frame = tk.Canvas(self.root, bg='black')
        self.video_frame.pack(fill='both', expand=True)

        self.lbl_key_data = tk.Label(self.root, text="Key Data: None", font=("Arial", 20), bg="black", fg="white")
        self.lbl_key_data.place(x=20, y=20)

        self.lbl_mouse_data = tk.Label(self.root, text="Mouse Data: None", font=("Arial", 20), bg="black", fg="white")
        self.lbl_mouse_data.place(x=20, y=60)

    def start_video_thread(self):
        threading.Thread(target=self.video_loop, daemon=True).start()

    def start_listeners(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def on_key_press(self, key):
        try:
            key_data = f"Key pressed: {key.char}"
        except AttributeError:
            key_data = f"Special key pressed: {key}"
        self.lbl_key_data.config(text=key_data)

    def on_mouse_move(self, x, y):
        mouse_data = f"Mouse moved to ({x}, {y})"
        self.lbl_mouse_data.config(text=mouse_data)

    def video_loop(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.video_frame.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.root.after(10, self.video_loop)

    def on_closing(self):
        self.is_running = False
        if self.cap.isOpened():
            self.cap.release()
        if self.keyboard_listener is not None:
            self.keyboard_listener.stop()
        if self.mouse_listener is not None:
            self.mouse_listener.stop()
        self.root.destroy()

app = MyGUI()
"""



# 12/22-12/23

# Project Module 5: Complete Project Engine

# - Data Visualization：matplotlib
#   - Build dashboard-like logic to report the output of the ...
#   - Use certain kinds of charts to show different kinds of analytics
#   - ...

# - PDF Report：PyPDF2, ReportLab
#   - Invoke Adobe PDF in order to get the reports sealed and transported
#   - Embed the results into a website so that the web-end at the user can be applied
#   - ...

# GUI:
# scale the window to fit your screen (e.g. mine is 2560*1600); can be 1920*1200
# relocate the statistics as a transparent box in top-left/top-right/bottom-left/bottom-right
# design where the buttons and dragger would be (this will be part of my tasks)

###### YOUR CODE HERE ######

import cv2
import mediapipe as mp
from pynput.keyboard import Controller
from pynput.mouse import Controller as MouseController

class EyeTracker:
    def __init__(self):
        self.keyboard = Controller()
        self.mouse = MouseController()
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh()

    def detect_eyes(self):
        cap = cv2.VideoCapture(0)  # 打开摄像头
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                continue

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(frame_rgb)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    # 在这里添加眼部检测的代码
                    # 可以使用face_landmarks中的关键点来检测眼睛的位置
                    # 根据检测结果来触发键盘和鼠标事件

            cv2.imshow('Eye Tracker', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def control_keyboard(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def control_mouse(self, x, y):
        self.mouse.position = (x, y)

# 在这里实例化EyeTracker类，并调用detect_eyes方法来开始眼部检测
if __name__ == "__main__":
    tracker = EyeTracker()
    tracker.detect_eyes()

# Project Module 6: The Tracker App

###### YOUR CODE HERE ######
