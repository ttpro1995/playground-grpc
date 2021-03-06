# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\"\"\n\nCalRequest\x12\t\n\x01\x61\x18\x01 \x02(\x05\x12\t\n\x01\x62\x18\x02 \x02(\x05\"\x1b\n\tCalResult\x12\x0e\n\x06result\x18\x01 \x02(\x05\x32.\n\nCalculator\x12 \n\x03\x61\x64\x64\x12\x0b.CalRequest\x1a\n.CalResult\"\x00'
)




_CALREQUEST = _descriptor.Descriptor(
  name='CalRequest',
  full_name='CalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='CalRequest.a', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='CalRequest.b', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=54,
)


_CALRESULT = _descriptor.Descriptor(
  name='CalResult',
  full_name='CalResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CalResult.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['CalRequest'] = _CALREQUEST
DESCRIPTOR.message_types_by_name['CalResult'] = _CALRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalRequest = _reflection.GeneratedProtocolMessageType('CalRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalRequest)
  })
_sym_db.RegisterMessage(CalRequest)

CalResult = _reflection.GeneratedProtocolMessageType('CalResult', (_message.Message,), {
  'DESCRIPTOR' : _CALRESULT,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalResult)
  })
_sym_db.RegisterMessage(CalResult)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=85,
  serialized_end=131,
  methods=[
  _descriptor.MethodDescriptor(
    name='add',
    full_name='Calculator.add',
    index=0,
    containing_service=None,
    input_type=_CALREQUEST,
    output_type=_CALRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
