from __future__ import absolute_import
import os
import shutil
from RecognizeFace2Classify.logger import create_logger

__author__ = 'suraj'


# GENERATE THE LOG PATH FROM CURRENT FILE NAME
LOG=create_logger(os.path.splitext(os.path.basename(__file__))[0])


class Decorate:
    home_path = os.path.expanduser("~")

    def __init__(self):
        pass

    def construct_default_path(self,parameter):
        default_path=self.home_path+'/'+parameter
        return default_path

    def make_directory(self,results_dir):
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        else:
            shutil.rmtree(results_dir)
            os.makedirs(results_dir)

    def list_directory(self,dir):
        try:
            os.listdir(dir)
        except Exception as e:
            LOG.info("The exception error is")
            LOG.info(e)
            raise SystemExit(e)

    def copy_images(self,individuals_name,results_dir,person_picture_collection):
        for person in individuals_name:
            dest = results_dir + "/" + person
            os.makedirs(results_dir + "/" + person)
            for picture in person_picture_collection[person]:
                shutil.copy(picture, dest)




