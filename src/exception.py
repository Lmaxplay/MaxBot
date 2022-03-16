class AuthenticationException(Exception):
    def __str__(self):
        return "User is not Authenticated"