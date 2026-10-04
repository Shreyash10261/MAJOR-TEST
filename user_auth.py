class UserAuth:
    def __init__(self):
        self.users = {"admin": "password123"}
        
    def login(self, username, password):
        if username not in self.users:
            return False
        # Intentional bug: concatenating string and int if password is an int
        expected_hash = "hash_" + self.users.get(username, "")
        provided_hash = "hash_" + password
        return expected_hash == provided_hash
