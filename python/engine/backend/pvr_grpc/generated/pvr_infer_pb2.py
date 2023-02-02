# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine/backend/pvr_grpc/generated/pvr_infer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='engine/backend/pvr_grpc/generated/pvr_infer.proto',
  package='pvr',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1engine/backend/pvr_grpc/generated/pvr_infer.proto\x12\x03pvr\"*\n\x12\x46indServiceRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\"*\n\x13\x46indServiceResponse\x12\x13\n\x0bservice_ack\x18\x01 \x01(\t\"$\n\x06Tensor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"+\n\x0cInferRequest\x12\x1b\n\x06inputs\x18\x01 \x03(\x0b\x32\x0b.pvr.Tensor\"-\n\rInferResponse\x12\x1c\n\x07outputs\x18\x01 \x03(\x0b\x32\x0b.pvr.Tensor2\x84\x01\n\x08PVRInfer\x12\x42\n\x0b\x46indService\x12\x17.pvr.FindServiceRequest\x1a\x18.pvr.FindServiceResponse\"\x00\x12\x34\n\tInference\x12\x11.pvr.InferRequest\x1a\x12.pvr.InferResponse\"\x00\x62\x06proto3'
)




_FINDSERVICEREQUEST = _descriptor.Descriptor(
  name='FindServiceRequest',
  full_name='pvr.FindServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='pvr.FindServiceRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=100,
)


_FINDSERVICERESPONSE = _descriptor.Descriptor(
  name='FindServiceResponse',
  full_name='pvr.FindServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_ack', full_name='pvr.FindServiceResponse.service_ack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=144,
)


_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='pvr.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pvr.Tensor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='pvr.Tensor.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=182,
)


_INFERREQUEST = _descriptor.Descriptor(
  name='InferRequest',
  full_name='pvr.InferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='pvr.InferRequest.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=227,
)


_INFERRESPONSE = _descriptor.Descriptor(
  name='InferResponse',
  full_name='pvr.InferResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='pvr.InferResponse.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=274,
)

_INFERREQUEST.fields_by_name['inputs'].message_type = _TENSOR
_INFERRESPONSE.fields_by_name['outputs'].message_type = _TENSOR
DESCRIPTOR.message_types_by_name['FindServiceRequest'] = _FINDSERVICEREQUEST
DESCRIPTOR.message_types_by_name['FindServiceResponse'] = _FINDSERVICERESPONSE
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
DESCRIPTOR.message_types_by_name['InferRequest'] = _INFERREQUEST
DESCRIPTOR.message_types_by_name['InferResponse'] = _INFERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FindServiceRequest = _reflection.GeneratedProtocolMessageType('FindServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDSERVICEREQUEST,
  '__module__' : 'engine.backend.pvr_grpc.generated.pvr_infer_pb2'
  # @@protoc_insertion_point(class_scope:pvr.FindServiceRequest)
  })
_sym_db.RegisterMessage(FindServiceRequest)

FindServiceResponse = _reflection.GeneratedProtocolMessageType('FindServiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDSERVICERESPONSE,
  '__module__' : 'engine.backend.pvr_grpc.generated.pvr_infer_pb2'
  # @@protoc_insertion_point(class_scope:pvr.FindServiceResponse)
  })
_sym_db.RegisterMessage(FindServiceResponse)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'engine.backend.pvr_grpc.generated.pvr_infer_pb2'
  # @@protoc_insertion_point(class_scope:pvr.Tensor)
  })
_sym_db.RegisterMessage(Tensor)

InferRequest = _reflection.GeneratedProtocolMessageType('InferRequest', (_message.Message,), {
  'DESCRIPTOR' : _INFERREQUEST,
  '__module__' : 'engine.backend.pvr_grpc.generated.pvr_infer_pb2'
  # @@protoc_insertion_point(class_scope:pvr.InferRequest)
  })
_sym_db.RegisterMessage(InferRequest)

InferResponse = _reflection.GeneratedProtocolMessageType('InferResponse', (_message.Message,), {
  'DESCRIPTOR' : _INFERRESPONSE,
  '__module__' : 'engine.backend.pvr_grpc.generated.pvr_infer_pb2'
  # @@protoc_insertion_point(class_scope:pvr.InferResponse)
  })
_sym_db.RegisterMessage(InferResponse)



_PVRINFER = _descriptor.ServiceDescriptor(
  name='PVRInfer',
  full_name='pvr.PVRInfer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=277,
  serialized_end=409,
  methods=[
  _descriptor.MethodDescriptor(
    name='FindService',
    full_name='pvr.PVRInfer.FindService',
    index=0,
    containing_service=None,
    input_type=_FINDSERVICEREQUEST,
    output_type=_FINDSERVICERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Inference',
    full_name='pvr.PVRInfer.Inference',
    index=1,
    containing_service=None,
    input_type=_INFERREQUEST,
    output_type=_INFERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PVRINFER)

DESCRIPTOR.services_by_name['PVRInfer'] = _PVRINFER

# @@protoc_insertion_point(module_scope)
