import uvicorn


def main():
    """
    Start the server from the command line using the default configuration.
    """
    uvicorn.run(
        app="wsgi:app",
        host="0.0.0.0",
        port=80,
        log_level="debug",
        reload=True,
    )


if __name__ == "__main__":
    main()