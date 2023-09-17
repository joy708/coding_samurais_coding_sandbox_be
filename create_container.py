import docker

# Initialize the Docker client
client = docker.from_env()

# Specify the container image you want to run
image_name = "coding_samurais:1"

host_path = '/Users/user/Desktop/coding-samurais/coding_samurais_coding_sandbox_be/temp/myscript.py'       # Replace with the actual path on your host machine
container_path = '/tmp/src/myscript.py'  # Replace with the desired path inside the container


#write python code to file
def write_python_code_to_file(filename, python_code):
    try:
        # Open the file in write mode
        with open(filename, 'w') as file:
            # Write the Python code to the file
            file.write(python_code)
        print(f"Python code has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


python_code = """
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
"""

write_python_code_to_file('temp/myscript.py', python_code)
# Define the container run parameters
container_options = {
    'detach': True,                  # Run the container in the background
    'volumes': {host_path: {'bind': container_path, 'mode': 'rw'}},
    'tty': True
}
# Number of containers to create
num_containers = 3

# Run a Python script on the third container)

containers = []

for i in range(num_containers):
    try:
        # Define a custom name for the container
        container_name = f"my-wrokers-{i + 1}"

        # Run the container with a custom name
        container = client.containers.run(image_name, name=container_name, **container_options)

        # Print the container ID and name
        print(f"Container {i + 1} Name: {container_name}")
        print(f"Container {i + 1} ID: {container.id}")

        containers.append(container)

    except docker.errors.ImageNotFound:
        print(f"Image {image_name} not found. Please pull it first.")
    except docker.errors.APIError as e:
        print(f"Docker API Error: {e}")

third = containers[2]
res = third.exec_run("python3 /tmp/src/myscript.py")
print(res.output.decode('utf-8'))
# Define the path to your Python script inside the container
