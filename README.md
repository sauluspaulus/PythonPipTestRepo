# PythonPipTestRepo


Download Red Hat Universal Base Image 8:
>podman pull registry.access.redhat.com/ubi8/ubi:8.6-990

Clone the repo from github:
>git clone https://github.com/sauluspaulus/PythonPipTestRepo

Build the image:
>sudo podman build -t [name] .

Run the Image
>sudo podman run [name] -p 80:8080
