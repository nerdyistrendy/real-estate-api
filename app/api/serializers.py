from marshmallow import Schema, fields, validates, ValidationError
import re


class StateSchema(Schema):
    id = fields.Integer()
    description = fields.String(required=True)
    initials = fields.String(required=True)


class LocationSchema(Schema):
    id = fields.Integer()
    postal_code = fields.String(required=True)
    street = fields.String(required=True)
    neighbourhood = fields.String(required=True)
    city = fields.String(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    places_id = fields.String(required=True)
    state = fields.Nested(StateSchema(), required=True)


class PropertySchema(Schema):
    id = fields.Integer()
    area = fields.Integer(required=True)
    price = fields.Float(required=True)
    location = fields.Nested(LocationSchema(), required=True)


class PropertyReaderSchema(Schema):
    area = fields.Integer(required=True)
    price = fields.Float(required=True)
    postal_code = fields.String(required=True)

    @validates("postal_code")
    def validate_postal_code(self, value):
        regex = re.compile(r"[0-9]{5}-[0-9]{3}")
        if not regex.match(value):
            raise ValidationError("postal_code must follow the #####-### pattern.")


class AddressComponentLongName(fields.Field):
    def _deserialize(self, obj, attr, data, **kwargs):
        if obj is None:
            return None
        return obj.get("long_name")


class AddressComponentShortName(fields.Field):
    def _deserialize(self, obj, attr, data, **kwargs):
        if obj is None:
            return None
        return obj.get("short_name")


class PlaceReader(Schema):
    places_id = fields.String(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    street = AddressComponentLongName()
    neighbourhood = AddressComponentLongName()
    city = AddressComponentLongName(required=True)
    state = AddressComponentShortName(required=True)
    postal_code = AddressComponentShortName(required=True)
