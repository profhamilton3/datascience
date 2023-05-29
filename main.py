def on_log_full():
    datalogger.delete_log(datalogger.DeleteType.FULL)
datalogger.on_log_full(on_log_full)

def on_gesture_shake():
    datalogger.log(datalogger.create_cv("compass_heading", input.compass_heading()),
        datalogger.create_cv("mgX", input.acceleration(Dimension.X)),
        datalogger.create_cv("mgY", input.acceleration(Dimension.Y)),
        datalogger.create_cv("mgZ", input.acceleration(Dimension.Z)),
        datalogger.create_cv("strenth", input.acceleration(Dimension.STRENGTH)))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

datalogger.include_timestamp(FlashLogTimeStampFormat.SECONDS)
datalogger.mirror_to_serial(True)
input.set_accelerometer_range(AcceleratorRange.FOUR_G)