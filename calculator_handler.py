import calculator_pb2_grpc
import calculator_pb2
import grpc
from concurrent import futures
import logging


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def add(self, requests: calculator_pb2.CalRequest, context):
        a = requests.a
        b = requests.b
        c = a + b
        return calculator_pb2.CalResult(result=c)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()