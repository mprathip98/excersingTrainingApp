
import numpy as np
import mediapipe as mp
 
mp_pose = mp.solutions.pose
SIDE = "LEFT"   # film the person's left side for now atleast
REP_LEN = 50    # frames for each rep
 

EXERCISES = {
    "squat": dict(
        features=[("angle", "HIP", "KNEE", "ANKLE"),
                  ("angle", "SHOULDER", "HIP", "KNEE"),
                  ("lean", "HIP", "SHOULDER")],
        top=160,
        cues={"good": "Great rep!",
              "shallow_depth": "Go deeper: aim for hips at knee level",
              "rounded_back": "Keep your chest up and back straight"},
    ),
    "pushup": dict(
        features=[("angle", "SHOULDER", "ELBOW", "WRIST"),
                  ("angle", "SHOULDER", "HIP", "ANKLE"),
                  ("lean", "HIP", "SHOULDER")],
        top=150,
        cues={"good": "Great rep!",
              "sagging_hips": "Squeeze your core, keep a straight line",
              "partial_range": "Lower your chest closer to the floor"},
    ),
    "curl": dict(
        features=[("angle", "SHOULDER", "ELBOW", "WRIST"),
                  ("lean", "ELBOW", "SHOULDER"),
                  ("lean", "HIP", "SHOULDER")],
        top=150,
        cues={"good": "Great rep!",
              "swinging": "Keep your elbow pinned, no swinging",
              "partial_range": "Use the full range of motion"},
    ),
}