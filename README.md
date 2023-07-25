# nipun-pythonapi
# Simple API Server

This is a simple API server written in Python that provides two endpoints: `/ping` and `/password`. The `/ping` endpoint responds with "Pong" when accessed, and the `/password` endpoint generates and returns a random password using a custom password generation library.
## How to Run the Server

1. Install Python if you haven't already (version 3.x is recommended).
2. Clone this repository to your local machine.
3. Navigate to the project directory.

4. Install the required library for password generation. (Make sure you have the `passwordP` library installed or provide instructions to install it.)

5. Run the server by executing the following command:
6. The server will start running on `http://localhost:8080/`.
## Available Endpoints

### `/ping`
- Method: GET
- Response: "Pong"

### `/password`
- Method: GET
- Response: Randomly generated password string

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



