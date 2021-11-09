FROM python:3

# Copy the current directory contents into the container at /fake
COPY . /usr/src/fake

# Set the working directory to /usr/src/fake
WORKDIR /usr/src/fake

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set up database
ENV DB api.db
RUN python db.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the command
CMD [ "python", "./api.py" ]