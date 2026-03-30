class PasswordChecker:
    def __init__(self):
        self.common_passwords = ["admin", "password", "123456", "root", "guest"]
        self.history = []

    def check_common(self, password):
        return password.lower() in self.common_passwords

    def check_strength(self, password):
        # Boolean logic for the three criteria
        return {
            "length": len(password) >= 8,
            "digit": any(c.isdigit() for c in password),
            "special": any(c in "!@#$%^&*" for c in password)
        }

    def evaluate(self, password):
        if self.check_common(password):
            result = "WEAK (common password)"
        else:
            # sum() treats True as 1 and False as 0—super handy!
            checks = self.check_strength(password)
            score = sum(checks.values())
            
            if score <= 1:
                result = "WEAK"
            elif score == 2:
                result = "MEDIUM"
            else:
                result = "STRONG"
        
        self.history.append((password, result))
        return result
