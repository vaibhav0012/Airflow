class APIKeys:
    def __init__(self, filepath):
        self.filepath = filepath
        self.keys = self.read_keys_from_file()

    def read_keys_from_file(self):
        keys = {}
        with open(self.filepath, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                keys[key.replace(" ", "_")] = value
        return keys

    def get_keys(self):
        return self.keys