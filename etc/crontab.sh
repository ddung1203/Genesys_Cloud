#! /usr/bin/bash

run() {
  (crontab -l 2>/dev/null; echo "0 15 * * 1-5 /home/vagrant/call_list_update.py") | crontab -
}