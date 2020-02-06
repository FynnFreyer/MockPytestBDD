#!/usr/bin/env python3

import pytest
import random
import string

from mock import MockApp
from pathlib import Path


class TestClass:
    EXAMPLE_TEXT = "Lorem Ipsum nvaöonavöovaöoinöoivaöoinvöoni"

    def test_naming_convention_with_suffix(self):
        mock = MockApp(self.tmp_dir)

        file_in = self.tmp_dir / "text.txt"
        file_in.write_text(self.EXAMPLE_TEXT)

        file_out = self.tmp_dir / "text_out.txt"
        assert not file_out.exists()

        mock.process()
        assert file_out.exists()

    def test_naming_convention_without_suffix(self):
        mock = MockApp(self.tmp_dir)

        file_in = self.tmp_dir / "text"
        file_in.write_text(self.EXAMPLE_TEXT)

        file_out = self.tmp_dir / "text_out"
        assert not file_out.exists()

        mock.process()
        assert file_out.exists()

    def test_uppercase(self):
        mock = MockApp(self.tmp_dir)

        file_in = self.tmp_dir / "text"
        file_in.write_text(self.EXAMPLE_TEXT)

        file_out = self.tmp_dir / "text_out"

        mock.process()

        actual = file_out.read_text()
        expected = self.EXAMPLE_TEXT.upper()

        assert actual == expected

    def test_mock_app_raises_file_not_found_exception(self):
        with pytest.raises(FileNotFoundError):
            mock = MockApp("dieser Pfad existiert nicht")

    def test_multiple_files_produce_multiple_outputs(self):
        mock = MockApp(self.tmp_dir)

        file_one_in = self.tmp_dir / "text1"
        file_one_in.write_text(self.EXAMPLE_TEXT)

        file_two_in = self.tmp_dir / "text2"
        file_two_in.write_text(self.EXAMPLE_TEXT)

        file_one_out = self.tmp_dir / "text1_out"
        file_two_out = self.tmp_dir / "text2_out"

        mock.process()

        assert file_one_out.exists() and file_two_out.exists()

    # Verwaltung
    @classmethod
    def setup_class(cls):
        cls.tmp_dir = Path().cwd() / ("tmp" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
        cls.tmp_dir.mkdir()

    def teardown_method(self):
        self.remove_output()

    def remove_output(self):
        files = self.tmp_dir.iterdir()
        for path in files:
            path.unlink()

    @classmethod
    def teardown_class(cls):
        cls.tmp_dir.rmdir()


if __name__ == "__main__":
    TestClass.setup_class()
    test = TestClass()
    test.test_uppercase()
    test.remove_output()
    TestClass.teardown_class()
