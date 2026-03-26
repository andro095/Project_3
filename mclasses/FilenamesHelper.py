import os.path

# from .PoseObject import PoseObject

DATA_DIR = "./data"
OBJ_MOD_DIR = "Object Models"
# Test
# IMAGES_DIR = "Sample Images"
# Final Dataset
IMAGES_DIR = "Full Dataset"
RUN_DIR = "run_"
CAMERA_CALIB_FILE = "camera_calibrations.yml"
GRAPHS_DIR = "Graph Result"

class FilenamesHelper:

    # Directory paths methods
    @staticmethod
    def get_obj_dir():
        return os.path.join(DATA_DIR, OBJ_MOD_DIR)

    # @staticmethod
    # def get_images_dir(run_number: int):
    #     # return os.path.join(DATA_DIR, IMAGES_DIR, RUN_DIR + str(run_number))
    #     return os.path.join(DATA_DIR, IMAGES_DIR)

    @staticmethod
    def get_images_dir():
        return os.path.join(DATA_DIR, IMAGES_DIR)

    @staticmethod
    def get_graphs_dir():
        return os.path.join(DATA_DIR, GRAPHS_DIR)

    # Object file paths methods
    @staticmethod
    def get_obj_file_path(obj):
        return os.path.join(FilenamesHelper.get_obj_dir(), obj.get_obj())

    @staticmethod
    def get_mtl_file_path(obj):
        return os.path.join(FilenamesHelper.get_obj_dir(), obj.get_mtl())

    @staticmethod
    def get_texture_file_path(obj):
        return os.path.join(FilenamesHelper.get_obj_dir(), obj.get_texture())

    @staticmethod
    def get_stl_file_path(obj):
        return os.path.join(FilenamesHelper.get_obj_dir(), obj.get_stl())

    # Image file paths methods
    @staticmethod
    def get_image_path(run_number: int, file_name: str):
        return os.path.join(FilenamesHelper.get_images_dir(), file_name)

    @staticmethod
    def get_image_file_path(obj):
        return FilenamesHelper.get_image_path(obj.run_number, obj.get_image())

    @staticmethod
    def get_mask_file_path(obj):
        return FilenamesHelper.get_image_path(obj.run_number, obj.get_mask())

    @staticmethod
    def get_depth_file_path(obj):
        return FilenamesHelper.get_image_path(obj.run_number, obj.get_depth())

    @staticmethod
    def get_pose_file_path(obj):
        return FilenamesHelper.get_image_path(obj.run_number, obj.get_pose())

    # Camera file paths methods
    @staticmethod
    def get_camera_calibrations_file_path():
        return os.path.join(DATA_DIR, CAMERA_CALIB_FILE)

    @staticmethod
    def get_graph_file_path(obj_name: str):
        return os.path.join(FilenamesHelper.get_graphs_dir(), f"{obj_name}.png")