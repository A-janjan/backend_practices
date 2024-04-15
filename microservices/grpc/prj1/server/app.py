from concurrent import futures
import logging

import grpc
import users_pb2
import users_pb2_grpc


class Users(users_pb2_grpc.UsersServicer):
    def GetUsers(self, request, context):
        return users_pb2.GetUsersResponse(users=[
            users_pb2.User(id='1', name='ali', email='ali@email.com', password='ali@214'),
        ])


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()