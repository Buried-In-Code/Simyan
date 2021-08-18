from marshmallow import Schema, fields, post_load, INCLUDE


class PeopleEntry:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class PeopleEntrySchema(Schema):
    api_url = fields.Url(data_key='api_detail_url')
    id = fields.Int()
    name = fields.Str()
    site_url = fields.Url(data_key='site_detail_url')
    count = fields.Str()

    class Meta:
        unknown = INCLUDE

    @post_load
    def make_object(self, data, **kwargs) -> PeopleEntry:
        return PeopleEntry(**data)
