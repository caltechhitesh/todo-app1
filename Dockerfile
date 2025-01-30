# Use an official Python image as a base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the app files into the container
COPY . .

# Set default command to run the script
CMD ["python", "todo.py"]

