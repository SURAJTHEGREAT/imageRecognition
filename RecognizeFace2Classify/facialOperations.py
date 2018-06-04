from __future__ import absolute_import
import os
from collections import defaultdict
import face_recognition
import cv2

from RecognizeFace2Classify.logger import create_logger
__author__ = 'suraj'

# GENERATE THE LOG PATH FROM CURRENT FILE NAME
LOG = create_logger(os.path.splitext(os.path.basename(__file__))[0])


class Facial:
    individuals_name = []
    individuals_face_encodings = []


    def create_name_array(self,individuals_images_list):
        for person in individuals_images_list:
            self.individuals_name.append(person[:-4])
            return self.individuals_name


    def create_encoding(self,individuals_images_list,individuals_images_path):
        try:
            for individuals in individuals_images_list:
                image = face_recognition.load_image_file(individuals_images_path + "/" + individuals)
                face_encoding = face_recognition.face_encodings(image)[0]
                self.individuals_face_encodings.append(face_encoding)

        except Exception as e:
            print("Error: [" + e.errno + "] " + e.strerr)
            LOG.info("The error is")
            LOG.info(e)

    @classmethod
    def create_facial_classify(cls,unclassified_images_list,unclassified_images_path):

        person_picture_collection = defaultdict(lambda: list())

        for images in unclassified_images_list:
            frame = cv2.imread(unclassified_images_path + "/" + images)
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                name = "unknown"
                for index in range(len(cls.individuals_face_encodings)):
                    face_distance = face_recognition.face_distance([cls.individuals_face_encodings[index]], face_encoding)
                    if face_distance < 0.5:
                        name=cls.individuals_name[index]
                person_picture_collection[name].append(unclassified_images_path + "/" + images)
        return person_picture_collection





