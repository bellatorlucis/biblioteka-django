from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View


class SluzbenikGroupRequiredMixin(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.groups.filter(name='sluzbenik').exists()