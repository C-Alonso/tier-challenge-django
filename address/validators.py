from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(theUrl):
    url_validator = URLValidator()

    try:
        url_validator(theUrl)
    except:
        try:
            url_validator('http://' + theUrl)
        except:
            raise ValidationError("Please enter a valid URL") 

    