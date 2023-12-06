# NewsAPI Fetcher

A Python script that utilizes the [NewsAPI](https://newsapi.org/) to retrieve and display news articles related to Tesla.

## Prerequisites

- Python 3.x
- [Requests](https://docs.python-requests.org/en/latest/) library
- NewsAPI key (Sign up [here](https://newsapi.org/register) to obtain your key)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/newsapi-fetcher.git
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your NewsAPI key:

    - Create an account on [NewsAPI](https://newsapi.org/register) to obtain your API key.
    - Set the 'NEWSAPI' environment variable with your API key:

        ```bash
        export NEWSAPI=your-api-key
        ```

4. Run the script:

    ```bash
    python newsapi_fetcher.py
    ```

## Features

- Fetches news articles related to Tesla using the NewsAPI.
- Displays the titles of the fetched articles.

## Error Handling

- Checks for the presence of the 'NEWSAPI' environment variable.
- Handles request timeouts and other request exceptions.

## Contributing

If you find any issues or have improvements to suggest, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
