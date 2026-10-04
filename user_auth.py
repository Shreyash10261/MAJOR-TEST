class UserAuth:
    def __init__(self):
        self.users = {"admin": "password123"}
        
    def login(self, username, password):
        if username not in self.users:
            return False
        # Fixed bug: cast password to string
        expected_hash = "hash_" + self.users.get(username, "")
        provided_hash = "hash_" + str(password)
        return expected_hash == provided_hash
