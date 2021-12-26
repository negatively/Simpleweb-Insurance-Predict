from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('rfr.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    age, bmi, kids, sex, smoker = [x for x in request.form.values()]

    data = []

    data.append(int(age))
    if sex == 'Laki-laki':
        data.append(1)
    else:
        data.append(0)
    data.append(float(bmi))
    data.append(int(kids))
    if smoker == 'Ya':
        data.append(1)
    else:
        data.append(0)
    
    

    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', insurance_cost=output)


if __name__ == '__main__':
    app.run(debug=True)