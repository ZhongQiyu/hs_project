import time
import threading
import cv2
#import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
from tkinter import ttk



class EyeTrackingApp:
    def __init__(self, window_title):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title(window_title)
        self.root.configure(bg='#404040')

        self.on_break = False

        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        # Create a style object
        style = ttk.Style()
        style.theme_use('clam')  # Use the 'clam' theme as a base for customization

        # Configure style for Button
        style.configure('Custom.TButton', 
                        background='#404040', 
                        foreground='white', 
                        bordercolor='white', 
                        borderwidth=2,
                        font=('Segoe UI', 14))

        # Configure style for Text
        text_bg = '#404040'  # Dark grey background for text
        text_fg = 'white'    # White text color

        # Main Frame
        main_frame = tk.Frame(self.root, bg='#404040')
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Video Frame
        video_frame = tk.Frame(main_frame, bg='#404040')
        video_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Right Section Frame
        right_frame = tk.Frame(main_frame, bg='#404040')
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_video = tk.Canvas(video_frame, bg='#404040')
        self.canvas_video.pack(fill="both", expand=True)

        # Time Elapsed Frame
        self.total_time_count = 0
        time_frame = tk.Frame(right_frame, bg='#404040')
        time_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.total_time_elapsed = tk.Label(time_frame, text="Total Time Elapsed: 0", font=("Segoe UI", 20), fg='white', bg='#404040')
        self.total_time_elapsed.pack()
        self.change_total_time_count()

        # Strictness Frame
        self.strictness = 10
        strictness_frame = tk.Frame(right_frame, bg='#404040')
        strictness_frame.pack(side=tk.TOP, fill=tk.X)
        strictness_frame.columnconfigure(0, weight=1)
        strictness_frame.columnconfigure(1, weight=1)
        self.strictness_value = tk.Label(strictness_frame, font=("Segoe UI", 20), text='Blink Strictness: ' + str(self.strictness), fg='white', bg='#404040')
        self.strictness_value.grid(row=0, columnspan=2)
        self.strictness_textbox = tk.Text(strictness_frame, font=("Segoe UI", 20), height=1, width=5, bg=text_bg, fg=text_fg)
        self.strictness_textbox.grid(row=1, column=0, pady=(0, 5), padx=5, sticky="ew")
        self.set_strictness_button = ttk.Button(strictness_frame, text="Set Strictness", style='Custom.TButton', command=self.set_strictness)
        self.set_strictness_button.grid(row=1, column=1, pady=(0, 5), padx=5, sticky="ew")
        self.strictness_explanation = tk.Label(strictness_frame, text="Blink Strictness means the maximum blink count per minute", font=("Arial", 15), fg='white', bg='#404040')
        self.strictness_explanation.grid(row=3, columnspan=2)
        self.warning_msg = tk.Label(strictness_frame, text="", font=("Arial", 15), fg='red', bg='#404040')
        self.warning_msg.grid(row=2, columnspan=2)

        # Blink Count Frame
        self.blink_count = 0
        self.EAR_THRESHOLD = 0.21
        self.eye_closed = False
        self.blink_count_frame = tk.Frame(right_frame, bg='#404040')
        self.blink_count_frame.pack(side=tk.TOP, fill=tk.X)
        self.total_blink_count = tk.Label(self.blink_count_frame, text="Total Blink Count: 0", font=("Segoe UI", 20), fg='white', bg='#404040')
        self.total_blink_count.pack()

        # Break Label
        self.break_label = tk.Label(right_frame, text="Time for a break!", font=("Segoe UI", 20), fg='red', bg='#404040')
        self.break_label.pack(pady=10)
        self.break_label.pack_forget()

        # Spacer Frame
        spacer_frame = tk.Frame(right_frame, height=20, bg='#404040')
        spacer_frame.pack(side=tk.TOP, fill=tk.X)

        # Clicks and Keystrokes Frame
        self.total_click_amount = 0
        self.total_keystroke_count = 0
        clicks_frame = tk.Frame(right_frame, bg='#404040')
        clicks_frame.pack(side=tk.TOP, fill=tk.X)
        self.total_clicks = tk.Label(clicks_frame, text="Total Clicks: 0", font=("Segoe UI", 20), fg='white', bg='#404040')
        self.total_clicks.pack()
        keystrokes_frame = tk.Frame(right_frame, bg='#404040')
        keystrokes_frame.pack(side=tk.TOP, fill=tk.X)
        self.total_keystrokes_label = tk.Label(keystrokes_frame, text="Total Keystroke Count: 0", font=("Segoe UI", 20), fg='white', bg='#404040')
        self.total_keystrokes_label.pack()

        # Total Inputs Frame
        total_inputs_frame = tk.Frame(right_frame, bg='#404040')
        total_inputs_frame.pack(side=tk.TOP, fill=tk.X)
        self.total_inputs_label = tk.Label(total_inputs_frame, text="Total Inputs: 0", font=("Segoe UI", 20), fg='white', bg='#404040')
        self.total_inputs_label.pack()

        # Input Strictness Frame
        self.input_strictness = 50
        input_strictness_frame = tk.Frame(right_frame, bg='#404040')
        input_strictness_frame.pack(side=tk.TOP, fill=tk.X)
        input_strictness_frame.columnconfigure(0, weight=1)
        input_strictness_frame.columnconfigure(1, weight=1)
        self.input_strictness_value = tk.Label(input_strictness_frame, font=("Segoe UI", 20), text='Input Strictness: ' + str(self.input_strictness), fg='white', bg='#404040')
        self.input_strictness_value.grid(row=0, columnspan=2)
        self.input_strictness_textbox = tk.Text(input_strictness_frame, font=("Segoe UI", 20), height=1, width=5, bg=text_bg, fg=text_fg)
        self.input_strictness_textbox.grid(row=1, column=0, pady=(0, 5), padx=5, sticky="ew")
        self.set_input_strictness_button = ttk.Button(input_strictness_frame, text="Set Input Strictness", style='Custom.TButton', command=self.set_input_strictness)
        self.set_input_strictness_button.grid(row=1, column=1, pady=(0, 5), padx=5, sticky="ew")
        self.input_strictness_warning_msg = tk.Label(input_strictness_frame, text="", font=("Arial", 15), fg='red', bg='#404040')
        self.input_strictness_warning_msg.grid(row=2, columnspan=2)

        # Reset Countdown Label
        self.reset_countdown_label = tk.Label(right_frame, text="Resets in 60 seconds", font=("Segoe UI", 20), fg='white', bg='#404040')
        self.reset_countdown_label.pack(side=tk.TOP, fill=tk.X)

        # Input Listener Thread
        input_listener_thread = threading.Thread(target=self.run_input_listeners)
        input_listener_thread.daemon = True
        input_listener_thread.start()

        self.is_tracking = False
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        self.delay = 15

        # Start video updates
        self.root.after(100, self.start_updates)
        self.handle_reset_countdown()
        self.root.mainloop()
    def set_input_strictness(self):
        value = self.input_strictness_textbox.get("1.0", "end").strip()
        try:
            intvalue = int(value)
            if 0 <= intvalue <= 500:
                self.input_strictness = intvalue
                self.input_strictness_value.config(text="Input Strictness: " + str(intvalue))
                self.input_strictness_warning_msg.config(text="")
            else:
                self.input_strictness_warning_msg.config(text="Invalid Input! Please enter a number between 0 and 500!")
        except ValueError:
            self.input_strictness_warning_msg.config(text="Invalid Input! Please enter an integer!")

    def reset_counters(self):
        # Reset all the counters and update their respective labels
        self.blink_count = 0
        self.total_blink_count.config(text="Total Blink Count: 0")
        self.total_click_amount = 0
        self.total_keystroke_count = 0
        self.update_click_count()
        self.update_keystroke_count()
        self.update_total_inputs_label()

    def change_total_time_count(self):
        self.total_time_elapsed.config(text=f"Total Time Elapsed: {self.total_time_count}")
        self.total_time_count += 1
        self.root.after(1000, self.change_total_time_count)

    def update_total_inputs_label(self):
        total_inputs = self.total_click_amount + self.total_keystroke_count
        self.total_inputs_label.config(text=f"Total Inputs: {total_inputs}")
        if total_inputs >= self.input_strictness and not self.on_break:
            self.initiate_break()


    def show_break_label(self):
        self.break_label.pack()

    def hide_break_label(self):
        self.break_label.pack_forget()

    def run_input_listeners(self):
        # Initialize the mouse listener
        mouse_listener = MouseListener(on_click=self.on_click)
        mouse_listener.start()

        # Initialize the keyboard listener
        keyboard_listener = KeyboardListener(on_press=self.on_press)
        keyboard_listener.start()


    def start_eye_tracking(self):
        # Directly start tracking without checking the button state
        self.is_tracking = True
        self.canvas_video.configure(bg='black')

    def handle_reset_countdown(self, countdown=60):
        if hasattr(self, 'after_id'):  # Check if there's an existing after call
            self.root.after_cancel(self.after_id)  # Cancel the previous after call

        if self.on_break:
            if countdown > 0:
                self.reset_countdown_label.config(text=f"Break time! {countdown} seconds remaining")
                self.after_id = self.root.after(1000, self.handle_reset_countdown, countdown - 1)
            else:
                self.on_break = False
                self.reset_countdown_label.config(text="Resets in 60 seconds")
                self.hide_break_label()
                self.reset_counters()  # Call the method to reset the counters
                self.handle_reset_countdown()  # Restart the countdown
        else:
            if countdown > 0:
                self.reset_countdown_label.config(text=f"Resets in {countdown} seconds")
                self.after_id = self.root.after(1000, self.handle_reset_countdown, countdown - 1)
            else:
                self.reset_counters()  # Call the method to reset the counters
                self.handle_reset_countdown()  # Restart the countdown


    

    def clear_video_feed(self):
        self.canvas_video.delete("all")
        self.canvas_video.configure(bg='white')
        self.canvas_video.create_text(
            self.canvas_video.winfo_width() // 2, self.canvas_video.winfo_height() // 2,
            text="Video feed stopped", font=("Arial", 20), fill="black"
        )

    def start_updates(self):
        if not self.is_tracking:
            self.start_eye_tracking()
        self.update()

    def update(self):
        ret, frame = self.vid.read()
        if ret and self.is_tracking:
            frame = cv2.flip(frame, 1)
            canvas_width = self.canvas_video.winfo_width()
            canvas_height = self.canvas_video.winfo_height()

            if canvas_width > 0 and canvas_height > 0:
                frame = self.resize_with_aspect_ratio(frame, width=canvas_width, height=canvas_height)
                if frame is not None:
                    frame = self.detect_eyes(frame)
                    self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                    self.canvas_video.create_image((canvas_width - self.photo.width()) // 2, (canvas_height - self.photo.height()) // 2, image=self.photo, anchor=tk.NW)
        self.root.after(self.delay, self.update)


    def resize_with_aspect_ratio(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        (h, w) = image.shape[:2]

        # Calculate the aspect ratio of the image and the desired aspect ratio
        image_aspect = w / h
        desired_aspect = width / height if width is not None and height is not None else image_aspect

        # Calculate scaling factors for resizing the image while maintaining aspect ratio
        if image_aspect > desired_aspect:
            # Image is wider than the desired aspect ratio
            r = width / float(w)
            dim = (width, int(h * r))
        else:
            # Image is taller or equal to the desired aspect ratio
            r = height / float(h)
            dim = (int(w * r), height)

        # Check that dimensions are valid before attempting to resize
        if dim[0] > 0 and dim[1] > 0:
            resized = cv2.resize(image, dim, interpolation=inter)
            return resized
        return None


    def detect_eyes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = self.eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

        # Blink detection logic
        if len(eyes) == 0 and not self.eye_closed:  # Eyes not detected (blink)
            self.eye_closed = True
        elif len(eyes) > 0 and self.eye_closed:  # Eyes detected again (end of blink)
            self.eye_closed = False
            self.blink_count += 1
            self.update_blink_count()

        # Draw ellipses around the eyes for visualization
        for (x, y, w, h) in eyes:
            center = (x + w // 2, y + h // 2)
            axes = (max(5, w // 4), max(5, h // 6))  # Adjust the axes lengths to fit the eye shape better
            cv2.ellipse(frame, center, axes, 0, 0, 360, (255, 0, 0), 2)

        return frame

    def set_strictness(self):
        value = self.strictness_textbox.get("1.0", "end").strip()
        try:
            intvalue = int(value)
            if 0 <= intvalue <= 75:
                self.strictness = intvalue
                self.strictness_value.config(text=" Blink Strictness: " + str(intvalue))
                self.warning_msg.config(text="")
            else:
                self.warning_msg.config(text="Invalid Input! Please enter a number between 0 and 75!")
        except ValueError:
            self.warning_msg.config(text="Invalid Input! Please enter an integer!")

   
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.total_click_amount += 1
            self.update_click_count()
            self.update_total_inputs_label()

    def on_press(self, key):
        self.total_keystroke_count += 1
        self.update_keystroke_count()
        self.update_total_inputs_label()


    def update_click_count(self):
        self.total_clicks.config(text="Total Clicks: " + str(self.total_click_amount))
        self.update_total_inputs_label()

    def update_keystroke_count(self):
        self.total_keystrokes_label.config(text="Total Keystroke Count: " + str(self.total_keystroke_count))
    def run_mouse_listener(self):
        with MouseListener(on_click=self.on_click) as listener:
            listener.join()

    # Separate method to run the keyboard listener
    def run_keyboard_listener(self):
        with KeyboardListener(on_press=self.on_press) as listener:
            listener.join()

    """
        Eye blink engine time!
    """

    def update_blink_count(self):
        if not self.on_break:  # Only update blink count if not on a break
            self.total_blink_count.config(text=f"Total Blink Count: {self.blink_count}")

            if self.blink_count >= self.strictness:
                self.initiate_break()

    def initiate_break(self):
        # Set the state to break and update the UI accordingly
        self.on_break = True
        self.show_break_label()
        self.reset_countdown_label.config(text="Timer stopped, take a break!")
        self.handle_reset_countdown(30)  # Start a 30-second break countdown

        # Reset all counts
        self.reset_counters()
    

app = EyeTrackingApp("MediaPipe Eye Tracking with Tkinter")


"""
H.W:
-Automatic adjustment of the strictness of blink detection based on distace of user from computer camera
"""