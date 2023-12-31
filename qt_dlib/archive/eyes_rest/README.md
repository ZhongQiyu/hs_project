# eyes_rest

**Please Do not share this curriculum with the student. This is only for you**

## Curriculum

### Module 1: AI Introduction

1. AI and Sklearn
    * Topics
        * The Introduction to AI
        * AI in Actions with Sklearn
    * References
        * Lecture Slides (
          pptx): [Link](https://drive.google.com/file/d/1QaDNCroT7mR968lUs_43RR8QSu08eNkE/view?usp=sharing)
        * Lecture Slides (
          keynote): [Link](https://docs.google.com/presentation/d/1QfNrK_L4GrO6FQyZTCdpSGkWpw2EHN3M/edit?usp=sharing&ouid=104361959057037146246&rtpof=true&sd=true)
        * Lecture sample: https://youtu.be/EjFanvsr-vk
        * Repl code sample: https://replit.com/@sunyu912/ForsakenTanConversions#main.py
    * Milestone and Goals
        * Student understands the major AI/Machine Learning concept (i.e., dataset, training, prediction)
        * Student understands the basic Sklearn Iris flower classification example code

2. Computer Vision to read a video/image

- OpenCV Get Started

    - Setup environment

    - Introduction to OpenCV

        - https://learnopencv.com/getting-started-with-opencv/
    - Process image:
        - Run the read, display and write an image example (with an image)

            - https://learnopencv.com/read-display-and-write-an-image-using-opencv/
        - Run the image resizing example (with an image)

            - https://learnopencv.com/image-resizing-with-opencv/
        - Run the putText example
            - https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
        - Run rectangle example
            - https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/
    - Process video
        - Run the read, display and write an video example (with a video)
            - From File
                - https://learnopencv.com/reading-and-writing-videos-using-opencv/

```
              import cv2 

              # Create a video capture object, in this case we are reading the video from a file
              vid_capture = cv2.VideoCapture('<file_path.mp4>') # For webcam change <file_path.mp4> to 0. Eg. vid_capture = cv2.VideoCapture(0)

              if (vid_capture.isOpened() == False):
                print("Error opening the video file")
              # Read fps and frame count
              else:
                # Get frame rate information
                # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
                fps = vid_capture.get(5)
                print('Frames per second : ', fps,'FPS')

                # Get frame count
                # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
                frame_count = vid_capture.get(7)
                print('Frame count : ', frame_count)

              while(vid_capture.isOpened()):
                # vid_capture.read() methods returns a tuple, first element is a bool 
                # and the second is frame
                ret, frame = vid_capture.read()
                if ret == True:
                  cv2.imshow('Frame',frame)
                  # 20 is in milliseconds, try to increase the value, say 50 and observe
                  key = cv2.waitKey(20)
                  
                  if key == ord('q'):
                    break
                else:
                  break

              # Release the video capture object
              vid_capture.release()
              cv2.destroyAllWindows()
```

## Module 2: Eyes Blink Engine

### Learn about Medipipe Face Mesh

MediaPipe is an open-source framework developed by Google that offers ready-to-use Machine Learning models for various
tasks, including face detection and facial landmark estimation. In this tutorial, we will focus on using the MediaPipe
Face Mesh model to detect facial landmarks in images and video streams.

#### Prerequisites

mediapipe Python library installed. You can install it using pip:

```commandline
pip install mediapipe
```

#### Getting Started

1. Import the required libraries:

   ```python
   import cv2
   import mediapipe as mp
   ```

2. Initialize the MediaPipe Face Mesh model:

   ```python
   mp_face_mesh = mp.solutions.face_mesh
   face_mesh = mp_face_mesh.FaceMesh()
   ```

3. Initialize the webcam or load an image:

   ```python
   # To use a webcam, you can initialize it like this:
   cap = cv2.VideoCapture(0)

   # To use an image, you can load it like this:
   # image = cv2.imread('your_image.jpg')
   ```

4. Create a loop to process frames (for live video):

   ```python
   while True:
       ret, frame = cap.read()
       if not ret:
           break

       # Convert the BGR image to RGB
       rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

       # Process the frame with MediaPipe Face Mesh
       results = face_mesh.process(rgb_frame)
   ```

5. Draw facial landmarks on the frame:

   ```python
       if results.multi_face_landmarks:
           for face_landmarks in results.multi_face_landmarks:
               for landmark in face_landmarks.landmark:
                   x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(landmark.z * frame.shape[1])
                   cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
   ```

6. Display the processed frame:

   ```python
       cv2.imshow('Face Mesh', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
   ```

7. Release the video capture and close the OpenCV window when finished:

   ```python
   cap.release()
   cv2.destroyAllWindows()
   ```

- To run the code with a webcam, make sure you have a webcam connected to your computer. Execute the script, and it will
  open a window displaying the webcam feed with facial landmarks drawn.

- To run the code with an image, uncomment the image loading section and provide the path to your image. Execute the
  script, and it will display the image with facial landmarks drawn.

#### Show left eyes

Let's inspect the image that show the canonical face model uv visualization

![canonical_face_model_uv_visualization.png](canonical_face_model_uv_visualization.png)

If we zoom in the image we can get the key-points for the left eyes
![img.png](left_eye.png)

To show only the left eye using the MediaPipe Face Mesh model, you can modify the code by selecting and drawing only the
left eye landmarks. Here's how you can do it:

```python
import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Define the indices for the left eye landmarks
            left_eye_landmark_indices = [33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145, 144, 163, 7]

            for idx in left_eye_landmark_indices:
                landmark = face_landmarks.landmark[idx]
                x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(
                    landmark.z * frame.shape[1])
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow('Left Eye', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```

In this modified code, we define the left_eye_landmark_indices list to specify the indices of the landmarks
corresponding to the left eye. We then iterate through these indices and draw circles at the corresponding positions on
the frame. This will show only the landmarks of the left eye, effectively isolating it from the rest of the face
landmarks.

### Eyes blink detector

- process_image
    - fetch_face_data
    - landmarksDetection
    - update_blink_data
    - Calculate blink ratio
        - euclidean_distance
        - blinkRatio
    - draw_eyes
    - check_blink_rate
    - show_activity_timer
    - calculate_frame_per_sec(frame, frame_counter, self.start_time)
    - reset_values
- Test using video input

## Module 3: Mouse and Keyboard tracker

### Learn abut pynput

- Monitoring the mouse

A mouse listener is a threading.Thread, and all callbacks will be invoked from the thread.

Call pynput.mouse.Listener.stop from anywhere, raise StopException or return False from a callback to stop the listener.

When using the non-blocking version above, the current thread will continue executing. This might be necessary when
integrating with other GUI frameworks that incorporate a main-loop, but when run from a script, this will cause the
program to terminate immediately.

  ```
    from pynput import mouse

    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    # Collect events until released
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    #listener = mouse.Listener(
     #   on_move=on_move,
      #  on_click=on_click,
       # on_scroll=on_scroll)
   # listener.start()
  ```

- Monitoring the keyboard

A keyboard listener is a threading.Thread, and all callbacks will be invoked from the thread.

Call pynput.keyboard.Listener.stop from anywhere, raise StopException or return False from a callback to stop the
listener.

The key parameter passed to callbacks is a pynput.keyboard.Key, for special keys, a pynput.keyboard.KeyCode for normal
alphanumeric keys, or just None for unknown keys.

When using the non-blocking version above, the current thread will continue executing. This might be necessary when
integrating with other GUI frameworks that incorporate a main-loop, but when run from a script, this will cause the
program to terminate immediately.

  ```
   from pynput import keyboard

    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
  ```

### Keyboard and Mouse Tracker

- Define a callback function for mouse events
- Define a callback function for keyword events
- Track user activity
- Run_tracker
- Test Tracker

## Module 4 - Activity and Inactivity Engine

### Build Activity and Inactivity Engine

- Simulate data
    - simulate_blink_rate(num_intervals):
    - simulate_usage_time(session_duration_minutes, max_interval_duration_minutes):
    - simulate_inactivity(usage_data):
    - simulate_activity_labels(inactivity_data, activity_data, threshold_ratio, activity_threshold):
- train_model
- Do prediction

## Module 5 - Build Eyes tracker

- process image in a thread
- Use the AI to predict if a person need to take a break (break_prediction)
- run_engine

## Module 6 - APP desktop

- Follow this curriculum to learn about Tkinter https://quest.codingmind.com/view/713865CE2E1144318BD128843A
- Build the EyeTrackerAPP

## References:

- https://github.com/google/mediapipe/wiki/MediaPipe-Face-Mesh
