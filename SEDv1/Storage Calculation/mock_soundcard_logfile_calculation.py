import pandas as pd

FREQUENCY_OF_THE_SOUNDCARD = 200
SECONDS_FUNCTIONING = 100

list = []

for i in range(FREQUENCY_OF_THE_SOUNDCARD * SECONDS_FUNCTIONING):
    list.append([0b0000000000000000])

df = pd.DataFrame(list, columns=['Volts'])
df.to_csv(f"Mock_SoundCard_{FREQUENCY_OF_THE_SOUNDCARD}Hz_{SECONDS_FUNCTIONING}s.csv")