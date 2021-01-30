from django.urls import reverse

import pytest


@pytest.mark.django_db
def test_sewage_info_passing(client):
    uri = reverse('sewage-info')
    resp = client.get(uri)
    assert resp.status_code == 200
