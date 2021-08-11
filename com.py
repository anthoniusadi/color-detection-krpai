import serial

serial1 = serial.Serial('/dev/ttyUSB0', 9600)
def kirim(x,y):
    serial1.flush()
    x = str(x)
    # y= str(y)+"#"
    x_Encode = x.encode()
    # y_Encode = y.encode()

    x_Encode += b'\n'
    # y_Encode += b'\n'
    serial1.write(x_Encode)
    # serial1.write(y_Encode)
    
    print(x_Encode)
def get():
    line=serial1.readline()
    if line:
        msg = line.decode()
        num = int(msg)
        return num
    # serial1.close()
