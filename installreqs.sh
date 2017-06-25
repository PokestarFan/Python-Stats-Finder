MKDIR InstallLogs
python -m pip install --upgrade --force --disable-pip-version-check --log ".\InstallLogs\pip.log" --requirement requirements.txt
