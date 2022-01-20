from webargs import fields

form_args = {
    "h-captcha-response": fields.Str(missing=None),
    "email": fields.Email(required=True),
    "message": fields.Str(required=True),
    "offers": fields.Bool(required=True)
}
