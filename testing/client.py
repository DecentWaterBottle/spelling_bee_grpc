import grpc
from testing import secretNumberClass_pb2_grpc, secretNumberClass_pb2

channel = grpc.insecure_channel("localhost:50051")

stub = secretNumberClass_pb2_grpc.SecretNumberStub(channel)

while True:
    num = int(input("Enter a number: "))
    number = secretNumberClass_pb2.Number(value=num)
    response = stub.addSecretNumber(number)
    print(response.value)



