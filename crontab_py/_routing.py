import os

PKG_ROOT = os.path.dirname(os.path.abspath(__file__))
PKG_NAME = os.path.basename(PKG_ROOT)
PKG_APP_ROOT = os.path.dirname(os.path.abspath(PKG_ROOT))

PATH_GENERATE_ENV = os.path.join(PKG_ROOT,"utils", "env_generator.sh")



