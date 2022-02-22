from django.core.exceptions import ValidationError


def validate_phone_number_min_length(value):
    if len(str(value)) < 10:
        return ValidationError('Phone must be at least 10 numbers')
