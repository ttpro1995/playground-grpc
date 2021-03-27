import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)
response = stub.add(calculator_pb2.CalRequest(a=1, b=2))
print(response)
print(response.result)

