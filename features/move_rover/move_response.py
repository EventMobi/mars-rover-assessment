class MoveResponse:
    def build_success_response(self, data: dict):
        for k, v in data.items():
            response = "{}:{}".format(k, " ".join(v))
            print(response)

    def build_failed_response(self, message: str):
        raise ValueError(message)
