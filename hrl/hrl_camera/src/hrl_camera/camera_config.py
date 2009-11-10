import roslib
roslib.load_manifest('hrl_camera')
import cv

camera_parameters = {
        #A sample configuration
        'default' :
        {
            'calibration_image_width' : 320.0,
            'calibration_image_height' : 240.0, 
            'focal_length_x_in_pixels' : 161.80593,
            'focal_length_y_in_pixels' : 163.49099,
            'optical_center_x_in_pixels' : 159.78997,
            'optical_center_y_in_pixels' : 136.73113,
            'lens_distortion_radial_1' : -0.26334,
            'lens_distortion_radial_2' : 0.05096,
            'lens_distortion_tangential_1' : 0.00105,
            'lens_distortion_tangential_2' : -0.00016,
            'opencv_bayer_pattern' : None,
            'color': False,
            #the class to load in a normal python import statement
            'class': 'firefly',
            #UUID obtained by calling 'python camera_uuid.py'
            'uid': None 
            },

#########################################################################
# Start of camera on ELE
#########################################################################
        'catadioptric' :
        {  
            'calibration_image_width' : 640.0,
            'calibration_image_height' : 480.0, 
            'focal_length_x_in_pixels' : 360,
            'focal_length_y_in_pixels' : 360,
            'optical_center_x_in_pixels' : 320,
            'optical_center_y_in_pixels' : 240,
            'lens_distortion_radial_1' :    0,
            'lens_distortion_radial_2' :    0,
            'lens_distortion_tangential_1' : 0,
            'lens_distortion_tangential_2' : 0,
            'opencv_bayer_pattern' : None,
            'type': 'Point Grey Firefly',
            'class': 'firefly',
            'color': False,
            'uid': 7281154
        },

        'stereo_left':
        {  
            'calibration_image_width' : 640.0,
            'calibration_image_height' : 480.0, 
            'focal_length_x_in_pixels' : 1017.33,
            'focal_length_y_in_pixels' : 1018.47,
            'optical_center_x_in_pixels' : 306.264,
            'optical_center_y_in_pixels' : 226.465,
            'lens_distortion_radial_1' :    -0.480961,
            'lens_distortion_radial_2' :     0.341886,
            'lens_distortion_tangential_1' : 0,
            'lens_distortion_tangential_2' : 0,
            'opencv_bayer_pattern' : cv.CV_BayerGR2BGR,
            'type': 'Point Grey Firefly',
            'class': 'firefly',
            'color': True,
            'uid': 7140923
        },

        'stereo_right':
        {  
            'calibration_image_width' : 640.0,
            'calibration_image_height' : 480.0, 
            'focal_length_x_in_pixels' : 1013.70,
            'focal_length_y_in_pixels' : 1015.33,
            'optical_center_x_in_pixels' : 303.834,
            'optical_center_y_in_pixels' : 219.792,
            'lens_distortion_radial_1' :   -0.530238,
            'lens_distortion_radial_2' :   0.766580,
            'lens_distortion_tangential_1' : 0,
            'lens_distortion_tangential_2' : 0,
            'opencv_bayer_pattern' : cv.CV_BayerGR2BGR,
            'type': 'Point Grey Firefly',
            'class': 'firefly',
            'color': True,
            'uid': 7041054
        },

        'snozzberry_hand' :
        {
            'calibration_image_width' : 640.0,
            'calibration_image_height' : 480.0, 
            'focal_length_x_in_pixels' : 351.38 ,
            'focal_length_y_in_pixels' : 351.01, 
            'optical_center_x_in_pixels' : 301.92,
            'optical_center_y_in_pixels' : 203.98,
            'lens_distortion_radial_1' :   -0.258504,
            'lens_distortion_radial_2' : 0.0482161,
            'lens_distortion_tangential_1' : 0.0,
            'lens_distortion_tangential_2' : 0.0,
            'opencv_bayer_pattern' : cv.CV_BayerGR2BGR,
            'color': True,
            'type': 'Point Grey Firefly',
            'class': 'firefly',
            'uid': 7140879,
            'fovy': 62.
        },

        'ele_carriage' :
        {
            'calibration_image_width' : 1024.0,
            'calibration_image_height' : 768.0, 
            'focal_length_x_in_pixels' : 636.88281,
            'focal_length_y_in_pixels' : 634.47177,
            'optical_center_x_in_pixels' : 522.02156 ,
            'optical_center_y_in_pixels' : 330.15335 ,
            'lens_distortion_radial_1' :  -0.2752,
            'lens_distortion_radial_2' :  0.05637,
            'lens_distortion_tangential_1' : 0,
            'lens_distortion_tangential_2' : 0,
            'opencv_bayer_pattern' : cv.CV_BayerGR2RGB,
            'cv_cap_prop_mode' : 101,
            'upside_down': True,
            'color': True,
            'type': 'Point Grey DragonFly2',
            'class': 'dragonfly2',
            'uid': 9030523
        }

#########################################################################
# End of cameras on ELE.
#########################################################################
    }
