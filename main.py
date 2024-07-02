from flask import Flask, render_template, request, jsonify
import boto3

app = Flask(__name__, template_folder='/home/ec2-user/myapp1/templates')

# Initialize the Amazon Comprehend client
comprehend = boto3.client(service_name='comprehend', region_name='ca-central-1', use_ssl=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']
    
    # Get syntax (PoS) analysis
    pos_response = comprehend.detect_syntax(Text=text, LanguageCode='en')
    pos = pos_response['SyntaxTokens']
    
    # Get entity (NER) analysis
    ner_response = comprehend.detect_entities(Text=text, LanguageCode='en')
    ner = ner_response['Entities']
    
    return jsonify({'pos': pos, 'ner': ner})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

