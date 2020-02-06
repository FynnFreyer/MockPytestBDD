#!/usr/bin/env python3


import pytest
import random
import string

from pytest_bdd import scenarios, given, when, then, parsers
from mock import MockApp
from pathlib import Path

# Constants
EXAMPLE_TEXT = "Lorem Ipsum nvaöonavöovaöoinöoivaöoinvöoni"


# Fixtures
@pytest.fixture(scope="module")
def tmp_dir():
    d = Path().cwd() / ("tmp" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
    d.mkdir()

    yield d

    files = d.iterdir()
    for path in files:
        path.unlink()
    d.rmdir()
    # oder shutil.rmtree(d) ?


# Scenarios
scenarios('features/output.feature')


# Given steps
@given(parsers.parse('the file "{file_name}" with content "{content}" exists'))
def a_file_exists(tmp_dir, file_name, content):
    file_in = tmp_dir / file_name
    file_in.write_text(content)


# When steps
@when(parsers.parse('I pass "{file_name}" as an argument to the app'))
def call_app(tmp_dir, file_name):
    mock = MockApp(tmp_dir / file_name)
    mock.process()


# Then steps
@then(parsers.parse('the file "{file_name}" should exist'))
def file_exists(tmp_dir, file_name):
    assert Path(tmp_dir / file_name).exists()


@then(parsers.parse('the content of "{file_name}" should be "{expected}"'))
def content_is_correct(tmp_dir, file_name, expected):
    actual = Path(tmp_dir / file_name).read_text()
    assert actual == expected


