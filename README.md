WordPress Site Management with Docker

This command-line script allows you to manage WordPress sites using Docker and Docker Compose. It sets up a LEMP stack in containers and creates, enables, disables, and deletes WordPress sites.

Requirements

Python (version 3.x)
Docker

# Installation

# Clone this repository:

```<bash>

///git clone https://github.com/pathakravi1999/example.com
cd example.com

```

Install Python if you haven't already
Install Docker and Docker Compose if you haven't already


# Usage

Run the script using Python:

```<python>

///python src/main.py example.com [subcommand]

```


example.com: The name of the WordPress site. Replace example.com with your desired site name.
[subcommand]: The action you want to perform on the site. Available subcommands are:
install: Install Docker and Docker Compose (required before using other subcommands).
create: Create a new WordPress site.
enable: Enable the WordPress site (start containers).
disable: Disable the WordPress site (stop containers).
delete: Delete the WordPress site (remove containers and local files).

# Note: For subcommands create, enable, disable, and delete, Docker and Docker Compose must be installed.

Examples

Install Docker and Docker Compose:


```<bash>

///python src/main.py example.com install


```

Create a new WordPress site:


```<bash>

///python src/main.py example.com create


```

Enable the WordPress site:

```<bash>

///python src/main.py example.com enable


```

Disable the WordPress site:


```<bash>

///python src/main.py example.com disable


```

Delete the WordPress site:


```<bash>

///python src/main.py example.com delete


```

# Troubleshooting

If you encounter any issues during installation or while using the script, please check the following:

Ensure you have Python (version 3.x) installed on your system.
Make sure you have Docker and Docker Compose installed. Check their versions using the following commands:



```<bash>

///docker --version
docker-compose --version

```
If Docker is not installed, follow the links provided in the "Installation" section to install Docker and Docker Compose.
If you encounter permission errors while using Docker or Docker Compose commands, you may need to run the script with sudo:


Thank you.
