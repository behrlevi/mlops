# Custom preprocessing

We are going to use `pyfunc` to ship a model with
surronding Python logic.
The wrapper (ScaledPredictor) we are buildig is
essentially a translator from raw data to the format
the model expects.
In our case, it substracts the average and divides
by the typical spread.

Examine `predict_with_preprocessing.py` in the scripts
directory.

Run `seed_prod.py` first to generate the model and 
`predict_with_preprocessing.py` to apply the wrapper.