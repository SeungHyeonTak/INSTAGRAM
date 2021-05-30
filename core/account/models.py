from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            # raise : 단일 인자의 예외를 발생
            raise ValueError(_('User must have and phone and email address'))

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )

        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name=_('이메일'), max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField(verbose_name=_('휴대폰 번호'), max_length=20, unique=True, blank=True, null=True)
    username = models.CharField(verbose_name=_('계정 이름'), max_length=30, unique=True)
    fullname = models.CharField(verbose_name=_('사용자 이름'), max_length=30)

    is_active = models.BooleanField(verbose_name=_('계정활성'), default=False)
    is_superuser = models.BooleanField(verbose_name=_('관리자'), default=False)

    date_joined = models.DateTimeField(verbose_name=_('수정일'), auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('생성일'), auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'auth_user'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.email}({self.fullname})'

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
