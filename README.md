## END TO END ML PROJECT

```markdown
# Student Performance Indicator

This project is an end-to-end machine learning application that predicts student performance based on various parameters. The project includes data ingestion, transformation, model training, and prediction components.

## Project Structure

```
├── .ebextensions
│   └── python.config
├── artifacts
├── data.csv
├── model.pkl
├── preprocessor.pkl
├── test.csv
├── train.csv
├── catboost_info
├── notebook
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── templates
│   │   ├── home.html
│   │   ├── index.html
│   │   └── __init__.py
│   ├── application.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Necessary Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/student-performance-indicator.git
cd student-performance-indicator
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

### Project Components

- **Data Ingestion**: Reads and splits the data into train and test sets.
- **Data Transformation**: Applies preprocessing to the data.
- **Model Training**: Trains the machine learning model.
- **Prediction Pipeline**: Generates predictions using the trained model.

### Usage

1. **Data Exploration**:

   Explore the data using the provided Jupyter Notebooks in the `notebook` directory:
   
   - `1. EDA STUDENT PERFORMANCE.ipynb`
   - `2. MODEL TRAINING.ipynb`

2. **Training the Model**:

   Run the training pipeline to ingest data, transform it, and train the model:
   
   ```bash
   python src/pipeline/train_pipeline.py
   ```

3. **Making Predictions**:

   Use the prediction pipeline to make predictions on new data:
   
   ```bash
   python src/pipeline/predict_pipeline.py
   ```

4. **Running the Application**:

   The application includes a web interface for user interaction. Start the application with:
   
   ```bash
   python src/application.py
   ```

   Access the web interface at `http://127.0.0.1:5000/`.

### File Descriptions

- **artifacts/**: Contains generated model and preprocessor files.
- **data.csv**: The main dataset.
- **model.pkl**: The trained model file.
- **preprocessor.pkl**: The preprocessor file.
- **test.csv**: Test dataset.
- **train.csv**: Training dataset.
- **notebook/**: Jupyter Notebooks for exploratory data analysis and model training.
- **src/**: Source code directory.
  - **components/**: Contains the main components of the pipeline.
    - `data_ingestion.py`: Data ingestion code.
    - `data_transformation.py`: Data transformation code.
    - `model_trainer.py`: Model training code.
  - **pipeline/**: Pipeline scripts.
    - `predict_pipeline.py`: Script for making predictions.
    - `train_pipeline.py`: Script for training the model.
  - **templates/**: HTML templates for the web interface.
    - `home.html`: Home page for prediction input.
    - `index.html`: Index page with navigation.
  - `application.py`: Main application script.
  - `exception.py`: Custom exception handling.
  - `logger.py`: Logging setup.
  - `utils.py`: Utility functions.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: Project documentation.
- **requirements.txt**: Python dependencies.
- **setup.py**: Setup script for packaging.

- Thank you to the authors of the libraries and tools used in this project.
- Special thanks to the contributors and the community for their support.

