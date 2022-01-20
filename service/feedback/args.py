from webargs import fields

form_args = {
    "email": fields.Email(required=True),
    "message": fields.Str(required=True),
    "offers": fields.Bool(required=True)
}
