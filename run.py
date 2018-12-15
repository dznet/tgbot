#!/usr/bin/env python3
from config import Development
from api import create_api

api = create_api(Development)

if __name__ == '__main__':
  api.run(host=api.config['SERVER_HOST'],
          port=api.config['SERVER_PORT'])
