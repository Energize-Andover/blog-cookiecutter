import subprocess
import sys

# Ansi color codes
RED = '\033[0;31m'
GRAY = '\033[0;37m'
RESET = '\033[0m'


def run_and_output(args) -> None:
    """
    Run a command and print its standard error.
    :param args: The arguments used to launch the process.
    This may be a list or a string.
    :return: nothing
    """
    result: subprocess.CompletedProcess = subprocess.run(
        args, capture_output=True, text=True
    )
    print(f"{GRAY}{result.stderr}{RESET}", file=sys.stderr)
    result.check_returncode()


def main():
    commands = [
        ["bundle", "install"],
        ["git", "init"],
        ["git", "add", "-A"],
        ["git", "commit", "-m", "Initial commit"]
    ]
    n = len(commands)

    print()
    try:
        for index, command in enumerate(commands):
            print(f"Post-generate hook {index+1}/{n}: {' '.join(command)}")
            run_and_output(command)
    except FileNotFoundError:
        raise SystemExit(f"{RED}Requirement not met. Stopping.{RESET}")
    except subprocess.CalledProcessError:
        raise SystemExit(f"{RED}Post-generate hook failed. Stopping.{RESET}")

    print("Successfully ran post-generate hooks.")


if __name__ == "__main__":
    main()
