# Object recognition - TensorFlow.


## How to run the project.
1. Go to the folder project.

$ cd python-object-recognition

2. Activate the python environment.

$ source bin/activate

3. Run the project.

$ python3 gui.py


## Shortcuts:
1. CTRL + O: open file (only on video).
2. space: start/stop (video and real time).
3. CTRL + R: start/stop recognition (video and real time).

(MacOS users need to use command key instead the CTRL).


## outputs
1. the outputs will always be printed to the console.
2. for MacOS users the screen reader voice Over will speak all recognized objects.


# To do:
1. Add new objects (images) to the neural network.
2. Train the neural network.
3. Add ESpeak screen reader to the project (available voice responses to Linux, MacOS and Windows users).


# Configure environment (only for developers):
1. Create a virtual environment.
2. Activate the virtual environment.
3. Install WXPython.

pip3 install wxpython

4. Install numpy.

pip install numpy

5. Install OpenCV 3.

pip install opencv-python

6. Install Tensor flow:

pip3 install --upgrade tensorflow

7. Run.

python3 gui.py
