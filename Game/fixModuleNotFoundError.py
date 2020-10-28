#code to solve module not found error.....from https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x

import os, sys
current_path = os.path.abspath('.')
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'child.settings')
