# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/secretmanager_v1/proto/resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/secretmanager_v1/proto/resources.proto",
    package="google.cloud.secretmanager.v1",
    syntax="proto3",
    serialized_options=b"\n!com.google.cloud.secretmanager.v1B\016ResourcesProtoP\001ZJgoogle.golang.org/genproto/googleapis/cloud/secretmanager/v1;secretmanager\370\001\001\242\002\003GSM\252\002\035Google.Cloud.SecretManager.V1\312\002\035Google\\Cloud\\SecretManager\\V1\352\002 Google::Cloud::SecretManager::V1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n3google/cloud/secretmanager_v1/proto/resources.proto\x12\x1dgoogle.cloud.secretmanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"\xdb\x02\n\x06Secret\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03\x12G\n\x0breplication\x18\x02 \x01(\x0b\x32*.google.cloud.secretmanager.v1.ReplicationB\x06\xe0\x41\x05\xe0\x41\x02\x12\x34\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x41\n\x06labels\x18\x04 \x03(\x0b\x32\x31.google.cloud.secretmanager.v1.Secret.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:M\xea\x41J\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}"\x91\x03\n\rSecretVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03\x12\x34\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x35\n\x0c\x64\x65stroy_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x46\n\x05state\x18\x04 \x01(\x0e\x32\x32.google.cloud.secretmanager.v1.SecretVersion.StateB\x03\xe0\x41\x03"H\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12\r\n\tDESTROYED\x10\x03:n\xea\x41k\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}"\xc8\x02\n\x0bReplication\x12I\n\tautomatic\x18\x01 \x01(\x0b\x32\x34.google.cloud.secretmanager.v1.Replication.AutomaticH\x00\x12N\n\x0cuser_managed\x18\x02 \x01(\x0b\x32\x36.google.cloud.secretmanager.v1.Replication.UserManagedH\x00\x1a\x0b\n\tAutomatic\x1a\x81\x01\n\x0bUserManaged\x12U\n\x08replicas\x18\x01 \x03(\x0b\x32>.google.cloud.secretmanager.v1.Replication.UserManaged.ReplicaB\x03\xe0\x41\x02\x1a\x1b\n\x07Replica\x12\x10\n\x08location\x18\x01 \x01(\tB\r\n\x0breplication"\x1d\n\rSecretPayload\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x42\xed\x01\n!com.google.cloud.secretmanager.v1B\x0eResourcesProtoP\x01ZJgoogle.golang.org/genproto/googleapis/cloud/secretmanager/v1;secretmanager\xf8\x01\x01\xa2\x02\x03GSM\xaa\x02\x1dGoogle.Cloud.SecretManager.V1\xca\x02\x1dGoogle\\Cloud\\SecretManager\\V1\xea\x02 Google::Cloud::SecretManager::V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_SECRETVERSION_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.cloud.secretmanager.v1.SecretVersion.State",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ENABLED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DISABLED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DESTROYED",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=777,
    serialized_end=849,
)
_sym_db.RegisterEnumDescriptor(_SECRETVERSION_STATE)


_SECRET_LABELSENTRY = _descriptor.Descriptor(
    name="LabelsEntry",
    full_name="google.cloud.secretmanager.v1.Secret.LabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.secretmanager.v1.Secret.LabelsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.secretmanager.v1.Secret.LabelsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=433,
    serialized_end=478,
)

_SECRET = _descriptor.Descriptor(
    name="Secret",
    full_name="google.cloud.secretmanager.v1.Secret",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.secretmanager.v1.Secret.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="replication",
            full_name="google.cloud.secretmanager.v1.Secret.replication",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\005\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.secretmanager.v1.Secret.create_time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.cloud.secretmanager.v1.Secret.labels",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_SECRET_LABELSENTRY,],
    enum_types=[],
    serialized_options=b"\352AJ\n#secretmanager.googleapis.com/Secret\022#projects/{project}/secrets/{secret}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=210,
    serialized_end=557,
)


_SECRETVERSION = _descriptor.Descriptor(
    name="SecretVersion",
    full_name="google.cloud.secretmanager.v1.SecretVersion",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.secretmanager.v1.SecretVersion.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.secretmanager.v1.SecretVersion.create_time",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="destroy_time",
            full_name="google.cloud.secretmanager.v1.SecretVersion.destroy_time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.cloud.secretmanager.v1.SecretVersion.state",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SECRETVERSION_STATE,],
    serialized_options=b"\352Ak\n*secretmanager.googleapis.com/SecretVersion\022=projects/{project}/secrets/{secret}/versions/{secret_version}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=560,
    serialized_end=961,
)


_REPLICATION_AUTOMATIC = _descriptor.Descriptor(
    name="Automatic",
    full_name="google.cloud.secretmanager.v1.Replication.Automatic",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1134,
    serialized_end=1145,
)

