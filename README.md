🐶 Dog Breed Image Classifier
    This project classifies pet images (with a focus on dog breeds) using a pre-trained convolutional neural network (CNN). It uses Python scripts to load images, classify them using models like ResNet, VGG, or AlexNet, and evaluate performance using a dog name reference file.
📌 Objective
    Classify whether the image is of a dog.

    If yes, identify the dog breed.

    Compare the prediction with the actual label extracted from the filename.

    Report classification accuracy and results.
 🧠 Supported Models
    AlexNet

    VGG

    ResNet
📁 Project Structure
    data/
    ├── pet_images/                 # Directory with dog/cat images
    ├── uploaded_images/           # Images for batch upload testing
    ├── __pycache__/               # Python bytecode
    ├── adjust_results4_isadog.py  # Determines if label/prediction is a dog
    ├── calculate_results_stats.py # Calculates stats on results
    ├── check_images.py            # Validates images for classification
    ├── classifier.py              # Handles model inference using pretrained models
    ├── classify_images.py         # Classifies each image using the selected model
    ├── get_input_args.py          # Parses command-line arguments
    ├── get_pet_labels.py          # Extracts pet labels from filenames
    ├── print_results.py           # Outputs performance results
    ├── dognames.txt               # Contains valid dog breed names
    ├── run_models_batch.sh        # Bash script to run classification batch
    ├── test_classifier.py         # Basic test runner
    └── imagenet1000_csid.txt      # Optional: Mapping for ImageNet class names

🖥️ How to Run

1. Clone the Repository
    git clone https://github.com/your-username/dog-breed-image-classifier.git
    cd dog-breed-image-classifier/data

 2. Install Requirements
    pip install torch torchvision

3. Run the Classifier
    python classify_images.py --dir pet_images --arch resnet --dogfile dognames.txt

4. Run with Uploaded Images
    python classify_images.py --dir uploaded_images --arch vgg --dogfile dognames.txt

🔧 CLI Argument Details
| Argument    | Description                                   | Example                  |
| ----------- | --------------------------------------------- | ------------------------ |
| `--dir`     | Folder with images to classify                | `--dir pet_images`       |
| `--arch`    | CNN model to use (`vgg`, `alexnet`, `resnet`) | `--arch resnet`          |
| `--dogfile` | File listing all valid dog breeds             | `--dogfile dognames.txt` |


📈 Output
    Shows how many images were classified correctly as dogs

    Shows how many breed matches occurred

    Shows statistics: % correct dogs, % correct breed, etc.

    Full result output if enabled via print_results.py

🧪 Example Output

    Number of Images: 40
    Number of Dog Images: 30
    Number of Correct Dog Classifications: 28
    Number of Correct Breed Classifications: 25

    % Correct Dogs: 93.3%
    % Correct Breed: 83.3%

📸 Sample Images
    You can test with:

    data/pet_images/dog_01.jpg

    data/uploaded_images/dog_02.jpg

📝 License
This project is licensed under the MIT License.