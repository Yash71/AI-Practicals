# ChatBot API
This API provides a simple way to interact with a pre-trained ChatBot model based on the DialogueGPT architecture.

## Base URL
The base URL for the API is http://localhost:5002.

## Endpoints
#### POST /bot
This endpoint accepts a JSON object in the request body with a "query" field containing the message to be sent to the ChatBot. The ChatBot will generate a response based on the message and return it as a JSON object in the following format:

```json
{
    "message": "Hello, how can I assist you today?"
}
```

#### **Request Parameters**
| **Parameter** | **Type** | **Description**                                      |
|---------------|----------|------------------------------------------------------|
| query         | string   | The message to be sent to the ChatBot for processing |

#### Example Request
```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"query": "Hi, can you help me with a reservation?"}' \
    http://localhost:5002/bot
```

#### Example Response
```json
{
    "message": "Of course, what kind of reservation would you like to make?"
}
```

## Installation

Install all the python packages required using the following command.

```bash
pip install -r path/to/requirements.txt
```

## Usage

- Run the app.py file and the api is online
- Now use the chatbot interface webpage to interact with the chatbot.
[Chatbot Webpage](https://github.com/Nitesh-13/Chatbot-Webpage)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)