_REPLICATION_USERMANAGED_REPLICA = _descriptor.Descriptor(
    name="Replica",
    full_name="google.cloud.secretmanager.v1.Replication.UserManaged.Replica",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="location",
            full_name="google.cloud.secretmanager.v1.Replication.UserManaged.Replica.location",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1250,
    serialized_end=1277,
)

_REPLICATION_USERMANAGED = _descriptor.Descriptor(
    name="UserManaged",
    full_name="google.cloud.secretmanager.v1.Replication.UserManaged",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="replicas",
            full_name="google.cloud.secretmanager.v1.Replication.UserManaged.replicas",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_REPLICATION_USERMANAGED_REPLICA,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1148,
    serialized_end=1277,
)

_REPLICATION = _descriptor.Descriptor(
    name="Replication",
    full_name="google.cloud.secretmanager.v1.Replication",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="automatic",
            full_name="google.cloud.secretmanager.v1.Replication.automatic",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="user_managed",
            full_name="google.cloud.secretmanager.v1.Replication.user_managed",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_REPLICATION_AUTOMATIC, _REPLICATION_USERMANAGED,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="replication",
            full_name="google.cloud.secretmanager.v1.Replication.replication",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=964,
    serialized_end=1292,
)


_SECRETPAYLOAD = _descriptor.Descriptor(
    name="SecretPayload",
    full_name="google.cloud.secretmanager.v1.SecretPayload",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="google.cloud.secretmanager.v1.SecretPayload.data",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1294,
    serialized_end=1323,
)

