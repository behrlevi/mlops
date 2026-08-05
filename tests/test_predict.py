# reach into src/ and pull the predict() function
from fraud_detection import predict


# assert = expect the statement to be strictly true
# otherwise throw an error
def test_flags_high_amount():
    assert predict([[150.0]]) == [1]


def test_passes_low_amount():
    assert predict([[50.0]]) == [0]
