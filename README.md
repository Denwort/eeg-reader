# EEG Reader

This project allows users to interact with the Epoc X data and store samples for future analysis.

## Credits
This project was adapted from the work of [vtr0n](https://github.com/vtr0n/emotiv-lsl).
You can find the original code on this repo: [emotiv-lsl](https://github.com/vtr0n/emotiv-lsl)

### How to install

```
pip install pipenv
python -m pipenv install
```

### How to run
Connect dongle, turn on the headset and 
```
# frist terminal
python -m pipenv run python main.py
```

Once you have established the connection, you can now view the data in real-time. To do so, simply open a new terminal and execute the following command:
```
# second terminal
python -m pipenv run python examples/read_data.py
```

However, if you want to take samples and store the data, you can run the following command instead:
```
# second terminal
python -m pipenv run python examples/read_and_export.py
```

After collecting your sample, update the filepath in read_fif.py to point to the new sample file you've just created. Then, to visualize the sample, run:
```
python -m pipenv run python .\examples\read_fif.py
```

### Config

To adjust the device sampling rate, change the SRATE value and update the setting in the emotiv app as well.

To change the duration of samples, you can change the duration value on read_and_export.py
