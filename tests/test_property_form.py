import pytest
from septic_check.forms import PropertyForm


@pytest.mark.parametrize(
    'address, zipcode, validity',
    [('123 S. Main St', 92357, True),
     (33457, 12345678910, False),
     ('55 East Washington', None, False),
     ('', 18, False),
     (None, 18, False),
     ])
def test_example_form(address, zipcode, validity):
    form = PropertyForm(data={
        'address': address,
        'zipcode': zipcode,
    })

    assert form.is_valid() is validity
