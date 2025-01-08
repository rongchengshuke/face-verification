from a002_model.a001_utils.a003_logger import build_logger_with_handler

LOGGER = build_logger_with_handler()

DPI = 300

DATASET_SF_TL54_PATH = r"./a000_DATASET/SF-TL54/"
DATASET_SF_TL54_CROPPED_PATH = r"./a000_DATASET/SF-TL54_CROPPED/"

MODEL_NAME_LIST = ["Facenet512", "ArcFace"]
DETECTOR_NAME_LIST = ["mtcnn", "retinaface", "opencv"]

TEST_DEVICE = "cpu"
TEST_BATCH_SIZE = 1
TEST_NUM_SAMPLES_PER_EPOCH = 5000
TEST_MODEL_NAME = MODEL_NAME_LIST[0]
TEST_DETECTOR_NAME = DETECTOR_NAME_LIST[1]
TEST_LOG_PATH = r"./a002_model/a002_batch_test/log"
TEST_RESULT_RECORDER_PATH = (
    rf"{TEST_LOG_PATH}/{TEST_MODEL_NAME}_{TEST_DETECTOR_NAME}_result_recorder.json"
)
TEST_FINAL_CONFUSION_MATRIX_PATH = (
    rf"{TEST_LOG_PATH}/{TEST_MODEL_NAME}_{TEST_DETECTOR_NAME}_confusion-matrix.json"
)

TRAINING_OR_VALI_DEVICE = "cuda"
TRAINING_NUM_SAMPLES_PER_EPOCH = 10000
TRAINING_DETECTOR_NAME = DETECTOR_NAME_LIST[1]
TRAINING_INITIAL_LR = 4e-5
TRAINING_TOTAL_EPOCHS = 2
TRAINING_MINIMUM_LR = 0.0
TRAINING_SAVE_MODEL_INTERVAL_IN_EPOCHS = 1
TRAINING_BATCH_SIZE = 64
TRAINING_PRINT_INFO_INTERVAL_IN_ITERS = 1
TRAINING_SAVE_MODEL_TO_FOLDER = "./a002_model/a003_training/saved_history/models"
TRAINING_VALI_SET_RATIO = 0.1
TRAINING_USING_GRAY_IMAGE = True
TRAINING_TENSOR_BOARD_LOG_DIR = "./a002_model/a003_training/runs"

TRAINING_OR_VALI_WITH_QUANTIZATION = False

TRAINING_WHETHER_USING_SAVED_STATE = False

LOAD_FROM_STATE_PATH = (
    r"a002_model/a003_training/saved_history/models"
    r"/2025-01-02_13-43-19_epochs-2_iters-up-to-now-312.pth"
)

VALI_SAMPLES_NUM = 5000
VALI_BATCH_SIZE = 64
TRAINING_VALI_INTERVAL_IN_ITERS = 200
VALI_LOG_FOLDER = r"./a002_model/a003_training/saved_history/validation"
VALI_ANALYZE_USING_DETAILED_RESULT_JS_NAME = "---------.json"
LOSS_FUNC_MARGIN = 0.6  # 负样本距离减去正样本距离小于MARGIN的组需要学习，距离取值在0~2之间
LOSS_FUNC_SWAP = True
LOSS_FUNC_USING_SELF_DEFINED = False
LOSS_FUNC_WEIGHT_D_AN_PENALTY = 0

FASTAPI_UPLOAD_IMAGE_FOLDER = r"a003_fastapi/a001_images/a001_upload_images"
FASTAPI_CROP_IMAGE_FOLDER = r"a003_fastapi/a001_images/a002_crop"
FASTAPI_DEVICE = "cpu"
FASTAPI_USING_DETECTION_METHOD = "mtcnn"  # also can choose deepface or opencv or yolov11
if FASTAPI_USING_DETECTION_METHOD == "yolov11":
    FASTAPI_DETECTION_YOLO_MODEL_PATH = r"a001_test/a009_yolo11/models/yolov11s-face.pt"
FASTAPI_PORT = 8092
FASTAPI_LOG_JSON_FILE_PATH = r"a003_fastapi/a003_logs/log.json"
FASTAPI_USING_GRAY_IMAGE = True
FASTAPI_WITH_QUANTIZATION_MODEL = False
FASTAPI_INFERENCE_WITH_MAX_IMAGE_SIDE = 800

FLASK_PORT = 8092

DISTANCE_THRESHOLD = 0.5  # a float, 0~2
