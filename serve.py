import subprocess
import os
import argparse

def main():
    """
    This script starts the MLX server to serve a model with an OpenAI-compatible API.
    """
    parser = argparse.ArgumentParser(description="Start the MLX server with an OpenAI-compatible API.")
    parser.add_argument("--model", type=str, default="reki-1", help="The path to the model directory.")
    parser.add_argument("--port", type=int, default=8787, help="The port to run the server on.")
    parser.add_argument("--log-level", type=str, default="INFO", help="The log level for the server.")
    args = parser.parse_args()

    model_path = os.path.abspath(args.model)

    command = [
        "venv/bin/mlx_lm.server",
        "--model", model_path,
        "--port", str(args.port),
        "--log-level", args.log_level,
    ]

    print(f"Starting OpenAI-compatible server with command: {' '.join(command)}")
    print(f"API documentation will be available at http://localhost:{args.port}/docs")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
    except FileNotFoundError:
        print("Error: mlx_lm.server not found. Make sure you are in the correct directory and the virtual environment is activated.")

if __name__ == "__main__":
    main()