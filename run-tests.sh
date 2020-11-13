#!/bin/bash

set -o errexit
set -o nounset

check_script () {
    shellcheck run-tests.sh utils/*.sh
}

check_pycodestyle () {
    pycodestyle utils/*.py
}

check_pydocstyle () {
    pydocstyle utils/*.py
}

check_all () {
    check_script
    check_pycodestyle
    check_pydocstyle
}

if [ $# -eq 0 ]; then
    check_all
    exit 0
fi

for arg in "$@"
do
    case $arg in
        --check-shellscript) check_script;;
        --check-pycodestyle) check_pycodestyle;;
        --check-pydocstyle) check_pydocstyle;;
        *)
    esac
done
