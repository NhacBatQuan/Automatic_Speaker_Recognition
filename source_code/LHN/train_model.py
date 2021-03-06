import glob
import sys
sys.path.append('../') # To import all python files in `source_code` folder.
from mfcc_gmm_func import * # To import functions that you need


audio_file_path_list = []
for wav in glob.glob("*.wav"):
    audio_file_path_list.append(wav)

model_path = 'LHN.gmm'
generate_GMM(audio_file_path_list, model_path)

for audio_file_path in audio_file_path_list:
    print(try_personal_GMM(audio_file_path, model_path))
