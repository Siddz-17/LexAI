# 🎬 LexAI

LexAI is an intelligent YouTube video summarizer that transforms lengthy videos into concise, insightful summaries within seconds. Powered by LLama3 and built with ❤️ using Streamlit, LexAI helps you grasp key points quickly and even allows you to ask specific questions about the video content.

## 🚀 Features

- **YouTube Video Summarization:** Instantly generate concise summaries of YouTube videos.
- **Interactive Q&A:** Ask questions based on the generated summary and receive clear, specific answers.
- **Dynamic Typing Effect:** Enjoy a visually engaging typing animation while the summary is generated.
- **Video Information Display:** Automatically fetches and displays the video’s title and thumbnail.
- **Modern UI:** Clean and responsive interface with a sleek gradient background and customized buttons.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python (Groq API, YouTube Transcript API)
- **AI Model:** LLama3
- **Other Libraries:**
  - `aiohttp` for asynchronous HTTP requests
  - `dotenv` for environment variable management

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/lexai.git
   cd lexai
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the project root:
   ```env
   API_URL=http://localhost:8000
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 🌐 Usage

1. Enter the YouTube video URL in the input field.
2. Click **"Summarize Video"** to generate the summary.
3. View the video title, thumbnail, and dynamic summary.
4. Ask specific questions about the summary for detailed answers.

## 📦 API Endpoints

- `POST /api/video-info`: Fetch video details (title, thumbnail).
- `POST /api/summarize`: Generate summary from video transcript.
- `POST /api/answer`: Answer questions based on the summary.

## 🤖 AI Models

- **LLama3-70B:** Used for detailed summarization.
- **LLama3-8B:** Optimized for answering questions quickly.

## 📝 Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💬 Acknowledgements

- **LLama3** for powerful AI capabilities.
- **Streamlit** for the easy-to-use web framework.
- **YouTube Transcript API** for seamless transcript extraction.

---

Built with ❤️ by [Your Name](https://github.com/your-username).

