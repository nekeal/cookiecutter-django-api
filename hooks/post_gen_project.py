import os


def remove_drf_files():
    os.remove(
        os.path.join("{{cookiecutter.project_name}}", "accounts", "serializers.py")
    )


def remove_celery_files():
    os.remove(os.path.join("{{cookiecutter.project_name}}", "celery.py"))


def remove_jazzmin_files():
    os.remove(
        os.path.join("{{cookiecutter.project_name}}", "settings", "conf", "theme.py")
    )


def main():
    if "{{ cookiecutter.use_drf }}".lower() == "n":
        remove_drf_files()

    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery_files()

    if "{{ cookiecutter.use_jazzmin }}".lower() == "n":
        remove_jazzmin_files()


if __name__ == "__main__":
    main()
