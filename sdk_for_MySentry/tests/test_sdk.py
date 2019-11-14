import pytest

from sdk_for_MySentry_pgk.sdk import ErrorLogSender


class SdkTest:

    def test_error_log_sender_init(self):
        app_id = 2
        token = 'qwe'
        error_log_sender_object = ErrorLogSender(app_id, token)
        assert isinstance(error_log_sender_object, ErrorLogSender)

    def test_error_log_sender_init_invalid_id(self):
        app_id = '1'
        token = 'qwe'
        with pytest.raises(AssertionError):
            error_log_sender_object = ErrorLogSender(app_id, token)

    def test_error_log_sender_init_invalid_token(self):
        app_id = 1
        token = 123
        with pytest.raises(AssertionError):
            error_log_sender_object = ErrorLogSender(app_id, token)


def start_test():
    sdk_test = SdkTest()
    sdk_test.test_error_log_sender_init()
    sdk_test.test_error_log_sender_init_invalid_id()
    sdk_test.test_error_log_sender_init_invalid_token()


if __name__ == '__main__':
    start_test()