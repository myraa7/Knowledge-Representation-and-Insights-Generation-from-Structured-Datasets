import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import joblib
import traceback

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('titanic_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return {'message': 'Hello, World!'}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_data = np.array([
            data.get('Pclass', 1), 
            data.get('Sex', 0), 
            data.get('Age', 30), 
            data.get('SibSp', 0),
            data.get('Parch', 0), 
            data.get('Fare', 32.2), 
            data.get('Embarked', 0),
            data.get('Title', 0),
            data.get('Ticket_Len', 0), 
            data.get('Ticket_Prefix', 0),
            data.get('Cabin', 0)
        ]).reshape(1, -1)
        
        # Apply the scaler to the input data
        scaled_input = scaler.transform(input_data)
        
        # Make prediction using the scaled input
        prediction = model.predict(scaled_input)
        
        output = 'Survived' if prediction[0] == 1 else 'Did not survive'
        print(f"Prediction made: {output}")  # Server-side logging
        return jsonify(result=output)
    except Exception as e:
        print(f"Error occurred in /predict: {str(e)}")  # Server-side error logging
        traceback.print_exc()  # Print the traceback for debugging
        return jsonify(error=str(e)), 400

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.csv'):
        try:
            df = pd.read_csv(file)
            print("File successfully read into DataFrame")
            print(df.head())  # Print first few rows of the DataFrame for debugging
            df = preprocess_data(df)
            graphs = generate_graphs(df)
            return jsonify({
                'graphs': [{'title': title, 'image': image} for title, image in graphs]
            })
        except Exception as e:
            print(f"Error occurred while processing the file: {str(e)}")
            traceback.print_exc()  # Print the traceback for debugging
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file format. Please upload a CSV file.'}), 400

def preprocess_data(df):
    try:
        df['Age'] = df['Age'].fillna(df['Age'].mean())
        df['Fare'] = df['Fare'].fillna(df['Fare'].mean())
        df['Embarked'] = df['Embarked'].fillna('S')
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
        df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
        
        # Extract Title from Name
        df['Title'] = df['Name'].apply(lambda name: name.split(',')[1].split('.')[0].strip())
        df['Title'] = df['Title'].map({'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Dr': 4, 'Rev': 5, 'Col': 6, 'Major': 7, 'Mlle': 8, 'Countess': 9, 'Ms': 10, 'Lady': 11, 'Jonkheer': 12, 'Don': 13, 'Dona': 14, 'Mme': 15, 'Capt': 16, 'Sir': 17})

        # Handle missing Titles
        df['Title'] = df['Title'].fillna(-1)
        
        # Create Ticket Length Feature
        df['Ticket_Len'] = df['Ticket'].apply(lambda x: len(x))
        
        # Create Ticket Prefix Feature
        df['Ticket_Prefix'] = df['Ticket'].apply(lambda x: ''.join(filter(str.isalpha, x)))
        df['Ticket_Prefix'] = df['Ticket_Prefix'].apply(lambda x: 0 if x == '' else len(x))
        
        # Handle missing Cabin
        df['Cabin'] = df['Cabin'].apply(lambda x: 0 if pd.isna(x) else 1)

        return df
    except Exception as e:
        print(f"Error in preprocessing data: {str(e)}")
        traceback.print_exc()  # Print the traceback for debugging
        raise

def generate_graphs(df):
    graphs = []
    try:
        # Survival Rate by Gender
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Sex', y='Survived', data=df)
        plt.title('Survival Rate by Gender')
        plt.xlabel('Gender')
        plt.ylabel('Survival Rate')
        graphs.append(('Survival Rate by Gender', plt_to_base64()))

        # Survival Rate by Age
        df['age_cat'] = pd.cut(df['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80], labels=['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80'])
        plt.figure(figsize=(12, 6))
        sns.barplot(x='age_cat', y='Survived', data=df, ci=None)
        plt.title('Survival Rate by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Survival Rate')
        graphs.append(('Survival Rate by Age Group', plt_to_base64()))

        # Passenger Class Distribution
        plt.figure(figsize=(10, 6))
        sns.countplot(x='Pclass', data=df, palette='viridis')
        plt.title('Passenger Class Distribution')
        plt.xlabel('Passenger Class')
        plt.ylabel('Count')
        graphs.append(('Passenger Class Distribution', plt_to_base64()))

        # Fare Distribution among Survived and Not Survived
        plt.figure(figsize=(14, 6))
        sns.histplot(df[df['Survived'] == 1]['Fare'], kde=False, color='blue', label='Survived')
        sns.histplot(df[df['Survived'] == 0]['Fare'], kde=False, color='red', label='Not Survived')
        plt.title('Fare Distribution among Survived and Not Survived')
        plt.xlabel('Fare')
        plt.ylabel('Count')
        plt.legend()
        graphs.append(('Fare Distribution among Survived and Not Survived', plt_to_base64()))

        # Correlation Heatmap
        plt.figure(figsize=(14, 10))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap of Titanic Dataset')
        graphs.append(('Correlation Heatmap', plt_to_base64()))

    except Exception as e:
        print(f"Error in generating graphs: {str(e)}")
        traceback.print_exc()  # Print the traceback for debugging
        raise

    return graphs

def plt_to_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    plt.close()
    return graph

if __name__ == '__main__':
    app.run(debug=True)
