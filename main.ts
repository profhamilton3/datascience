datalogger.onLogFull(function () {
    datalogger.deleteLog(datalogger.DeleteType.Full)
})
input.onGesture(Gesture.Shake, function () {
    datalogger.log(
    datalogger.createCV("compass_heading", input.compassHeading()),
    datalogger.createCV("mgX", input.acceleration(Dimension.X)),
    datalogger.createCV("mgY", input.acceleration(Dimension.Y)),
    datalogger.createCV("mgZ", input.acceleration(Dimension.Z)),
    datalogger.createCV("strenth", input.acceleration(Dimension.Strength))
    )
})
datalogger.includeTimestamp(FlashLogTimeStampFormat.Seconds)
datalogger.mirrorToSerial(true)
input.setAccelerometerRange(AcceleratorRange.FourG)
