import os


class TestBaseAPI:
    def setup_class(self):
        pass

    def teardown_class(self):
        os.system('for /d /r . %d in (.pytest_cache) do @if exist "%d" rd /s/q "%d"')
