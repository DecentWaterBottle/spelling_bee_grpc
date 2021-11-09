# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngame.proto\"\x07\n\x05\x45mpty\"\x14\n\x04Word\x12\x0c\n\x04word\x18\x01 \x01(\t\" \n\nDifficulty\x12\x12\n\ndifficulty\x18\x01 \x01(\t\"\'\n\x05Score\x12\x0f\n\x07outcome\x18\x01 \x01(\x08\x12\r\n\x05score\x18\x02 \x01(\x05\"\x16\n\x05Words\x12\r\n\x05words\x18\x01 \x01(\t\"4\n\x07Letters\x12\x14\n\x0cgame_letters\x18\x01 \x01(\t\x12\x13\n\x0bmain_letter\x18\x02 \x01(\t2\xb7\x01\n\x0fSpellingBeeGame\x12\'\n\x0eSendDifficulty\x12\x0b.Difficulty\x1a\x08.Letters\x12\x1a\n\tCheckWord\x12\x05.Word\x1a\x06.Score\x12\x1f\n\x0bSendLetters\x12\x06.Empty\x1a\x08.Letters\x12\x1e\n\x0cGetUserWords\x12\x06.Empty\x1a\x06.Words\x12\x1e\n\x0cGetUserScore\x12\x06.Empty\x1a\x06.Scoreb\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=14,
  serialized_end=21,
)


_WORD = _descriptor.Descriptor(
  name='Word',
  full_name='Word',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='Word.word', index=0,
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
  serialized_start=23,
  serialized_end=43,
)


_DIFFICULTY = _descriptor.Descriptor(
  name='Difficulty',
  full_name='Difficulty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='Difficulty.difficulty', index=0,
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
  serialized_start=45,
  serialized_end=77,
)


_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='outcome', full_name='Score.outcome', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='Score.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=118,
)


_WORDS = _descriptor.Descriptor(
  name='Words',
  full_name='Words',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='Words.words', index=0,
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
  serialized_start=120,
  serialized_end=142,
)


_LETTERS = _descriptor.Descriptor(
  name='Letters',
  full_name='Letters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_letters', full_name='Letters.game_letters', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='main_letter', full_name='Letters.main_letter', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=144,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Word'] = _WORD
DESCRIPTOR.message_types_by_name['Difficulty'] = _DIFFICULTY
DESCRIPTOR.message_types_by_name['Score'] = _SCORE
DESCRIPTOR.message_types_by_name['Words'] = _WORDS
DESCRIPTOR.message_types_by_name['Letters'] = _LETTERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
  'DESCRIPTOR' : _WORD,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:Word)
  })
_sym_db.RegisterMessage(Word)

Difficulty = _reflection.GeneratedProtocolMessageType('Difficulty', (_message.Message,), {
  'DESCRIPTOR' : _DIFFICULTY,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:Difficulty)
  })
_sym_db.RegisterMessage(Difficulty)

Score = _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), {
  'DESCRIPTOR' : _SCORE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:Score)
  })
_sym_db.RegisterMessage(Score)

Words = _reflection.GeneratedProtocolMessageType('Words', (_message.Message,), {
  'DESCRIPTOR' : _WORDS,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:Words)
  })
_sym_db.RegisterMessage(Words)

Letters = _reflection.GeneratedProtocolMessageType('Letters', (_message.Message,), {
  'DESCRIPTOR' : _LETTERS,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:Letters)
  })
_sym_db.RegisterMessage(Letters)



_SPELLINGBEEGAME = _descriptor.ServiceDescriptor(
  name='SpellingBeeGame',
  full_name='SpellingBeeGame',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=199,
  serialized_end=382,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendDifficulty',
    full_name='SpellingBeeGame.SendDifficulty',
    index=0,
    containing_service=None,
    input_type=_DIFFICULTY,
    output_type=_LETTERS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckWord',
    full_name='SpellingBeeGame.CheckWord',
    index=1,
    containing_service=None,
    input_type=_WORD,
    output_type=_SCORE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendLetters',
    full_name='SpellingBeeGame.SendLetters',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_LETTERS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserWords',
    full_name='SpellingBeeGame.GetUserWords',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_WORDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserScore',
    full_name='SpellingBeeGame.GetUserScore',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_SCORE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPELLINGBEEGAME)

DESCRIPTOR.services_by_name['SpellingBeeGame'] = _SPELLINGBEEGAME

# @@protoc_insertion_point(module_scope)
