import time
import u3

SCAN_FREQUENCY = 48000  # Hz


card = u3.U3()
card.configU3()
card.getCalibrationData()
card.configIO(FIOAnalog=3)  # NOTE: What does this do?

card.streamConfig(  # TODO: Look up what each of these parameters do
    NumChannels=3,
    PChannels=[0, 1, 2],
    NChannels=[31, 31, 31],
    Resolution=3,
    ScanFrequency=SCAN_FREQUENCY
)

try:
    card.streamStart()

    with open("AIO0.txt", 'w+') as input0, open("AIO1.txt", 'w+') as input1:
        for data_batch in card.streamData():
            if data_batch is not None:

                # Writing the input to two separate files
                input0.write(f"{data_batch['AIN0']}")
                input1.write(f"{data_batch['AIN1']}")

                #results = card.processStreamData(data_batch)

                #conversion = lambda x : 10000/(1023/x - 1)

                r_aio2 = sum(data_batch['AIN2'])/len(data_batch['AIN2'])
                
                #print(card.processStreamData(data_batch['AIN2']))
                print(f"ain2: {r_aio2}")
except KeyboardInterrupt as e:
    print("exiting...")
finally:
    card.streamStop()
    card.close()