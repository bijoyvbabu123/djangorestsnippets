from django.contrib.auth.models import BaseUserManager


# model manager for custom user model with email as the user identifier
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        if not password:
            raise ValueError('Superusers must have a password')
        if not email:
            raise ValueError('Superusers must have an email address')
        if not username:
            raise ValueError('Superusers must have a username')

        user = self.create_user(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user