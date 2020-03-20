class ErrorCode:
    """
    Error codes per error type.
    """
    UNKNOWN_SERVICE_ERROR = 100
    SERVICE_ERROR = 101
    INVALID_TOKEN_ERROR = 102


class UnknownServiceError(Exception):
    """
    Error to be thrown if the given service/plugin/addon does not exist.
    """

    def __init__(self, service_name):
        """
        Default constructor.

        :param service_name: The service name.
        """
        self.code = ErrorCode.UNKNOWN_SERVICE_ERROR
        self.message = "The service {} does not exist!".format(service_name)

    def get_error(self):
        """
        Error message builder.
        """
        return {
            "code": self.code,
            "message": self.message
        }


class ServiceError(Exception):
    """
    Error to be thrown in case of snap or systemctl service error.
    """

    def __init__(self, log):
        """
        Default constructor.

        :param log: The service log.
        """
        self.code = ErrorCode.SERVICE_ERROR
        self.message = log

    def get_error(self):
        """
        Error message builder.
        """
        return {
            "code": self.code,
            "message": self.message
        }


class InvalidTokenError(Exception):
    """
    Error to be raised in case of invalid token.
    """

    def __init__(self):
        """
        Default constructor.
        """
        self.code = ErrorCode.INVALID_TOKEN_ERROR
        self.message = "Invalid token"

    def get_error(self):
        """
        Error message builder.
        """
        return {
            "code": self.code,
            "message": self.message
        }
