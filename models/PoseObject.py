from .Pose import Pose

class PoseObject:

    def __init__(self, image_object_path: str):
        image_elements = image_object_path.split("-")

        self.name: str = image_elements[0]
        self.bin_name: str = image_elements[2]
        self.clutter: int = int(image_elements[3])
        self.position: int = int(image_elements[4])
        self.frame_number: int = int(image_elements[5].split(".")[0])

        self.pose: Pose = Pose.from_OpenCV(self.get_pose())

    def get_image_property(self, property: str, ext: str = "png"):
        return f"{self.name}-{property}-{self.bin_name}-{self.clutter}-{self.position}-{self.frame_number}.{ext}"

    def get_image(self):
        return self.get_image_property("image")

    def get_mask(self):
        return self.get_image_property("mask")

    def get_depth(self):
        return self.get_image_property("depth")

    def get_pose(self):
        return self.get_image_property("pose", "yml")