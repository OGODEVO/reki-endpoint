import subprocess
import os

def main():
    """
    This script starts the MLX server to serve the reki-1 model.
    """
    port = 8787
    model_path = os.path.abspath("reki-1")
    
    command = [
        "venv/bin/mlx_lm.server",
        "--model", model_path,
        "--port", str(port),
    ]
    
    print(f"Starting server with command: {' '.join(command)}")
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
    except FileNotFoundError:
        print("Error: mlx_lm.server not found. Make sure you are in the correct directory and the virtual environment is activated.")

if __name__ == "__main__":
    main()
