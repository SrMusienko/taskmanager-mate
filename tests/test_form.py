import io
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image

from task.forms import WorkerForm


class WorkerFormTest(TestCase):
    @staticmethod
    def create_test_image(size):
        image = Image.new("RGB", (100, 100))
        temp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        image.save(temp_file)
        temp_file.seek(0)
        return SimpleUploadedFile(
            temp_file.name,
            temp_file.read(),
            content_type="image/jpeg"
        )

    @staticmethod
    def create_image_file(size_in_mb, file_name="test_image.jpg"):
        image = Image.new("RGB", (1000, 1000), color="red")
        image_file = io.BytesIO()
        image.save(image_file, format="JPEG")
        image_file.seek(0)
        image_data = image_file.read()
        current_size = len(image_data)
        size_in_bytes = size_in_mb * 1024 * 1024
        if current_size < size_in_bytes:
            image_data += b"\0" * (size_in_bytes - current_size)
        return SimpleUploadedFile(
            file_name, image_data,
            content_type="image/jpeg"
        )

    def test_photo_file_size_validation(self):
        large_image = self.create_test_image(size=5 * 1024 * 1024 + 1)
        large_image = self.create_image_file(size_in_mb=6)
        form_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "position": None,
        }
        form_files = {
            "photo": large_image,
        }
        form = WorkerForm(data=form_data, files=form_files)

        self.assertFalse(form.is_valid())
        self.assertIn("photo", form.errors)
        self.assertEqual(
            form.errors["photo"][0],
            "The maximum file size allowed is 5 MB."
        )

    def test_photo_file_size_under_limit(self):
        small_image = self.create_test_image(size=5 * 1024 * 1024 - 1)
        form_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "position": None,
        }
        form_files = {
            "photo": small_image,
        }
        form = WorkerForm(data=form_data, files=form_files)

        self.assertTrue(form.is_valid())
