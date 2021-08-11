# Requriements
* OpenCV 4  (originally using 4.1.2.30)
* Numpy > 1.15 (originally using 1.19.2)

# Configure Arduino Input 
===
go to com.py setting serial1 = serial.Serial('/dev/ttyUSB0', 9600)
set up '/dev/ttyUSB0' according input Arduino

# Run program
===
python3 main.py

# Parameters
===
set luas for thresholding
set min_HSV & max_hsv according color you want 

# Close manualy
===
press ESC or wait luas>130000