# 🎓 ElaRech – Multimodal Research Assistant

**ElaRech** is an intelligent, voice-interactive **multimodal research assistant** that helps students explore and understand visual academic content like diagrams, charts, handwritten notes, or research papers. Just **speak your query**, upload an image, and ElaRech will answer both visually and audibly.

📸 Demo
![ElaRech](https://github.com/user-attachments/assets/8ec8b595-45c1-4b48-a3ed-829e2752ccc6)

---


### 🧠 Model Used
- **Multimodal Model**: meta-llama/llama-4-scout-17b-16e-instruct via Groq API
- **Voice Recognition**: Whisper
- **TTS Engines**: Google gTTS & ElevenLabs

### Tech Stack
 **Groq API** – Ultra-fast LLM API
 **LLaMA-4 Vision Model** – meta-llama/llama-4-scout-17b-16e-instruct
 **Whisper** – For speech recognition
 **gTTS & ElevenLabs** – For voice output
 **Gradio** – For building the web interface

## 🔍 Features

- 🎙️ **Voice Input**: Speak your research question naturally.
- 🧠 **Multimodal AI**: Combines your voice query with an uploaded image to give smart, context-aware answers.
- 🖼️ **Image Understanding**: Upload diagrams, charts, handwritten pages, or screenshots — ElaRech understands them.
- 💬 **LLM-Powered Responses**: Powered by `meta-llama/llama-4-scout-17b-16e-instruct` via Groq API.
- 🔊 **Dual TTS Engines**: Replies are spoken aloud using both **gTTS** and **ElevenLabs**.
- 🌐 **Gradio Web Interface**: Clean, easy-to-use interface accessible from your browser.

---

## 📁 Project Structure
ElaRech/
├── gradio_app.py # Main app with Gradio interface 
├── brain_of_the_elaRech.py # Core logic for image + query processing 
├── .env \n
├── voice_of_researcher.py 
└── voice_of_user.py 


---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/iamafridi/elaRech.git
cd elaRech
```

### Set Environment Variables
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

### Run the App
python gradio_app.py

### 🎓 Example Use Case
Upload a biology diagram and ask:

🗣️ "Explain this process in simple terms."

📢 ElaRech will generate a voice and text response explaining the diagram based on your question.

📜 License
MIT License


### 👤 Author
Afridi Akbar Ifty
GitHub: https://github.com/iamafridi
Portfolio : https://iamafrididev.netlify.app
LinkedIn: [your-linkedin-profile](https://www.linkedin.com/in/iamafridi/) 



