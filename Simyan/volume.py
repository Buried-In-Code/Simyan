"""
Volume module.

This module provides the following classes:

- Volume
- VolumeSchema
"""
from typing import Any, Dict

from marshmallow import EXCLUDE, Schema, fields, post_load

from Simyan.generic_entries import CountEntrySchema, GenericEntrySchema, ImageEntrySchema, IssueEntrySchema


class Volume:
    r"""
    The Volume object contains information for a volume.

    Args:
        **kwargs: The keyword argument is used for setting Volume data from ComicVine.

    Attributes:
        aliases (str): List of names the Volume has used, separated by ``\n``.
        api_url (str): Url to the ComicVine API.
        characters (list of :obj: `CountEntry`): List of characters in the Volume.
        concepts (list of :obj: `CountEntry`): List of concepts in the Volume.
        creators (list of :obj: `CountEntry`): List of creators in the Volume.
        date_added (datetime): Date and time when the Volume was added to ComicVine.
        date_last_updated (datetime): Date and time when the Volume was updated on ComicVine.
        description (str, Optional): Long description of the Volume.
        first_issue (:obj: `IssueEntry`): First issue of the Volume.
        id (int): Identifier used in ComicVine.
        image (:obj: `ImageEntry`): Different sized images, posters and thumbnails for the Volume.
        issue_count (int): Number of issues in the Volume.
        issues (list of :obj: `IssueEntry`): List of issues in the Volume.
        last_issue (:obj: `IssueEntry`): Last issue of the Volume.
        locations (list of :obj: `CountEntry`): List of locations in the Volume.
        name (str): Name/Title of the Volume.
        objects (list of :obj: `CountEntry`): List of objects in the Volume.
        publisher (:obj: `GenericEntry`): The publisher of the Volume.
        site_url (str): Url to the ComicVine Website.
        start_year (int): The year the Volume started.
        summary (str, Optional): Short description of the Volume.
    """

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class VolumeSchema(Schema):
    """Schema for the Volume API."""

    aliases = fields.Str(allow_none=True)
    api_url = fields.Url(data_key="api_detail_url")
    characters = fields.Nested(CountEntrySchema, many=True)
    concepts = fields.Nested(CountEntrySchema, many=True)
    creators = fields.Nested(CountEntrySchema, data_key="people", many=True)
    date_added = fields.DateTime()
    date_last_updated = fields.DateTime()
    description = fields.Str(allow_none=True)
    first_issue = fields.Nested(IssueEntrySchema)
    id = fields.Int()
    image = fields.Nested(ImageEntrySchema)
    issue_count = fields.Int(data_key="count_of_issues")
    issues = fields.Nested(IssueEntrySchema, many=True)
    last_issue = fields.Nested(IssueEntrySchema)
    locations = fields.Nested(CountEntrySchema, many=True)
    name = fields.Str()
    objects = fields.Nested(CountEntrySchema, many=True)
    publisher = fields.Nested(GenericEntrySchema)
    site_url = fields.Url(data_key="site_detail_url")
    start_year = fields.Int()
    summary = fields.Str(data_key="deck", allow_none=True)

    class Meta:
        """Any unknown fields will be excluded."""

        unknown = EXCLUDE
        dateformat = "%Y-%m-%d %H:%M:%S"
        datetimeformat = "%Y-%m-%d %H:%M:%S"

    @post_load
    def make_object(self, data: Dict[str, Any], **kwargs) -> Volume:
        """
        Make the Volume object.

        Args:
            data: Data from the ComicVine response.
            **kwargs:

        Returns:
            A `Volume` object
        """
        return Volume(**data)
