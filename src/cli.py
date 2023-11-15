from service import Service


class CliInterface:
    def __init__(self, service: Service):
        self.service = service

    def run(self):
        pass
