# PulseVision
 A Python project analyzing stock market sector behavior using yfinance, pandas, numpy, and visualization tools.PulseVision is a Python-based application designed to estimate a person's heart rate by analyzing video footage of their face. The core of this project lies in detecting subtle color changes in the skin, which are caused by blood circulation. By processing these signals, we can extract the underlying heart pulse and calculate the beats per minute (BPM).This non-contact method provides a safe and convenient alternative to traditional heart rate monitoring devices.
#Features
Real-time Face Detection: Automatically detects and tracks faces in a video stream.
Region of Interest (ROI) Extraction: Isolates key facial areas (e.g., forehead, cheeks) for signal extraction.
rPPG Signal Processing: Extracts the raw blood volume pulse (BVP) signal from pixel intensity changes.
Signal Filtering: Applies digital filters (e.g., Butterworth bandpass) to remove noise and artifacts.
Heart Rate Calculation: Uses Fast Fourier Transform (FFT) to determine the dominant frequency in the signal, which corresponds to the heart rate.
Visual Feedback: Displays the live video feed, detected face, and calculated heart rate on the screen.

#Technologies Used 
This project is built using the following technologies and libraries:
Python 3.9+
OpenCV: For video capture, face detection, and image processing.
NumPy: For efficient numerical operations and array manipulation.
SciPy: For scientific and technical computing, especially for signal filtering and FFT.
Matplotlib (Optional): For plotting signals and results for analysis.
