from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, full_name, is_botanist, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')

        if not email:
            raise ValueError('Users must have an email address')
        
        if not full_name:
            raise ValueError('Users must have an full name')

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            full_name=full_name,
            is_botanist=is_botanist
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, full_name, is_botanist, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(phone_number, email, full_name, is_botanist, password)
        user.is_admin = True
        user.save(using=self._db)
        return user