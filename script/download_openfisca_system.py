import os
from subprocess import check_output
from pip._internal.utils.misc import get_installed_distributions


def download_and_install(path_to_save, project_name, github_link):
    current_path = os.getcwd()
    full_path = str(path_to_save + "\\"+ project_name)
    try:
        if os.path.exists(full_path):
            os.remove((full_path))
        os.chdir(str(path_to_save))
        check_output("git clone " + github_link, shell=True).decode()

        check_output("python -m pip install --upgrade pip", shell=True).decode()

        os.chdir(full_path)

        if project_name == 'openfisca-italy':
            check_output("git checkout Initizialize_open-fisca-italy", shell=True).decode()
        full_path = "\""+full_path+"\""
        check_output("pip install --editable " + full_path, shell=True).decode()
        os.chdir(current_path)
        return True
    except Exception as e:
        print e
        os.chdir(current_path)
        return False

def check_package_is_installed(country_package_name):
    installed_packages = sorted(["%s==%s" % (i.key, i.version) for i in get_installed_distributions()])
    print(installed_packages)
    for pack in installed_packages:
        if country_package_name in pack:
            return True
    return False # if the country package was not detected


def install_country_package(country_package_name, full_path):
    actual_path = os.getcwd()
    check_output("python -m pip install --upgrade pip", shell=True).decode()
    os.chdir(full_path)
    if country_package_name == 'openfisca-italy':
        check_output("git checkout Initizialize_open-fisca-italy", shell=True).decode()
    full_path = "\"" + full_path + "\""
    check_output("pip install --editable " + full_path, shell=True).decode()
    os.chdir((actual_path))
    return True