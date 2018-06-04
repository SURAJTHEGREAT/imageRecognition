import os
from RecognizeFace2Classify.parameterFile import Classify
from RecognizeFace2Classify.osOperations import Decorate
from RecognizeFace2Classify.logger import create_logger
from RecognizeFace2Classify.facialOperations import Facial
# GENERATE THE LOG PATH FROM CURRENT FILE NAME
LOG = create_logger(os.path.splitext(os.path.basename(__file__))[0])


class Recognize2Classify:

    def __init__(self):
        self.param = Classify()
        self.os_param = Decorate()
        self.facial_param = Facial()
    def __call__(self, *args, **kwargs):
        self.param(self, *args, **kwargs)
        results_dir="results"
        self.unclassified_images_path, self.individuals_images_path = self.param.get_parameter()
        self.unclassified_images_list, self.individuals_images_list= self.os_param.list_directory(self.unclassified_images_path),self.os_param.list_directory(self.individuals_images_path)
        if self.individuals_images_list or self.individuals_images_list is None:
            raise SystemExit("program exited as directory is empty")

        individuals_name=self.facial_param.create_name_array(self.individuals_images_list)
        self.facial_param.create_encoding(self.individuals_images_list,self.individuals_images_path)
        person_picture_collection=self.facial_param.create_facial_classify(self.facial_param,self.unclassified_images_list,self.unclassified_images_path)
        self.os_param.make_directory(self,results_dir)
        self.os_param.copy_images(self, individuals_name, results_dir, person_picture_collection)
    def debug(self):
        LOG.info("The unclassified images path is")
        LOG.info(self.unclassified_images_path)
        LOG.info("The individuals images path is")
        LOG.info(self.individuals_images_path)
        LOG.info("The unclassified images list is")
        LOG.info(self.unclassified_images_list)
        LOG.info("The individual images list is")
        LOG.info(self.individuals_images_list)




