# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from service_spec import DSSMService_pb2 as service__spec_dot_DSSMService__pb2


class DSSMStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.semantic_modeling = channel.unary_unary(
        '/DSSM/semantic_modeling',
        request_serializer=service__spec_dot_DSSMService__pb2.DSSMRequest.SerializeToString,
        response_deserializer=service__spec_dot_DSSMService__pb2.DSSMResponse.FromString,
        )


class DSSMServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def semantic_modeling(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DSSMServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'semantic_modeling': grpc.unary_unary_rpc_method_handler(
          servicer.semantic_modeling,
          request_deserializer=service__spec_dot_DSSMService__pb2.DSSMRequest.FromString,
          response_serializer=service__spec_dot_DSSMService__pb2.DSSMResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DSSM', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
