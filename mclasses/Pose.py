
import numpy as np
import numpy.typing as npt
import cv2

class Pose:
    def __init__(self, rotation: npt.NDArray[np.float32], translation: npt.NDArray[np.float32]):
        self.rotation = rotation
        self.translation = translation

    @classmethod
    def from_OpenCV(cls, filename: str) -> 'Pose':
        fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_READ)

        rotation = fs.getNode("object_rotation_wrt_camera")

        translation = fs.getNode("object_translation_wrt_camera")

        rot = rotation.mat().reshape(3, 3)

        # Use list comprehension for cleaner and faster extraction
        trans_list = [translation.at(i).real() for i in range(translation.size())]
        trans = np.array(trans_list, dtype=np.float32).reshape(3, 1)

        fs.release()

        return cls(rot, trans)

    def to_homogeneous_matrix(self) -> np.ndarray:
        """
        Combines the 3x3 rotation and 3x1 translation into a single 4x4 matrix.
        """
        # 1. Create the base "container": a 4x4 Identity Matrix.
        # This gives us a matrix of zeros, but with a diagonal line of 1s.
        # This automatically sets up our bottom row as [0, 0, 0, 1]!
        H = np.eye(4, dtype=np.float32)

        # 2. Pack the Rotation: Paste the 3x3 matrix into the top-left corner
        H[0:3, 0:3] = self.rotation

        # 3. Pack the Translation: Paste the 3x1 vector into the top-right corner
        H[0:3, 3:4] = self.translation

        return H

    def __str__(self) -> str:
        return f"Pose:\n  Rotation:\n{self.rotation}\n  Translation:\n{self.translation}"