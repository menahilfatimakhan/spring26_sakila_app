# ============================================================
# config.py
# Authors: Menahil Fatima & Ali Hassan
# Description: Application config with timeout and health checks
# ============================================================
import os

# Combined database settings
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

# Combined custom features from both branches
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))