import sys
import json
import mimetypes
import os
import ntpath

import helper


try:
  if __name__ != '__main__':
    print "not allow"
    sys.exit()


  current_file = os.path.realpath(__file__)
  current_path = os.path.dirname(current_file)
  
  os.chdir(current_path)

  print sys.argv
  if len(sys.argv) != 3:
    print "wrong argv python download_newest.py config_file_path save_file_path"
    sys.exit()

  config_file_path = sys.argv[1]
  save_file_path = sys.argv[2]

  if os.path.isfile(config_file_path) is False:
    print "not found config file: "+config_file_path
    sys.exit()

  if os.path.isdir(save_file_path) is False:
    print "not found save directory: " + save_file_path
    sys.exit()
  
  config_file = open(config_file_path, 'r')
  config = json.loads(config_file.read())

  
  drive_service = helper.createDriveService(config)
  print helper.coloured_output("Authentication is sucessful" , 'green')
  print helper.print_about( drive_service )
  print helper.coloured_output("Getting files information from your google drive" , 'yellow')

  children_files = helper.retrieve_all_files( drive_service, config['backup_folder_id'] )
  if len(children_files) == 0:
    print helper.coloured_output("There is no file in folder" , 'red')
    sys.exit()
  
  print helper.coloured_output("Getting newest file" , 'yellow')
  import operator
  children_files.sort(key=operator.itemgetter('modifiedDate'))
  newest_file = children_files[len(children_files) - 1]

  print helper.coloured_output("Downloading newest file" , 'yellow')
  print save_file_path
  helper.download_file(drive_service, newest_file, save_file_path)
  
  print helper.coloured_output("Save newest file done" , 'green')
except Exception, e:
  print "error"
  print e
finally:
  pass

