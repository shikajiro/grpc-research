from concurrent import futures
import time

import grpc

import grpc_pb2
import grpc_pb2_grpc

from PIL import Image
from io import BytesIO

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(grpc_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        image = Image.open(BytesIO(request.images))
        image.save('output.jpg', format='jpeg')
        return grpc_pb2.HelloReply(message='saved output.jpg')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()