
from django.conf import settings
from django.urls import is_valid_path

import pytest


@pytest.mark.urls("septic_check.urls")
def test_urls():
    assert settings.ROOT_URLCONF == "septic_check.urls"
    assert is_valid_path("/sewage_info/")
