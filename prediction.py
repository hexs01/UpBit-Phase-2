import joblib
from sklearn.ensemble import RandomForestClassifier
import gradio as gr

model = joblib.load(r'random_forest_model.joblib')

slider1 = gr.Slider(minimum=0, maximum=1000, label="CAPEX (RM mil)")
slider2 = gr.Slider(minimum=0, maximum=1000, label="OPEX (RM mil)")
slider3 = gr.Slider(minimum=0, maximum=5, label="Performance")
slider4 = gr.Slider(minimum=0, maximum=1000, label="Revenue (RM mil)")

def prediction(first,second,third,forth):
    prediction = model.predict([[first,second,third,forth]])
    label = ['Not Affordable','Affordable']
    return label[prediction[0]]

demo = gr.Interface(
    fn=prediction,
    inputs=[slider1,slider2,slider3,slider4],
    outputs=["text"],
)

if __name__ == "__main__":
    demo.launch()