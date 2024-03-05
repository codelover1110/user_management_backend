# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE profile_project.settings

# Set the working directory in the container
WORKDIR /app

# Copy the production environment file to the application directory
COPY .env.prod /app/.env

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Run python command
RUN python manage.py makemigrations
RUN python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy your custom Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Remove the default Nginx configuration
RUN rm /etc/nginx/sites-enabled/default

# Create the target directory and a symbolic link to the Nginx configuration file
RUN mkdir -p /etc/nginx/sites-enabled/ && ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Expose port 80 for Nginx
EXPOSE 80

# Start both Gunicorn and Nginx
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 --workers 4 profile_project.wsgi:application & nginx -g 'daemon off;'"]
