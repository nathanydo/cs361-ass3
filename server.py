import time
import zmq

# ZeroMQ Context
context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for next request from client
    message = socket.recv()
    print(f"Received request from the client: {message.decode()}")

    if len(message) > 0:
        if message.decode() == 'Q':
            print("Received Q, exiting...")
            break
    
        time.sleep(1)

        comment = "This is a message from CS361"

        print(f'Sending "{comment}" to the client')

        time.sleep(1)

        # Send reply back to client
        socket.send_string(comment)

context.destroy()