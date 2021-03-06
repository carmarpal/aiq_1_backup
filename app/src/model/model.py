from dataclasses import dataclass
from marshmallow import fields, Schema, post_load, INCLUDE


# Request marshmallow expected, you can add validation
class RequestSchema(Schema):
    # Allow unkown fields
    class Meta:
        unknown = INCLUDE

    # Schema
    N = fields.Integer(required=False)
    state = fields.String(required=False)
    @post_load
    def make(self, data, **kwargs):
        N = data['N']
        state = data['state']
        return N, state


# Response marshmallow json response
class ResponseSchema(Schema):
    modelScore = fields.Float()
    explicability = fields.Dict(missing=None, required=False)
    transformations = fields.List(fields.Float(missing=None, required=False))
    transformations_dic = fields.Dict(missing=None, required=False)
    errorCode = fields.Integer(allow_nan=True, allow_none=True)
    errorMessage = fields.String(allow_nan=True)