from rest_framework.serializers import ValidationError


class URLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        print(f'{value=}')
        # tmp_val = str(dict(value).get(self.field))
        if not value.startswith('https://www.youtube.com/'):
            raise ValidationError('Нельзя добавлять сторонние ссылки, кроме youtube')
