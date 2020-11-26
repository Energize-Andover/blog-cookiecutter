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
    try:
        print(f"Post-generate hook 1/3: git init")
        run_and_output(["git", "init"])

        print(f"Post-generate hook 2/3: bundle update")
        run_and_output(["bundle", "update"])

        print(f"Post-generate hook 3/3: bundle install")
        run_and_output(["bundle", "install"])
    except FileNotFoundError:
        raise SystemExit(f"{RED}Requirement not met. Stopping.{RESET}")
    except subprocess.CalledProcessError:
        raise SystemExit(f"{RED}Post-generate hook failed. Stopping.{RESET}")

    print("Successfully ran post-generate hooks.")


if __name__ == "__main__":
    main()
