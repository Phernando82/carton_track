import pytest
from django.urls.base import reverse

from carton_track_project.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse("base:home"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title>Rastreo de Pedidos</title>")


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Rastreo de Pedidos</a>')
