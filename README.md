# ZeroMQ Spike

This program is a spike for two programs: one that sends and one that receives messages using ZeroMQ.

## Prerequisites

- Python 3.x
- ZeroMQ library (`pyzmq`)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install pyzmq
    ```

## Usage

### Sender

To run the sender program:
```sh
python sender.py
```

### Receiver

To run the receiver program:
```sh
python receiver.py
```

## Description

- `sender.py`: This program sends messages to a specified endpoint using ZeroMQ.
- `receiver.py`: This program receives messages from a specified endpoint using ZeroMQ.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.