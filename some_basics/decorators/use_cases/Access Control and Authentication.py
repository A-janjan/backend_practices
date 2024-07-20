def require_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("User is not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, authenticated):
        self.is_authenticated = authenticated

@require_authentication
def view_profile(user):
    print("Profile page")

user = User(authenticated=True)
view_profile(user)
