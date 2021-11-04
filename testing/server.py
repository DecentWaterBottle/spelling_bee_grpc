
import grpc

import secretNumberClass_pb2
import secretNumberClass_pb2_grpc
from concurrent import futures
import time

import secretNumberClass


class SecretNumberService(secretNumberClass_pb2_grpc.SecretNumberServicer):
    def addSecretNumber(self, request, context):
        response = secretNumberClass_pb2.Number()
        response.value = secretNumberClass.addSecretNumber(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
secretNumberClass_pb2_grpc.add_SecretNumberServicer_to_server(SecretNumberService(), server)

print("Starting server")
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(60000)
except KeyboardInterrupt:
    server.stop(0)
