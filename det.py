import roman_imsim
import sys

params = sys.argv[1]
visit = int(sys.argv[2])
sca = int(sys.argv[3])
dither_from_file = sys.argv[4]

if len(sys.argv)>5:
    sca_path = sys.argv[5]
else:
    sca_path = None

roman_imsim.detector_physics.modify_image(params,visit,sca,dither_from_file,sca_filepath=sca_path)
