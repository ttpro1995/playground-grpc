import grpc
import hello_pb2_grpc
import hello_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = hello_pb2_grpc.GreeterStub(channel)
response = stub.SayHello(hello_pb2.HelloRequest(name='you'))
print("Greeter client received: " + response.message)
response = stub.SayHelloAgain(hello_pb2.HelloRequest(name='you'))
print("Greeter client received: " + response.message)
response = stub.SayHelloAgain(hello_pb2.HelloRequest(name='meow'))
print(response)
