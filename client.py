from __future__ import print_function

import grpc

import grpc_pb2
import grpc_pb2_grpc

from PIL import Image
from io import BytesIO


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_pb2_grpc.GreeterStub(channel)
        image = Image.open('input.jpg')
        out = BytesIO()
        image.save(out, format='jpeg')
        v = out.getvalue()
        response = stub.SayHello(grpc_pb2.HelloRequest(image=v))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()