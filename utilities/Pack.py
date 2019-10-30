class Pack:
    def __init__(self, path,type_message, data):
        self.path = path
        self.type_message = type_message
        self.data = data

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def get_type_m(self):
        return self.type_message

    def get_data(self):
        return self.data