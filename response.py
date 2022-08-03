import transformers
import pickle
def sample_response(input_text):
    user_message=str(input_text).lower().strip()
    pickled_model = pickle.load(open('/content/drive/MyDrive/Bully_bot/model.pkl', 'rb'))
    x=pickled_model(user_message)[0]["label"]
    if x=='LABEL_1':
        return "This message might be offensive, do you want to kick this user out?"
    else:
        return "Not offensive"