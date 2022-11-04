# PythonPipTestRepo


Download Red Hat Universal Base Image 8:
>podman pull registry.access.redhat.com/ubi8/ubi:8.6-990

Clone the repo from github:
>git clone https://github.com/sauluspaulus/PythonPipTestRepo

Build the image:
>sudo podman build -t [name] .

Run the Image
>sudo podman run [name] -p 80:8080


___________________
Openshift GUI:

As Developer click on "+Add" on the sidebar
Select "From Git"

under Git Repo URL paste: https://github.com/sauluspaulus/PythonPipTestRepo
as Builder Image select Python
Choose a Name
Select "Create a route to the Application
and under Advanced options choose a Target port e.g. 8080
click on "Create"
