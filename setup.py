from setuptools import setup, find_packages

setup(
    name="threat-intelligence-automation",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "pyyaml",
        "splunk-sdk",
        "suricata",
        "pytest"
    ],
    entry_points={
        'console_scripts': [
            'osint-collector=src.osint_collector:collect_data',
            'rule-updater=src.rule_updater:update_rules',
            'alert-manager=src.alert_manager:send_alert',
        ],
    },
)
