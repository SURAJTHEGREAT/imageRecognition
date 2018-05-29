from __future__ import absolute_import
import os
from RecognizeFace2Classify.osOperations import Decorate
from RecognizeFace2Classify.logger import create_logger

__author__ = 'suraj'

# GENERATE THE LOG PATH FROM CURRENT FILE NAME
LOG=create_logger(os.path.splitext(os.path.basename(__file__))[0])

class Classify:
    # Declare variables
    _unclassified = None
    _sample = None

    def __init__(self):

        # create object for Decorate class on initiate
        self.obj = Decorate()

    def __call__(self,*args,**kwargs):
        # On calling Classify object ,declare unclassified and sample
        LOG.info("The args is")
        LOG.info(args)
        LOG.info("The kwargs is")
        LOG.info(kwargs)
        try:

            temp_unclassified = kwargs.pop('unclassified',self.obj.construct_default_path('Pictures'))
            temp_sample = kwargs.pop('sample',self.obj.construct_default_path('Sample'))
            LOG.info("The kwargs after pop is")
            LOG.info(kwargs)
            if kwargs:
                LOG.info("The code will exit as extra parameters apart from unclassified and sample are provided")
                raise SystemExit("program exited as extra parameters apart from unclassified and sample are provided")
            else:
                self._unclassified=temp_unclassified
                self._sample=temp_sample



        except Exception as e:

            LOG.info("The error is")
            LOG.info(e)

    def get_parameter(self):

        if self._unclassified and self._sample is not None:
            LOG.info("The unclassified is")
            LOG.info(self._unclassified)
            LOG.info("The sample is")
            LOG.info(self._sample)

        else:
            LOG.info("The code will exit as method called before declaring")
            raise SystemExit("program exited as values are not declared yet")

        return self._unclassified, self._sample