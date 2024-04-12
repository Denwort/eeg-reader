import mne
import matplotlib.pyplot as plt

filepath = './samples/data_1710855964486137_raw.fif'

raw = mne.io.read_raw_fif(filepath, preload=True)

print(raw.info)

for idx in range(len(raw)):
    data, times = raw[:, idx]

    # Process the data as needed
    print(f"Sample {idx}:")
    print("Data:", data)
    print("Time:", times)

raw.plot()
plt.show(block=True)