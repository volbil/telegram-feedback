from webargs import fields

form_args = {
    "h-captcha-response": fields.Str(missing=None),
    "name": fields.Email(required=False),
    "email": fields.Email(required=True),
    "message": fields.Str(required=True),
    "budget": fields.Str(required=False),
    "offers": fields.Bool(required=True)
}