_SECRET_LABELSENTRY.containing_type = _SECRET
_SECRET.fields_by_name["replication"].message_type = _REPLICATION
_SECRET.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SECRET.fields_by_name["labels"].message_type = _SECRET_LABELSENTRY
_SECRETVERSION.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SECRETVERSION.fields_by_name[
    "destroy_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SECRETVERSION.fields_by_name["state"].enum_type = _SECRETVERSION_STATE
_SECRETVERSION_STATE.containing_type = _SECRETVERSION
_REPLICATION_AUTOMATIC.containing_type = _REPLICATION
_REPLICATION_USERMANAGED_REPLICA.containing_type = _REPLICATION_USERMANAGED
_REPLICATION_USERMANAGED.fields_by_name[
    "replicas"
].message_type = _REPLICATION_USERMANAGED_REPLICA
_REPLICATION_USERMANAGED.containing_type = _REPLICATION
_REPLICATION.fields_by_name["automatic"].message_type = _REPLICATION_AUTOMATIC
_REPLICATION.fields_by_name["user_managed"].message_type = _REPLICATION_USERMANAGED
_REPLICATION.oneofs_by_name["replication"].fields.append(
    _REPLICATION.fields_by_name["automatic"]
)
_REPLICATION.fields_by_name["automatic"].containing_oneof = _REPLICATION.oneofs_by_name[
    "replication"
]
_REPLICATION.oneofs_by_name["replication"].fields.append(
    _REPLICATION.fields_by_name["user_managed"]
)
_REPLICATION.fields_by_name[
    "user_managed"
].containing_oneof = _REPLICATION.oneofs_by_name["replication"]
DESCRIPTOR.message_types_by_name["Secret"] = _SECRET
DESCRIPTOR.message_types_by_name["SecretVersion"] = _SECRETVERSION
DESCRIPTOR.message_types_by_name["Replication"] = _REPLICATION
DESCRIPTOR.message_types_by_name["SecretPayload"] = _SECRETPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Secret = _reflection.GeneratedProtocolMessageType(
    "Secret",
    (_message.Message,),
    {
        "LabelsEntry": _reflection.GeneratedProtocolMessageType(
            "LabelsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SECRET_LABELSENTRY,
                "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.Secret.LabelsEntry)
            },
        ),
        "DESCRIPTOR": _SECRET,
        "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2",
        "__doc__": """A [Secret][google.cloud.secretmanager.v1.Secret] is a logical secret
  whose value and versions can be accessed.  A
  [Secret][google.cloud.secretmanager.v1.Secret] is made up of zero or
  more [SecretVersions][google.cloud.secretmanager.v1.SecretVersion]
  that represent the secret data.
  
  Attributes:
      name:
          Output only. The resource name of the
          [Secret][google.cloud.secretmanager.v1.Secret] in the format
          ``projects/*/secrets/*``.
      replication:
          Required. Immutable. The replication policy of the secret data
          attached to the
          [Secret][google.cloud.secretmanager.v1.Secret].  The
          replication policy cannot be changed after the Secret has been
          created.
      create_time:
          Output only. The time at which the
          [Secret][google.cloud.secretmanager.v1.Secret] was created.
      labels:
          The labels assigned to this Secret.  Label keys must be
          between 1 and 63 characters long, have a UTF-8 encoding of
          maximum 128 bytes, and must conform to the following PCRE
          regular expression:
          ``[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}``  Label values
          must be between 0 and 63 characters long, have a UTF-8
          encoding of maximum 128 bytes, and must conform to the
          following PCRE regular expression:
          ``[\p{Ll}\p{Lo}\p{N}_-]{0,63}``  No more than 64 labels can be
          assigned to a given resource.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.Secret)
    },
)
_sym_db.RegisterMessage(Secret)
_sym_db.RegisterMessage(Secret.LabelsEntry)

SecretVersion = _reflection.GeneratedProtocolMessageType(
    "SecretVersion",
    (_message.Message,),
    {
        "DESCRIPTOR": _SECRETVERSION,
        "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2",
        "__doc__": """A secret version resource in the Secret Manager API.
  
  Attributes:
      name:
          Output only. The resource name of the
          [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
          in the format ``projects/*/secrets/*/versions/*``.
          [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
          IDs in a [Secret][google.cloud.secretmanager.v1.Secret] start
          at 1 and are incremented for each subsequent version of the
          secret.
      create_time:
          Output only. The time at which the
          [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
          was created.
      destroy_time:
          Output only. The time this
          [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
          was destroyed. Only present if
          [state][google.cloud.secretmanager.v1.SecretVersion.state] is 
          [DESTROYED][google.cloud.secretmanager.v1.SecretVersion.State.
          DESTROYED].
      state:
          Output only. The current state of the
          [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.SecretVersion)
    },
)
_sym_db.RegisterMessage(SecretVersion)

Replication = _reflection.GeneratedProtocolMessageType(
    "Replication",
    (_message.Message,),
    {
        "Automatic": _reflection.GeneratedProtocolMessageType(
            "Automatic",
            (_message.Message,),
            {
                "DESCRIPTOR": _REPLICATION_AUTOMATIC,
                "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2",
                "__doc__": """A replication policy that replicates the
    [Secret][google.cloud.secretmanager.v1.Secret] payload without any
    restrictions.""",
                # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.Replication.Automatic)
            },
        ),
        "UserManaged": _reflection.GeneratedProtocolMessageType(
            "UserManaged",
            (_message.Message,),
            {
                "Replica": _reflection.GeneratedProtocolMessageType(
                    "Replica",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _REPLICATION_USERMANAGED_REPLICA,
                        "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2",
                        "__doc__": """Represents a Replica for this
      [Secret][google.cloud.secretmanager.v1.Secret].
      
      Attributes:
          location:
              The canonical IDs of the location to replicate data. For
              example: ``"us-east1"``.
      """,
                        # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.Replication.UserManaged.Replica)
                    },
                ),
                "DESCRIPTOR": _REPLICATION_USERMANAGED,
                "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2",
                "__doc__": """A replication policy that replicates the
    [Secret][google.cloud.secretmanager.v1.Secret] payload into the
    locations specified in [Secret.replication.user_managed.replicas][]
    
    Attributes:
        replicas:
            Required. The list of Replicas for this
            [Secret][google.cloud.secretmanager.v1.Secret].  Cannot be
            empty.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.Replication.UserManaged)
            },
        ),
        "DESCRIPTOR": _REPLICATION,
        "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2",
        "__doc__": """A policy that defines the replication configuration of data.
  
  Attributes:
      replication:
          The replication policy for this secret.
      automatic:
          The [Secret][google.cloud.secretmanager.v1.Secret] will
          automatically be replicated without any restrictions.
      user_managed:
          The [Secret][google.cloud.secretmanager.v1.Secret] will only
          be replicated into the locations specified.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.Replication)
    },
)
_sym_db.RegisterMessage(Replication)
_sym_db.RegisterMessage(Replication.Automatic)
_sym_db.RegisterMessage(Replication.UserManaged)
_sym_db.RegisterMessage(Replication.UserManaged.Replica)

SecretPayload = _reflection.GeneratedProtocolMessageType(
    "SecretPayload",
    (_message.Message,),
    {
        "DESCRIPTOR": _SECRETPAYLOAD,
        "__module__": "google.cloud.secretmanager_v1.proto.resources_pb2",
        "__doc__": """A secret payload resource in the Secret Manager API. This contains the
  sensitive secret payload that is associated with a
  [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
  
  Attributes:
      data:
          The secret data. Must be no larger than 64KiB.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.secretmanager.v1.SecretPayload)
    },
)
_sym_db.RegisterMessage(SecretPayload)


DESCRIPTOR._options = None
_SECRET_LABELSENTRY._options = None
_SECRET.fields_by_name["name"]._options = None
_SECRET.fields_by_name["replication"]._options = None
_SECRET.fields_by_name["create_time"]._options = None
_SECRET._options = None
_SECRETVERSION.fields_by_name["name"]._options = None
_SECRETVERSION.fields_by_name["create_time"]._options = None
_SECRETVERSION.fields_by_name["destroy_time"]._options = None
_SECRETVERSION.fields_by_name["state"]._options = None
_SECRETVERSION._options = None
_REPLICATION_USERMANAGED.fields_by_name["replicas"]._options = None
# @@protoc_insertion_point(module_scope)
