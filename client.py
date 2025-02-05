import zmq
import time

context = zmq.Context()

print("Connecting to the server...")

time.sleep(1)

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print(f"Sending request to the server...")
time.sleep(1)

socket.send_string("Get comment from server")
message = socket.recv()

time.sleep(1)

print(f"Received reply from the server: {message.decode()}")
socket.send_string("Q")
