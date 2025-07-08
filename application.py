from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            carat=float(request.form.get('carat')), # type: ignore
            depth = float(request.form.get('depth')), # type: ignore
            table = float(request.form.get('table')), # type: ignore
            x = float(request.form.get('x')), # type: ignore
            y = float(request.form.get('y')), # type: ignore
            z = float(request.form.get('z')), # type: ignore
            cut = request.form.get('cut'), # type: ignore
            color= request.form.get('color'), # type: ignore
            clarity = request.form.get('clarity') # type: ignore
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('form.html',final_result=results)
    

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)