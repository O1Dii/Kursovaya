from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    # python manage.py createsuperuser
    def create_superuser(self, email, is_staff, password, Organization, first_name,last_name, status):
        user = self.model(
            email=email,
            is_staff=is_staff,
            Organization=Organization,
            first_name=first_name,
            last_name=last_name,
            status=status,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    sys_id = models.AutoField(primary_key=True, blank=True)
    '''Системный id'''
    email = models.EmailField(max_length=127, unique=True, null=False, blank=False)
    '''e-mail пользователя'''
    first_name = models.CharField(max_length=30, default=" ")
    '''Имя'''
    last_name = models.CharField(max_length=150, default=" ")
    '''Фамилия'''
    Organization = models.CharField(max_length=150, default=" ")
    '''Организация'''
    is_staff = models.BooleanField()
    '''Флаг, дающий права администратора'''
    is_active = models.BooleanField(default=True)
    '''Флаг, показывающий, активен ли аккаунт пользователя'''
    status = models.BooleanField(default=False)
    '''Флаг, разделяющий руководителей и экспертов'''
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS must contain all required fields on your User model,
    # but should not contain the USERNAME_FIELD or password as these fields will always be prompted for.
    REQUIRED_FIELDS = ['is_staff', 'Organization', 'first_name', 'last_name', 'status']

    class Meta:
        app_label = "loginsys"
        db_table = 'users'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
