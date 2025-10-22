import time
import roboflex as rcc
import roboflex.webcam_gst as rcw

print("Available devices:")
print(rcw.get_device_list_string())

WIDTH = 640
HEIGHT = 480
FPS = 30

sensor = rcw.WebcamSensor(
    width=WIDTH,
    height=HEIGHT,
    fps=FPS,
    device_index=-1,
    format="",
    emit_rgb=True,
)
sensor.print_device_info()

sensor > rcc.MessagePrinter("Received")

sensor.start()
time.sleep(5)
sensor.stop()
