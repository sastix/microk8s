import subprocess

from .exceptions import UnknownServiceError, ServiceError


class ServiceUtils:
    """
    Service utilities.
    """

    @staticmethod
    def check_if_service_exists(service):
        """
        Check if the given service exists.

        Performs:
        $ snap info microk8s
        and checks the output for the given service

        :param service: the service name
        :return: True if the service exists
        """
        try:
            services = subprocess.check_output(['snap', 'info', 'microk8s'])
        except subprocess.CalledProcessError as err:
            raise ServiceError(err.output)

        found = False

        for line in str(services, 'utf-8').splitlines():
            if service + ':' in line:
                found = True

        if not found:
            raise UnknownServiceError(service)

    @staticmethod
    def get_service_status(service):
        """
        Returns the status of the given service if it exists.

        Example response:
        {
            "name": "service_name",
            "type": "simple",
            "mode": "enabled",
            "status": "active"
        }

        :return: Dictionary with the service data or error data
        """
        try:
            services = subprocess.check_output(['snap', 'info', 'microk8s'])
        except subprocess.CalledProcessError as err:
            raise ServiceError(err.output)

        for line in str(services, 'utf-8').splitlines():
            if service + ':' in line:
                line = line.replace(',', '')
                line = line.replace(':', '')
                linespl = line.split()
                return {'name': linespl[0], 'type': linespl[1], 'mode': linespl[2], 'status': linespl[3]}

        raise UnknownServiceError(service)
