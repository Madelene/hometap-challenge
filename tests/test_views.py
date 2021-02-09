import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_sewage_info_passing(client):
    uri = reverse('sewage_info')
    resp = client.get(uri)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_home(client):
    uri = reverse('home')
    resp = client.get(uri)
    assert resp.status_code == 200
