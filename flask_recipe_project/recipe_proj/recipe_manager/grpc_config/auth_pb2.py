# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\"\x1c\n\x0b\x41uthRequest\x12\r\n\x05token\x18\x01 \x01(\t\"0\n\x0c\x41uthResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x32:\n\x0b\x41uthService\x12+\n\x0c\x41uthenticate\x12\x0c.AuthRequest\x1a\r.AuthResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AUTHREQUEST']._serialized_start=14
  _globals['_AUTHREQUEST']._serialized_end=42
  _globals['_AUTHRESPONSE']._serialized_start=44
  _globals['_AUTHRESPONSE']._serialized_end=92
  _globals['_AUTHSERVICE']._serialized_start=94
  _globals['_AUTHSERVICE']._serialized_end=152
# @@protoc_insertion_point(module_scope)