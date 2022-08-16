from webargs import fields

form_args = {
    "h-captcha-response": fields.Str(missing=None),
    "name": fields.Email(missing=""),
    "email": fields.Email(required=True),
    "message": fields.Str(required=True),
    "budget": fields.Str(missing=""),
    "offers": fields.Bool(required=True)
}
