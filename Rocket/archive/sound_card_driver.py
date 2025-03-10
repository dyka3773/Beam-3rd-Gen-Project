"""
Note: Our Python interfaces throw exceptions when there are any issues with
device communications that need addressed. Many of our examples will
terminate immediately when an exception is thrown. The onus is on the API
user to address the cause of any exceptions thrown, and add exception
handling when appropriate. We create our own exception classes that are
derived from the built-in Python Exception class and can be caught as such.
For more information, see the implementation in our source code and the
Python standard documentation.
"""
import traceback
from datetime import datetime

import u3


# MAX_REQUESTS is the number of packets to be read.
MAX_REQUESTS = 75  # We don't use that
# SCAN_FREQUENCY is the scan frequency of stream mode in Hz
SCAN_FREQUENCY = 48000  # TODO

d = None

###############################################################################
# U3
# Uncomment these lines to stream from a U3
###############################################################################
# At high frequencies ( >5 kHz), the number of samples will be MAX_REQUESTS
# times 48 (packets per request) times 25 (samples per packet).
d = u3.U3()

# To learn the if the U3 is an HV
d.configU3()

# For applying the proper calibration to readings.
d.getCalibrationData()

# Set the FIO0 and FIO1 to Analog (d3 = b00000011)
d.configIO(FIOAnalog=3)

print("Configuring U3 stream")
d.streamConfig(
    NumChannels=2,
    PChannels=[0, 1],
    NChannels=[31, 31],
    Resolution=3,
    ScanFrequency=SCAN_FREQUENCY
)

missed = 0
dataCount = 0
packetCount = 0
start = datetime.now()

try:
    print("Start stream")
    d.streamStart()
    start = datetime.now()
    print("Start time is %s" % start)

    with open("AIO0.txt", 'w+') as input0, open("AIO1.txt", 'w+') as input1:
        for r in d.streamData():
            if r is not None:
                # Our stop condition
                # if dataCount >= MAX_REQUESTS: # FIXME: Setted this up to never stop
                #     break

                if r["errors"] != 0:
                    print("Errors counted: %s ; %s" %
                          (r["errors"], datetime.now()))

                if r["numPackets"] != d.packetsPerRequest:
                    print("----- UNDERFLOW : %s ; %s" %
                          (r["numPackets"], datetime.now()))

                if r["missed"] != 0:
                    missed += r['missed']
                    print("+++ Missed %s" % r["missed"])

                # Comment out these prints and do something with r
                # print("Average of %s AIN0, %s AIN1 readings: %s, %s" %
                #      (len(r["AIN0"]), len(r["AIN1"]), sum(r["AIN0"])/len(r["AIN0"]), sum(r["AIN1"])/len(r["AIN1"])))

                input0.write(f"{r['AIN0']}")
                input1.write(f"{r['AIN1']}")

                dataCount += 1
                packetCount += r['numPackets']
            else:
                # Got no data back from our read.
                # This only happens if your stream isn't faster than the USB read
                # timeout, ~1 sec.
                print("No data ; %s" % datetime.now())
except:
    print("".join(i for i in traceback.format_exc()))
finally:
    stop = datetime.now()
    d.streamStop()
    print("Stream stopped.\n")
    d.close()

    sampleTotal = packetCount * d.streamSamplesPerPacket

    scanTotal = sampleTotal / 2  # sampleTotal / NumChannels
    print("%s requests with %s packets per request with %s samples per packet = %s samples total." %
          (dataCount, (float(packetCount)/dataCount), d.streamSamplesPerPacket, sampleTotal))
    print("%s samples were lost due to errors." % missed)
    sampleTotal -= missed
    print("Adjusted number of samples = %s" % sampleTotal)

    runTime = (stop-start).seconds + float((stop-start).microseconds)/1000000
    print("The experiment took %s seconds." % runTime)
    print("Actual Scan Rate = %s Hz" % SCAN_FREQUENCY)
    print("Timed Scan Rate = %s scans / %s seconds = %s Hz" %
          (scanTotal, runTime, float(scanTotal)/runTime))
    print("Timed Sample Rate = %s samples / %s seconds = %s Hz" %
          (sampleTotal, runTime, float(sampleTotal)/runTime))
