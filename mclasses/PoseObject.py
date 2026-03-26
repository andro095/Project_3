from .Pose import Pose
from .FilenamesHelper import FilenamesHelper

class PoseObject:

    def __init__(self, image_object_filename: str, run_number: int = 1):
        image_file_name = image_object_filename.split(".")[0]
        image_elements = image_file_name.split("-")

        self.name: str = image_elements[0]
        self.bin_name: str = image_elements[2]
        self.clutter: int = int(image_elements[3])
        self.position: int = int(image_elements[4])
        self.frame_number: int = int(image_elements[5])

        self.run_number: int = run_number

        self.pose: Pose = Pose.from_OpenCV(FilenamesHelper.get_pose_file_path(self))

    def get_image_property(self, property: str, ext: str = "png"):
        return f"{self.name}-{property}-{self.bin_name}-{self.clutter}-{self.position}-{self.frame_number}.{ext}"

    def get_obj_property(self, ext: str = "obj"):
        return f"{self.name}.{ext}"

    def get_image(self):
        return self.get_image_property("image")

    def get_mask(self):
        return self.get_image_property("mask")

    def get_depth(self):
        return self.get_image_property("depth")

    def get_pose(self):
        return self.get_image_property("pose", "yml")

    def get_obj(self):
        return self.get_obj_property()

    def get_mtl(self):
        return self.get_obj_property("obj.mtl")

    def get_texture(self):
        return self.get_obj_property("png")

    def get_stl(self):
        return self.get_obj_property("stl")