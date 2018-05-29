import os
from RecognizeFace2Classify.parameterFile import Classify
from RecognizeFace2Classify.osOperations import Decorate
from RecognizeFace2Classify.logger import create_logger

# GENERATE THE LOG PATH FROM CURRENT FILE NAME
LOG = create_logger(os.path.splitext(os.path.basename(__file__))[0])


class Recognize2Classify:

    def __init__(self):
        self.param = Classify()
        self.os_param = Decorate()

    def __call__(self, *args, **kwargs):
        self.param(self, *args, **kwargs)
        self.unclassified_images_path, self.individuals_images_path = self.param.get_parameter()
        self.unclassified_images_list, self.individuals_images_list= self.os_param.list_directory(self.unclassified_images_path),self.os_param.list_directory(self.individuals_images_path)
        if self.individuals_images_list or self.individuals_images_list is None:
            raise SystemExit("program exited as directory is empty")

    def debug(self):
        LOG.info("The unclassified images path is")
        LOG.info(self.unclassified_images_path)
        LOG.info("The individuals images path is")
        LOG.info(self.individuals_images_path)
        LOG.info("The unclassified images list is")
        LOG.info(self.unclassified_images_list)
        LOG.info("The individual images list is")
        LOG.info(self.individuals_images_list)


