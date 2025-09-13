import platform
import shutil
import subprocess
import os
import uuid
import docker
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Detect OS type (for future package installations)
def get_os_family():
    if os.path.exists("/etc/debian_version"):
        return "debian"
    elif os.path.exists("/etc/redhat-release"):
        return "redhat"
    else:
        return "unknown"

# Install missing package
def install_package(tool, os_family):
    try:
        if os_family == "debian":
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
        elif os_family == "redhat":
            subprocess.run(["sudo", "yum", "install", "-y", tool], check=True)
        return True, None
    except Exception as e:
        return False, str(e)

# Check if Portainer is actually installed and running (or exists as a container)
def is_portainer_installed():
    try:
        result = subprocess.run(
            ["docker", "inspect", "-f", "{{.State.Running}}", "portainer"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result.stdout.strip() in ["true", "false"]
    except Exception:
        return False

# Actually run Portainer
def run_portainer():
    try:
        subprocess.run(["docker", "volume", "create", "portainer_data"], check=True)
        subprocess.run([
            "docker", "run", "-d",
            "-p", "9443:9443", "-p", "9000:9000",
            "--name", "portainer",
            "--restart=always",
            "-v", "/var/run/docker.sock:/var/run/docker.sock",
            "-v", "portainer_data:/data",
            "portainer/portainer-ce:latest"
        ], check=True)
        return True, "✅ Portainer installed successfully."
    except subprocess.CalledProcessError as e:
        return False, f"❌ Docker Error: {str(e)}"

# Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/install_portainer", methods=["GET", "POST"])
def install_portainer_route():
    installed = is_portainer_installed()
    portainer_url = "https://localhost:9443"
    message = None

    if request.method == "POST":
        if not installed:
            success, message = run_portainer()
            installed = success
        else:
            message = "ℹ️ Portainer is already installed."

    return render_template("portainer.html", installed=installed, message=message, url=portainer_url)

@app.route("/pre-req")
def prereq():
    tools = ["pip3", "podman", "openssl", "docker"]
    results = {}
    os_family = get_os_family()

    for tool in tools:
        if shutil.which(tool):
            results[tool] = "✅ Installed"
        else:
            success, error = install_package(tool, os_family)
            if success:
                results[tool] = "❌ Not Found → 🛠️ Installed"
            else:
                results[tool] = f"❌ Not Found → ❌ Error: {error}"
    docker_installed = shutil.which("docker") is not None
    return render_template("prereq.html", results=results, os_family=os_family, docker_installed=docker_installed)


##################PYTHON INSTALLATION##################

@app.route("/python")
def python_info():
    return render_template("python_info.html")


###########################################################

@app.route("/python/local")
def python_local():
    try:
        # Check if Python is already installed
        try:
            python_version = subprocess.check_output(["python3", "--version"], stderr=subprocess.STDOUT).decode()
            return render_template("python_local.html", result=f"✅ Python is already installed:\n{python_version}")
        except subprocess.CalledProcessError:
            pass  # not installed yet
        except FileNotFoundError:
            pass  # python3 not found

        # Detect OS
        os_release = subprocess.check_output(["cat", "/etc/os-release"]).decode()
        if "debian" in os_release.lower() or "ubuntu" in os_release.lower():
            install_cmd = [
                ["sudo", "apt", "update"],
                ["sudo", "apt", "install", "-y", "python3", "python3-pip"]
            ]
            os_type = "Debian-based (APT)"
        elif "rhel" in os_release.lower() or "centos" in os_release.lower() or "fedora" in os_release.lower():
            install_cmd = [
                ["sudo", "yum", "install", "-y", "python3", "python3-pip"]
            ]
            os_type = "RHEL-based (YUM)"
        else:
            return render_template("python_local.html", result="❌ Unsupported OS for automatic installation.")

        output_logs = f"🔍 Detected OS: {os_type}\n"

        for cmd in install_cmd:
            process = subprocess.run(cmd, check=True, capture_output=True, text=True)
            output_logs += f"\n$ {' '.join(cmd)}\n{process.stdout}"

        python_version = subprocess.check_output(["python3", "--version"]).decode()
        pip_version = subprocess.check_output(["pip3", "--version"]).decode()
        output_logs += f"\n✅ Python Installed Successfully:\n{python_version}\n{pip_version}"

    except subprocess.CalledProcessError as e:
        output_logs = f"❌ Error during installation:\n{e}\n\n{e.stderr if hasattr(e, 'stderr') else ''}"
    except Exception as ex:
        output_logs = f"⚠️ Unexpected error: {str(ex)}"

    return render_template("python_local.html", result=output_logs)
##################PYTHON INSTALLATION END##################
@app.route("/python/virtualenv")
def python_virtualenv():
    return render_template("python_virtualenv.html")
#########################   ansible execution environment########################

######################################## playbooks #################################################



PLAYBOOKS_DIR = "./playbooks"
INVENTORY_FILE = os.path.join(PLAYBOOKS_DIR, "./../inventory.ini")

@app.route('/ansible/local/playbooks', methods=['GET', 'POST'])
def ansible_local_playbooks():
    # Playbook run
    if request.method == 'POST':
        selected_playbook = request.form.get('playbook')
        if selected_playbook:
            playbook_path = os.path.join(PLAYBOOKS_DIR, selected_playbook)
            try:
                result = subprocess.run(
                    ['ansible-playbook', '-i', INVENTORY_FILE, playbook_path],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                return render_template("playbook_output.html", output=result.stdout)
            except subprocess.CalledProcessError as e:
                return render_template("playbook_output.html", output=e.stdout)

    # List playbooks
    playbooks = [f for f in os.listdir(PLAYBOOKS_DIR)
                 if f.endswith(('.yml', '.yaml')) and os.path.isfile(os.path.join(PLAYBOOKS_DIR, f))]
    
    return render_template('playbooks_list.html', playbooks=playbooks)


from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import subprocess

@app.route('/ansible/local/playbooks/view/<playbook_name>')
def view_playbook(playbook_name):
    safe_name = secure_filename(playbook_name)
    playbook_path = os.path.join(PLAYBOOKS_DIR, safe_name)

    if not os.path.exists(playbook_path):
        return f"<pre>Playbook not found: {safe_name}</pre>"

    try:
        with open(playbook_path, 'r') as f:
            content = f.read()
        return render_template('playbook_view.html', playbook_name=safe_name, content=content)
    except Exception as e:
        return f"<pre>Could not read playbook: {e}</pre>"



######################################## playbooks end  #################################################

@app.route("/python/tutorials")
def python_tutorials():
    tabs = ["Basics", "Intermediate", "Advanced", "Expert", "Flask"]
    return render_template("python_tutorials.html", tabs=tabs)

# Map levels to folders
FOLDER_MAP = {
    "Basics": "basic",
    "Intermediate": "intermediate",
    "Advanced": "advanced",
    "Expert": "expert",
    "Flask": "flask"
}

# Route: list scripts for a level
@app.route("/python/tutorials/<level>")
def list_scripts(level):
    folder = FOLDER_MAP.get(level)
    if not folder or not os.path.isdir(folder):
        return f"❌ Invalid level: {level}"

    # List all Python scripts
    scripts = [f for f in os.listdir(folder) if f.endswith(".py")]
    return render_template("python_scripts_list.html", level=level, scripts=scripts)

# Route: show script content and run option
@app.route("/python/tutorials/<level>/script/<script_name>", methods=["GET", "POST"])
def show_and_run_script(level, script_name):
    folder = FOLDER_MAP.get(level)
    if not folder:
        return f"❌ Invalid level: {level}"

    script_path = os.path.join(folder, script_name)
    if not os.path.isfile(script_path):
        return f"❌ Script not found: {script_name}"

    # Read script content
    with open(script_path, "r") as f:
        code = f.read()

    output = None
    if request.method == "POST":
        try:
            # Run the script
            output = subprocess.check_output(["python3", script_path], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = f"❌ Error:\n{e.output}"

    return render_template("python_script_run.html", level=level, script_name=script_name, code=code, output=output)


######################### advanced playbook start #####################################################



ADVANCED_PLAYBOOKS_DIR = "./advanced-playbooks"
ADV_PLAYBOOK_FILE = os.path.join(ADVANCED_PLAYBOOKS_DIR, "playbook.yml")
ADV_INVENTORY_FILE = os.path.join(ADVANCED_PLAYBOOKS_DIR, "./../inventory.ini")
ADV_OUTPUT_FILE = os.path.join(ADVANCED_PLAYBOOKS_DIR, "advanced_playbook_output.yml")
ADV_README_FILE = os.path.join(ADVANCED_PLAYBOOKS_DIR, "README.md")


def get_directory_tree(path):
    tree = ""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = "│   " * level + "├── "
        tree += f"{indent}{os.path.basename(root)}/\n"
        subindent = "│   " * (level + 1) + "├── "
        for f in files:
            tree += f"{subindent}{f}\n"
    return tree


@app.route('/ansible/local/playbooks/advanced-playbooks', methods=['GET', 'POST'])
def view_advanced_playbook():
    output = None
    dir_tree = None
    readme = None

    if request.method == 'POST':
        if 'run_playbook' in request.form:
            try:
                result = subprocess.run(
                    ['ansible-playbook', '-i', ADV_INVENTORY_FILE, ADV_PLAYBOOK_FILE],
                   
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    check=True
                )
                with open(ADV_OUTPUT_FILE, 'w') as f:
                    f.write(result.stdout)
                output = result.stdout
            except subprocess.CalledProcessError as e:
                output = e.stdout

        elif 'show_tree' in request.form:
            dir_tree = get_directory_tree(ADVANCED_PLAYBOOKS_DIR)

        elif 'show_readme' in request.form and os.path.exists(ADV_README_FILE):
            with open(ADV_README_FILE, 'r') as f:
                readme = f.read()

    return render_template(
        'advanced_playbook_output.html',
        dir_tree=dir_tree,
        readme=readme,
        output=output
    )

######################### advanced playbook end #####################################################

#####################################################################################################
#ansible roles start


ROLES_DIR = "./roles"
INVENTORY_FILE = "./inventory.ini"
ROLE_PLAYBOOK_FILE = "./roles/role_playbook.yml"

def get_directory_tree(path):
    tree = ""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = "│   " * level + "├── "
        tree += f"{indent}{os.path.basename(root)}/\n"
        subindent = "│   " * (level + 1) + "├── "
        for f in files:
            tree += f"{subindent}{f}\n"
    return tree

@app.route('/ansible/local/playbooks/roles', methods=['GET', 'POST'])
def manage_roles():
    message = None
    output = None
    dir_tree = None
    readme = None

    if request.method == 'POST':
        if 'create_role' in request.form:
            role_name = request.form.get('role_name')
            if role_name:
                subprocess.run(['ansible-galaxy', 'init', os.path.join(ROLES_DIR, role_name)])
                message = f"✅ Role '{role_name}' created."
            else:
                message = "⚠️ Role name required."

        elif 'install_role' in request.form:
            role_name = request.form.get('role_name')
            if role_name:
                subprocess.run(['ansible-galaxy', 'install', role_name, '-p', ROLES_DIR])
                message = f"✅ Role '{role_name}' installed from Galaxy."
            else:
                message = "⚠️ Role name required."

        elif 'show_tree' in request.form:
            dir_tree = get_directory_tree(ROLES_DIR)

        elif 'show_readme' in request.form:
            role_name = request.form.get('role_name')
            readme_path = os.path.join(ROLES_DIR, role_name, 'README.md')
            if os.path.exists(readme_path):
                with open(readme_path) as f:
                    readme = f.read()
            else:
                readme = "README.md not found."

        elif 'run_role' in request.form:
            role_name = request.form.get('role_name')
            if role_name:
                # Create a temporary playbook using the role
                with open(ROLE_PLAYBOOK_FILE, 'w') as f:
                    f.write(f"""---
- hosts: all
  become: true
  roles:
    - {role_name}
""")
                try:
                    result = subprocess.run(
                        ['ansible-playbook', '-i', INVENTORY_FILE, ROLE_PLAYBOOK_FILE],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        text=True,
                        check=True
                    )
                    output = result.stdout
                except subprocess.CalledProcessError as e:
                    output = e.stdout
            else:
                message = "⚠️ Role name required to run playbook."

    return render_template(
        'role_manager.html',
        message=message,
        dir_tree=dir_tree,
        readme=readme,
        output=output
    )


################################### ansible role end #############################################################

########################## Ansible Tower ##########################################################


@app.route('/ansible/local/tower', methods=['GET', 'POST'])
def ansible_tower():
    output = None
    install_requested = False
    awx_cloned = os.path.exists('./awx')

    if request.method == 'POST':
        install_requested = True

        try:
            distro = platform.freedesktop_os_release().get("ID", "").lower()
            
            # 1. Install Docker if not present
            docker_check = subprocess.run(['which', 'docker'], stdout=subprocess.PIPE, text=True)
            if not docker_check.stdout.strip():
                if "ubuntu" in distro or "debian" in distro:
                    subprocess.run(['sudo', 'apt', 'update'])
                    subprocess.run(['sudo', 'apt', 'install', '-y', 'docker.io'])
                elif "centos" in distro or "rhel" in distro or "rocky" in distro or "fedora" in distro:
                    subprocess.run(['sudo', 'yum', 'install', '-y', 'docker'])
                else:
                    raise Exception(f"Unsupported distro: {distro}. Please install Docker manually.")

            # 2. Install docker-compose if not present
            compose_check = subprocess.run(['which', 'docker-compose'], stdout=subprocess.PIPE, text=True)
            if not compose_check.stdout.strip():
                subprocess.run([
                    'sudo', 'curl', '-SL',
                    'https://github.com/docker/compose/releases/download/v2.32.0/docker-compose-linux-x86_64',
                    '-o', '/usr/local/bin/docker-compose'
                ])
                subprocess.run(['sudo', 'chmod', '+x', '/usr/local/bin/docker-compose'])
                subprocess.run(['sudo', 'ln', '-sf', '/usr/local/bin/docker-compose', '/usr/bin/docker-compose'])

            # 3. Clone AWX repo and setup
            if not awx_cloned:
                subprocess.run(['git', 'clone', 'https://github.com/ansible/awx.git'])
                os.chdir('./awx')               
                os.chdir('./tools/docker-compose')
                subprocess.run(['cp', '.env.example', '.env'])

            # 4. Start AWX via docker-compose
            os.chdir('./awx/tools/docker-compose')
            subprocess.run(['docker-compose', 'up', '-d'])

            output = "✅ AWX (Ansible Tower) installed and started successfully!"
        except Exception as e:
            output = f"❌ Error during AWX setup: {str(e)}"

    return render_template(
        'ansible_tower.html',
        output=output,
        install_requested=install_requested
    )


########################## Ansible Tower  end ##########################################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6006, debug=True)
