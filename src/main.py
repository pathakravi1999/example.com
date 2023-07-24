import subprocess
import argparse
import os

def check_docker_installed():
    try:
        subprocess.run(["docker", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run(["docker-compose", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        return False
    return True

def install_docker():
    subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"], check=True)
    subprocess.run(["sudo", "sh", "get-docker.sh"], check=True)
    subprocess.run(["sudo", "usermod", "-aG", "docker", os.getlogin()], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)
    subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)
    subprocess.run(["sudo", "docker-compose", "up", "-d"], check=True)

def create_wordpress_site(site_name):
    with open("docker/nginx/nginx.conf", "r") as f:
        nginx_conf = f.read().replace("example.com", site_name)

    with open("docker/nginx/nginx.conf", "w") as f:
        f.write(nginx_conf)

def enable_site():
    subprocess.run(["sudo", "docker-compose", "start"], check=True)

def disable_site():
    subprocess.run(["sudo", "docker-compose", "stop"], check=True)

def delete_site():
    subprocess.run(["sudo", "docker-compose", "down", "--volumes"], check=True)

def main():
    parser = argparse.ArgumentParser(description="Manage WordPress sites using Docker")
    parser.add_argument("site_name", help="Name of the WordPress site")

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")
    subparsers.add_parser("install", help="Install Docker and Docker Compose")
    subparsers.add_parser("create", help="Create a WordPress site using the latest version")
    subparsers.add_parser("enable", help="Enable the WordPress site")
    subparsers.add_parser("disable", help="Disable the WordPress site")
    subparsers.add_parser("delete", help="Delete the WordPress site")

    args = parser.parse_args()

    if args.subcommand == "install":
        if not check_docker_installed():
            install_docker()
        else:
            print("Docker and Docker Compose are already installed.")
    elif args.subcommand == "create":
        if not check_docker_installed():
            print("Docker and Docker Compose are not installed. Please run 'python main.py install'")
            return

        create_wordpress_site(args.site_name)
        subprocess.run(["sudo", "docker-compose", "up", "-d"], check=True)
        print(f"WordPress site '{args.site_name}' is created and running at http://example.com")
    elif args.subcommand == "enable":
        enable_site()
        print("WordPress site is enabled.")
    elif args.subcommand == "disable":
        disable_site()
        print("WordPress site is disabled.")
    elif args.subcommand == "delete":
        delete_site()
        print("WordPress site is deleted.")

if __name__ == "__main__":
    main()
